from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import pandas as pd
import time
import random
import logging
from datetime import datetime
from typing import Dict, List, Optional

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='scraper.log'
)

class RestaurantScraper:
    def __init__(self):
        self.setup_browser()
        self.setup_logging()
        self.request_count = 0
        self.max_requests_per_minute = 10

    def setup_logging(self):
        self.logger = logging.getLogger(__name__)

    def setup_browser(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument(f'user-agent={UserAgent().random}')
        
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )
        self.wait = WebDriverWait(self.driver, 10)

    def rate_limit(self):
        self.request_count += 1
        if self.request_count >= self.max_requests_per_minute:
            time.sleep(60)
            self.request_count = 0
        else:
            time.sleep(random.uniform(2, 4))

    def validate_data(self, data: Dict) -> bool:
        required_fields = ['name', 'rating', 'address', 'phone']
        return all(data.get(field) != "N/A" for field in required_fields)

    def clean_text(self, text: Optional[str]) -> str:
        if not text:
            return "N/A"
        return ' '.join(text.strip().split())

    def scrape_restaurants(self, location: str, max_results: int = 20) -> List[Dict]:
        restaurants = []
        search_query = f"restaurants in {location}".replace(' ', '+')
        url = f"https://www.google.com/search?q={search_query}"
        
        try:
            self.logger.info(f"Starting scrape for {location}")
            self.driver.get(url)
            self.rate_limit()
            
            results_processed = 0
            while results_processed < max_results:
                try:
                    restaurant_elements = self.driver.find_elements(By.CSS_SELECTOR, 'div.VkpGBb')
                    
                    for element in restaurant_elements[results_processed:]:
                        if results_processed >= max_results:
                            break
                            
                        try:
                            soup = BeautifulSoup(element.get_attribute('innerHTML'), 'html.parser')
                            
                            restaurant_data = {
                                'name': self.clean_text(soup.select_one('span.OSrXXb')?.text),
                                'rating': self.clean_text(soup.select_one('span.rating')?.text),
                                'address': self.clean_text(soup.select_one('div.address')?.text),
                                'phone': self.clean_text(soup.select_one('div.phone')?.text)
                            }
                            
                            if self.validate_data(restaurant_data):
                                restaurants.append(restaurant_data)
                                results_processed += 1
                                self.logger.info(f"Scraped: {restaurant_data['name']}")
                            
                            self.rate_limit()
                            
                        except Exception as e:
                            self.logger.error(f"Error processing restaurant: {str(e)}")
                            continue
                    
                    last_height = self.driver.execute_script("return document.body.scrollHeight")
                    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(random.uniform(1, 2))
                    new_height = self.driver.execute_script("return document.body.scrollHeight")
                    
                    if new_height == last_height or not restaurant_elements:
                        break
                    
                except Exception as e:
                    self.logger.error(f"Error during pagination: {str(e)}")
                    break
                
        except Exception as e:
            self.logger.error(f"Critical error during scraping: {str(e)}")
        
        finally:
            self.driver.quit()
            
        return restaurants

    def save_data(self, data: List[Dict]) -> str:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'restaurants_{timestamp}.csv'
        
        try:
            df = pd.DataFrame(data)
            df.to_csv(filename, index=False)
            self.logger.info(f"Successfully saved {len(data)} records to {filename}")
            return filename
        except Exception as e:
            self.logger.error(f"Error saving data: {str(e)}")
            raise

def main():
    try:
        print("Restaurant Data Scraper")
        print("----------------------")
        location = input("Enter location (e.g., 'Downtown Toronto'): ")
        max_results = int(input("Enter maximum number of results (default 20): ") or 20)
        
        scraper = RestaurantScraper()
        print(f"Starting scrape for {location}...")
        print("Check scraper.log for detailed progress")
        
        restaurants = scraper.scrape_restaurants(location, max_results)
        if restaurants:
            filename = scraper.save_data(restaurants)
            print(f"Successfully scraped {len(restaurants)} restaurants")
            print(f"Data saved to {filename}")
        else:
            print("No restaurants found or all results were invalid")
            
    except Exception as e:
        logging.error(f"Application error: {str(e)}")
        print(f"An error occurred. Check scraper.log for details")

if __name__ == "__main__":
    main()

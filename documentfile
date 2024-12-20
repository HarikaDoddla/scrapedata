# Restaurant Data Scraper Documentation

## Overview
The Restaurant Scraper is a Python-based web scraping tool designed to collect restaurant information from Google Search results. It uses Selenium WebDriver for browser automation and BeautifulSoup for HTML parsing.

## Table of Contents
1. [Features](#features)
2. [Dependencies](#dependencies)
3. [Installation](#installation)
4. [Class Structure](#class-structure)
5. [Usage](#usage)
6. [Data Format](#data-format)
7. [Error Handling](#error-handling)
8. [Best Practices](#best-practices)
9. [Limitations](#limitations)
10. [Maintenance](#maintenance)

## Features
* Automated scraping of restaurant data from Google Search
* Rate limiting to prevent blocking
* Data validation and cleaning
* CSV export functionality
* Detailed logging
* Configurable search parameters

## Dependencies
Required Python packages:
```python
selenium==4.x.x
beautifulsoup4==4.x.x
pandas
webdriver_manager
fake_useragent
logging
typing
```

## Installation
1. Clone the repository
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure Chrome browser is installed
4. ChromeDriver will be automatically managed by webdriver_manager

## Class Structure

### RestaurantScraper Class

#### Initialization Methods

##### `__init__()`
* Initializes the scraper with browser setup and logging configuration
* Sets rate limiting parameters
* Configures initial request count

##### `setup_browser()`
* Configures Chrome WebDriver with headless mode
* Sets browser options:
  - Headless mode enabled
  - GPU disabled
  - Window size: 1920x1080
  - Random user agent

##### `setup_logging()`
* Configures logging with timestamp and level information
* Creates log file: 'scraper.log'
* Sets logging format: '%(asctime)s - %(levelname)s - %(message)s'

#### Core Methods

##### `rate_limit()`
* Purpose: Manages request frequency
* Functionality:
  - Limits to 10 requests per minute
  - Adds random delays between 2-4 seconds
  - Resets counter after reaching limit

##### `validate_data(data: Dict) -> bool`
* Validates required fields:
  - name
  - rating
  - address
  - phone
* Returns boolean indicating data validity

##### `clean_text(text: Optional[str]) -> str`
* Cleans text data by removing extra spaces
* Handles None values
* Returns cleaned string or "N/A"

##### `scrape_restaurants(location: str, max_results: int = 20) -> List[Dict]`
* Parameters:
  - location: Target area for restaurant search
  - max_results: Maximum number of restaurants to scrape (default: 20)
* Returns: List of restaurant dictionaries
* Implements scrolling for pagination
* Handles rate limiting

##### `save_data(data: List[Dict]) -> str`
* Saves scraped data to CSV
* Filename format: 'restaurants_YYYYMMDD_HHMMSS.csv'
* Returns: Generated filename
* Uses pandas for data export

## Usage

### Basic Usage
```python
def main():
    # Create scraper instance
    scraper = RestaurantScraper()
    
    # Set location and max results
    location = "Downtown Toronto"
    max_results = 20
    
    # Run scraper
    restaurants = scraper.scrape_restaurants(location, max_results)
    
    # Save results
    if restaurants:
        filename = scraper.save_data(restaurants)
        print(f"Data saved to {filename}")
```

### Command Line Interface
Run the script directly:
```bash
python restaurant_scraper.py
```
Follow the prompts to enter:
* Location
* Maximum number of results

## Data Format

### Input
* Location string
* Maximum results number (optional)

### Output CSV Structure
```csv
name,rating,address,phone
Restaurant Name,X.X,Full Address,Phone Number
```

### Data Dictionary
* name: String - Restaurant name
* rating: Float - Google rating (0.0-5.0)
* address: String - Full address including postal code
* phone: String - Contact number with area code

## Error Handling

### Exception Types Handled
* TimeoutException
* NoSuchElementException
* General exceptions

### Logging
* Log file: scraper.log
* Log levels:
  - INFO: General progress
  - ERROR: Exceptions and failures
  - DEBUG: Detailed operation info

## Best Practices

### Rate Limiting
* Maximum 10 requests per minute
* Random delays between requests
* 60-second pause after reaching limit

### Data Validation
* Required field checking
* Data cleaning and standardization
* Missing value handling

### Browser Configuration
* Headless mode for efficiency
* User agent rotation
* Appropriate window sizing

## Limitations
1. Depends on Google's search results structure
2. Rate limited to 10 requests per minute
3. Maximum results configurable but limited by available data
4. Requires stable internet connection
5. May be affected by Google's layout changes

## Maintenance

### Regular Updates Required For
* CSS selectors
* User agent strings
* Rate limiting parameters
* Browser compatibility

### Recommended Maintenance Schedule
* Monthly checks for layout changes
* Quarterly dependency updates
* Annual code review for optimization

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to the branch
5. Create a Pull Request

## License
MIT License - see LICENSE.md for details

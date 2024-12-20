# Restaurant Scraper

A Python web scraper that collects restaurant information from Google search results using Selenium and BeautifulSoup.

## Features

- Scrapes restaurant names, ratings, addresses, and phone numbers
- Implements rate limiting to prevent IP blocking
- Validates and cleans scraped data
- Saves results in CSV format
- Includes detailed logging
- Uses headless browser mode
- Rotates user agents

## Prerequisites

- Python 3.7 or higher
- Google Chrome browser
- Chrome WebDriver (automatically installed by webdriver-manager)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/restaurant-scraper.git
cd restaurant-scraper
```

2. Install required packages:
```bash
pip install selenium beautifulsoup4 pandas webdriver_manager fake-useragent
```

## Usage

1. Run the script:
```bash
python scraper.py
```

2. Enter requested information:
- Location (e.g., "Downtown Toronto")
- Maximum number of results to collect (default: 20)

3. The script will:
- Start scraping data
- Show progress in the console
- Save detailed logs to scraper.log
- Save results to a CSV file with timestamp

## Output

The script generates two files:
1. `restaurants_YYYYMMDD_HHMMSS.csv` - Contains scraped data
2. `scraper.log` - Contains detailed execution logs

CSV columns:
- name: Restaurant name
- rating: Google rating
- address: Physical address
- phone: Contact number

## Error Handling

- The script includes comprehensive error handling
- All errors are logged to scraper.log
- Failed scrapes are reported but don't stop execution
- Data validation ensures quality of collected information

## Rate Limiting

- Maximum 10 requests per minute
- Random delays between requests (2-4 seconds)
- Automatic pause when limit is reached

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Disclaimer

This scraper is for educational purposes only. Before scraping any website, ensure you have permission and are following the website's terms of service and robots.txt guidelines.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

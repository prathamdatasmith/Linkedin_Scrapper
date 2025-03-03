# LinkedIn Job Scraper

A robust Python-based LinkedIn job scraping tool developed by Prathamesh Ettam. This tool helps in automated collection of job listings from LinkedIn with customizable filters for location, posting time, and work type.

## 🚀 Features

- Scrape job listings from multiple Indian cities
- Customizable search filters:
  - Job posting timeframe (24h, Week, Month)
  - Work type (Remote, Hybrid, On-site)
  - Location-based search using LinkedIn's geoIDs
- Detailed job information extraction:
  - Job title
  - Company name
  - Location
  - Complete job description
  - Job URL
- Rate limiting protection
- Data export to CSV format

## 📋 Requirements

```bash
pip install requests beautifulsoup4
```

## 🎯 Project Structure

```
/d:/sccraP/
├── main.py           # Entry point of the application
├── config.py         # Configuration settings and constants
├── utils.py          # Utility functions for URL parsing and job description extraction
└── linkedin_scraper.py  # Core scraping functionality
```

## 🔧 Usage

1. Clone the repository
2. Install the required dependencies
3. Run the scraper:

```bash
python main.py
```

### Customizing the Search

Edit the parameters in `main.py` to modify your search:

```python
keywords = "Data Engineer"  # Change to your desired job title
scraper.scrape_jobs(
    keywords,
    "India",             # Location
    GEO_IDS["India"],    # Geographic ID
    "Past Month",        # Time filter
    "On-Site"           # Work type
)
```

Available options:
- Time filters: "Past 24 hours", "Past Week", "Past Month"
- Work types: "On-Site", "Remote", "Hybrid"
- Locations: Multiple Indian cities (Mumbai, Chennai, Pune, etc.)

## 📊 Output

The scraper generates CSV files with the naming convention:
```
{location}_{keywords}_{timeframe}_{worktype}.csv
```

Each CSV contains:
- Job ID
- Job Title
- Company Name
- Location
- Job Link
- Full Job Description

## ⚠️ Important Notes

- Respect LinkedIn's terms of service and rate limits
- Use reasonable delays between requests
- The tool is for educational purposes only

## 🛠️ Developer

Developed by **Prathamesh Ettam**

This project demonstrates the practical application of:
- Web scraping with BeautifulSoup
- HTTP request handling
- Rate limiting and retry logic
- Object-oriented programming in Python
- Data processing and CSV handling

## 📝 License

This project is for educational purposes. Please respect LinkedIn's terms of service when using this tool.
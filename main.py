from config import GEO_IDS
from linkedin_scraper import LinkedInJobScraper

def main():
    scraper = LinkedInJobScraper()
    keywords = "Data Engineer"
    
    # Example usage
    scraper.scrape_jobs(keywords, "India", GEO_IDS["India"], "Past Month", "On-Site")
    
    # Uncomment to run for other configurations
    # scraper.scrape_jobs(keywords, "Chennai", GEO_IDS["Chennai"], "Past 24 hours", "Hybrid")
    # scraper.scrape_jobs(keywords, "Pune", GEO_IDS["Pune"], "Past Month", "On-Site")
    # scraper.scrape_jobs(keywords, "Bengaluru", GEO_IDS["Bengaluru"], "Past Week", "Remote")

if __name__ == "__main__":
    main()

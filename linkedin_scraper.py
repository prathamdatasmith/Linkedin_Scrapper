import time
import random
import csv
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode
from config import HEADERS, BASE_URL, JOBS_PER_PAGE, TIME_FILTERS, WORK_TYPE_FILTERS
from utils import extract_job_id, get_job_description

class LinkedInJobScraper:
    def __init__(self):
        self.seen_job_ids = set()
        self.processed_jobs = 0

    def _generate_file_name(self, city_name, keywords, time_filter, work_type):
        return f"{city_name.lower()}_{keywords.replace(' ', '_')}_{time_filter.replace(' ', '_')}_{work_type}.csv"

    def _process_job_listing(self, job, writer):
        href_link = job.find('a', class_='base-card__full-link')['href']
        job_id = extract_job_id(href_link)
        
        if not job_id or job_id in self.seen_job_ids:
            return False

        self.seen_job_ids.add(job_id)
        title = job.find('h3', {'class': 'base-search-card__title'}).text.strip()
        company = job.find('a', {'class': 'hidden-nested-link'}).text.strip()
        location_text = job.find('span', {'class': 'job-search-card__location'}).text.strip()
        job_description = get_job_description(href_link)

        writer.writerow([job_id, title, company, location_text, href_link, job_description])
        return True

    def scrape_jobs(self, keywords, city_name, geo_id, time_filter, work_type):
        """Main method to scrape LinkedIn job listings."""
        file_name = self._generate_file_name(city_name, keywords, time_filter, work_type)
        self.processed_jobs = 0

        with open(file_name, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Job ID", "Job Title", "Company Name", "Location", "Job Link", "Job Description"])

            page = 0
            while True:
                if not self._process_page(page, keywords, city_name, geo_id, time_filter, work_type, writer):
                    break
                page += 1
                time.sleep(random.uniform(5, 10))

        print(f"🎉 Scraping completed for {city_name}. Total unique jobs processed: {self.processed_jobs}")
        print(f"📁 Data saved in `{file_name}`")

    def _process_page(self, page, keywords, city_name, geo_id, time_filter, work_type, writer):
        params = {
            'keywords': keywords,
            'location': city_name,
            'geoId': geo_id,
            'start': page * JOBS_PER_PAGE,
            'position': 1,
            'pageNum': page,
            'f_TPR': TIME_FILTERS[time_filter],
            'f_WT': WORK_TYPE_FILTERS[work_type],
        }
        url = f'{BASE_URL}?{urlencode(params)}'

        response = self._make_request(url)
        if not response:
            return False

        soup = BeautifulSoup(response.text, 'html.parser')
        job_listings = soup.find_all('div', {'class': 'job-search-card'})

        if not job_listings:
            print(f"✅ No more job listings found for {city_name}.")
            return False

        for job in job_listings:
            try:
                if self._process_job_listing(job, writer):
                    self.processed_jobs += 1
                time.sleep(random.uniform(3, 7))
            except Exception as e:
                print(f"⚠️ Error processing job listing: {e}")
                continue

        print(f"✅ Finished page {page + 1} for {city_name}, moving to next page...")
        return True

    def _make_request(self, url):
        """Make HTTP request with retry logic."""
        while True:
            response = requests.get(url, headers=HEADERS)
            if response.status_code == 429:
                print("⚠️ Rate limit hit. Sleeping for 60 seconds and retrying...")
                time.sleep(60)
                continue
            if response.status_code != 200:
                print(f"❌ Failed to fetch page. Status code: {response.status_code}")
                return None
            return response

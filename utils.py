from urllib.parse import urlparse, parse_qs
import requests
from bs4 import BeautifulSoup
from config import HEADERS

def extract_job_id(url):
    """Extract the LinkedIn job ID from the job URL."""
    try:
        if 'currentJobId=' in url:
            return parse_qs(urlparse(url).query)['currentJobId'][0]
        else:
            return url.split('view/')[1].split('?')[0]
    except Exception as e:
        print(f"Error extracting job ID from URL {url}: {e}")
        return None

def get_job_description(url):
    """Fetch job description from job page."""
    try:
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            desc = soup.find('div', {'class': 'description__text'})
            return desc.text.strip() if desc else "Description not available"
    except Exception as e:
        print(f"Error fetching job description: {e}")
    return "Failed to fetch description"

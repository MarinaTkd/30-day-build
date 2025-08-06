import requests
from bs4 import BeautifulSoup
import logging
from requests.exceptions import RequestException, Timeout

def fetch_clean_text(url):
    """
    Fetches the main textual content from the given URL.
    Returns the clean text or None if fetching fails.
    """
    try: 
        #send a HTTP GET request to the URL
        response = requests.get(url, timeout = 10)
        response.raise_for_status() #raise an error if the request failed
        logging.debug("Content fetched successfully, length: %d", len(response.text))
    except requests.exceptions.RequestException as e: 
        logging.error(f"[ERROR] Failed to fetch URL:{e}")
        return None 
    try:
        #parse the HTML content with BeautifulSoup 
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')

        if not paragraphs:
            logging.warning("No <p> tags found at URL: %s", url)
            return None

        #remove script and style elements
        for tag in soup(['script', 'style']):
            tag.decompose

        text = soup.get_text(separator = ' ', strip = True)

        return text
    
    except Timeout: 
        logging.error("Timeout occurred while fetching: %s", url)
    except RequestException as e:
        logging.error("Request faild for %s; %s", url, str(e))
    
    except Exception as e:
        logging.exception("Unexpected error during scraping: %s", url)
        
    
    return None 
    

# # TESTING

# if __name__=="__main__":
#     url = "https://www.novinky.cz/clanek/domaci-riziko-pro-narodni-bezpecnost-europoslance-dostala-vyhostili-z-moldavska-40531996#dop_ab_variant=0&dop_source_zone_name=novinky.sznhp.box&source=hp&seq_no=1&utm_campaign=&utm_medium=z-boxiku&utm_source=www.seznam.cz"
#     clean_text = fetch_clean_text(url)

#     if clean_text:
#         print("Fetched text (first 500 characters):\n")
#         print(clean_text[:500])
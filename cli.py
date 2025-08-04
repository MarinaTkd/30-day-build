import logging

logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s [%(levelname)s] %(message)s"
)


from scraper import fetch_clean_text
from agent import create_summary, extract_topics

def main():
    url = input("Enter the URL to summarize: ").strip()

    text = fetch_clean_text(url)
    if not text: 
        logging.error("Failed to fetch or extract text from the URL")
        return 
    
    summary = create_summary(text)
    topics = extract_topics(text)

    print("\n📝 Summary:\n")
    print(summary)

    print("\n🔑 Extracted Topics:")
    print(topics)

if __name__ == "__main__":
    main()
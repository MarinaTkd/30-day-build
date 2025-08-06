import logging

logging.basicConfig(
    level = logging.INFO,
    format = "%(asctime)s [%(levelname)s] %(message)s"
)


from scraper import fetch_clean_text
from agent import create_summary, extract_topics

def main():
    try:
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
        
    except KeyboardInterrupt:
        logging.warning("Operation cancelled by user.")
    except Exception as e:
        logging.exception(f"Unexpected error in CLI: {e}")


if __name__ == "__main__":
    main()
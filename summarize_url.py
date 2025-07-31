from fetch_page import fetch_clean_text
from send_prompt import create_summary, extract_topics



def summarise_url(url):
    """
    Fetches text from a given URL and returns a GPT-generated summary.
    """
    fetched_text = fetch_clean_text(url)
    summary = create_summary(fetched_text)
    topics = extract_topics(fetched_text)

    return summary, topics


if __name__ == "__main__":
    passed_url = input("Please enter URL to summarise: ".strip())

    if passed_url:
        summary, topics = summarise_url(passed_url)

        if summary:
            print("Here is your summary: \n")
            print(summary)
        if topics: 
            print("--------------------------\n")
            print("Here are you main 5 topics / keywords from the text: \n")
            print(topics)
    else: 
        print("No URL provided.")
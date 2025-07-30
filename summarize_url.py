from fetch_page import fetch_clean_text
from send_prompt import create_summary


def summarise_url(url):
    """
    Fetches text from a given URL and returns a GPT-generated summary.
    """
    fetched_text = fetch_clean_text(url)
    summary = create_summary(fetched_text)

    return summary


if __name__ == "__main__":
    passed_url = input("Please enter URL to summarise: ".strip())

    if passed_url:
        summarised_text = summarise_url(passed_url)

        if summarised_text:
            print("Here is your summary: \n")
            print(summarised_text)
    else: 
        print("No URL provided.")
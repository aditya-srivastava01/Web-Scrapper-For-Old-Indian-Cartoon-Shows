import random
import requests
from bs4 import BeautifulSoup

# Define a dictionary of intents and their corresponding responses
intent_responses = {
    "greeting": ["Hi!", "Hello!", "Hey there! How can I assist you with Amazon products today?"],
    "product_info": [
        "Sure! Let me find that information for you.",
        "Of course! I can help you with that.",
        "Absolutely! I'll get the details you're looking for."
    ],
    "fallback": [
        "I'm sorry, I didn't understand that.",
        "Could you please rephrase that?",
        "I'm still learning. Can you be more specific?"
    ]
}

# Function to extract product details from Amazon URL
def extract_product_details(url):
    from selectorlib import Extractor
    import requests 
    import json 
    from time import sleep

    # Create an Extractor by reading from the YAML file
    e = Extractor.from_yaml_file('selectors.yml')
    headers = {
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.amazon.com/',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    # Download the page using requests
    print("Downloading %s"%url)
    r = requests.get(url, headers=headers)
    # Simple check to check if page was blocked (Usually 503)
    if r.status_code > 500:
        if "To discuss automated access to Amazon data please contact" in r.text:
            print("Page %s was blocked by Amazon. Please try using better proxies\n"%url)
        else:
            print("Page %s must have been blocked by Amazon as the status code was %d"%(url,r.status_code))
        return None
    # Pass the HTML of the page and create 
    print(r.text)
    return r.text

    # product_data = []
    # with open("urls.txt",'w+') as urllist, open('output.jsonl','w+') as outfile:
    #     for url in urllist.read().splitlines():
    #         data = scrape(url) 
    #         if data:
    #             json.dump(data,outfile)
    #             outfile.write("\n")
    #             # sleep(5)
        

# Main loop to get user input and generate responses
print("ChatBot: Hello! How can I assist you with Amazon products today?")
while True:
    user_input = input("User: ").strip()

    if user_input.lower() == "exit":
        print("ChatBot: Goodbye!")
        break

    if "amazon" in user_input.lower():
        product_details = extract_product_details(user_input)
        if product_details:
            print("ChatBot:", intent_responses["product_info"][0])
            # Handle extracted product details and continue the conversation
            while True:
                user_question = input("User: ").strip()
                # Implement logic to respond to user's questions about the product
                if user_question.lower() == "exit":
                    print("ChatBot: Goodbye!")
                    break
        else:
            print("ChatBot: I couldn't extract product details from the URL.")

    else:
        intent_matched = False
        for intent in intent_responses:
            if any(response.lower() in user_input.lower() for response in intent_responses[intent]):
                print("ChatBot:", random.choice(intent_responses[intent]))
                intent_matched = True
                break

        if not intent_matched:
            print("ChatBot:", random.choice(intent_responses["fallback"]))

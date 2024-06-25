import requests
import json

API_KEY = 'SikRYVB5fGslAVtLSsk8ct6L0UafDszyS8M7e0B6'
ENDPOINT = 'https://api.cohere.ai/v1/classify'  

def get_sentiment(text):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json',
    }
    data = {
        'inputs': [text],
        'examples': [
            {"text": "I love this!", "label": "positive"},
            {"text": "This is great!", "label": "positive"},
            {"text": "This is amazing!", "label": "positive"},
            {"text": "I am so happy with this.", "label": "positive"},
            {"text": "I hate this.", "label": "negative"},
            {"text": "This is awful.", "label": "negative"},
            {"text": "I am very disappointed.", "label": "negative"},
            {"text": "This is terrible.", "label": "negative"},
            {"text": "It's okay, not great.", "label": "neutral"},
            {"text": "It's fine, not bad.", "label": "neutral"},
            {"text": "It's decent.", "label": "neutral"},
        ]
    }
    response = requests.post(ENDPOINT, headers=headers, data=json.dumps(data))
    
    # print the status code and response (debug output)
    # print(f"Status Code: {response.status_code}")
    # print(f"Response: {response.text}")
    
    if response.status_code == 200:
        results = response.json().get('classifications', [])
        if results:
            return results[0]['prediction']
        else:
            return 'No sentiment found'
    else:
        return f"Error: {response.status_code} - {response.text}"

def analyze_reviews(reviews):
    sentiments = {'positive': 0, 'neutral': 0, 'negative': 0}
    for review in reviews:
        sentiment = get_sentiment(review)
        # print each review's sentiment (debug)
        # print(f"Review: {review} -> Sentiment: {sentiment}") 
        if sentiment in sentiments:
            sentiments[sentiment] += 1
    return sentiments

if __name__ == "__main__":
    # example reviews
    customer_reviews = [
        "I love this product! It works perfectly.",
        "It's okay, not the best but not the worst.",
        "I'm very disappointed. It broke after a week."
    ]
    
    results = analyze_reviews(customer_reviews)
    print("Sentiment Analysis Results:")
    print(f"Positive: {results['positive']}")
    print(f"Neutral: {results['neutral']}")
    print(f"Negative: {results['negative']}")

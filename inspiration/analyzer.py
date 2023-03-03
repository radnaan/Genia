import nltk

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
import praw
import googleapiclient.discovery
import googleapiclient.errors
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Reddit API credentials
reddit_client_id = 'your_reddit_client_id'
reddit_client_secret = 'your_reddit_client_secret'
reddit_user_agent = 'your_reddit_user_agent'
reddit_username = 'your_reddit_username'
reddit_password = 'your_reddit_password'

# YouTube API credentials
youtube_api_key = 'your_youtube_api_key'

# Initialize the Reddit API client
reddit = praw.Reddit(client_id=reddit_client_id,
                     client_secret=reddit_client_secret,
                     user_agent=reddit_user_agent,
                     username=reddit_username,
                     password=reddit_password)

# Get the top 10 trending topics on Reddit
reddit_trends = reddit.subreddit('all').hot(limit=10)

# Initialize the YouTube API client
youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=youtube_api_key)

# Get the top 10 trending topics on YouTube
youtube_trends = youtube.videos().list(part='snippet', chart='mostPopular', regionCode='US', videoCategoryId='').execute()['items'][:10]

# Define the NLP preprocessing functions
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    tokens = [token for token in tokens if token.isalpha()]
    tokens = [token for token in tokens if token not in stop_words]
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return tokens

# Analyze the trending topics and identify the most relevant subreddits
subreddits = set()
for trend in reddit_trends:
    tokens = preprocess_text(trend.title)
    tags = nltk.pos_tag(tokens)
    nouns = [word for word, pos in tags if pos.startswith('N')]
    for noun in nouns:
        subreddit = reddit.subreddit(noun)
        if subreddit:
            subreddits.add(subreddit.display_name)

print('Relevant subreddits on Reddit:', subreddits)

# Print the trending topics
print('Reddit trends:')
for trend in reddit_trends:
    print(trend.title)
    
print('YouTube trends:')
for trend in youtube_trends:
    print(trend['snippet']['title'])

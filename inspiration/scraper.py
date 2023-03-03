import praw
import googleapiclient.discovery
import googleapiclient.errors

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

# Print the trending topics
print('Reddit trends:')
for trend in reddit_trends:
    print(trend.title)
    
print('YouTube trends:')
for trend in youtube_trends:
    print(trend['snippet']['title'])

import praw
import openai

# Set up the OpenAI API client
openai.api_key = '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'

# Set up the Reddit API client
reddit = praw.Reddit(
    client_id='gXXLFD9GbXhvZ-gY9TBfrg',
    client_secret='3rB9FLDEkRJ8OS7occwyjfdp01OjJw',
    user_agent='Josuke',
)

def get_relevant_subreddits(topic):
    """Find relevant subreddits for a given topic"""
    search_results = reddit.subreddit('all').search(topic, limit=5)
    subreddits = [result.subreddit.display_name for result in search_results]
    return subreddits

def get_top_posts(subreddits):
    """Get the top posts from relevant subreddits"""
    posts = []
    for subreddit in subreddits:
        subreddit = reddit.subreddit(subreddit)
        for post in subreddit.top(limit=5):
            if not post.stickied:
                post_text = post.title + post.selftext
                if len(post_text) > 4000:
                    post_text = post_text[:4000]
                posts.append(post_text)
    return posts

def generate_title_and_script(posts):
    """Generate a new title and script using GPT-3"""
    prompt = ('Generate video title, script based on these top posts from subreddits.'+ '\n'.join(posts))[:300]

    model = 'text-davinci-002'
    temperature = 0.5

    response = openai.Completion.create(
        model=model,
        prompt=prompt,
        temperature=1,
        n=1,
        max_tokens=4000-len(prompt),
        stop=None,
        timeout=60
    )

    print(response)
    title = response.choices[0].text.strip()
    script = response.choices[0].text.strip()

    return title, script

# Example usage
topic = 'horror stories'
subreddits = get_relevant_subreddits(topic)
posts = get_top_posts(subreddits)
title, script = generate_title_and_script(posts)

print('Relevant subreddits:', subreddits)
print('Generated title:', title)
print('Generated script:', script)

import feedparser
import requests

# A form to get new feeds
def get_new_podcast(podcast_url):
    new_podcast = requests.get(podcast_url)
    feed = feedparser.parse(new_podcast.content)
    # handle getting all new feed episodes
    for episodes in feed['items']:
        print([episodes][0]['links'][0]['href'])
import tweepy
consumerKey = 'MjJXXtkO9M35P9INiPT0gVTBV'
consumerSecret = '1mukbIPFUXUMuo1lJQddsJWySXK07lT0fi56BjQBQyWNglGsE4'
accessToken = '76703201-bX4WIeUECn7fg88DDxafci5ijTQ4LIu44odEZlJB2'
accessTokenSecret = 'r10v84iSPIah6ygUaiIu1pvllum0tjyxXCHy1fpHHjldB'
callback_url = 'http://localhost:5000/callback'

def auth():
    authorize = tweepy.OAuthHandler(consumerKey, consumerSecret, callback_url)


# auth.set_access_token(accessToken, accessTokenSecret)
# api = tweepy.API(auth)

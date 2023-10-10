import tweepy as tp
import json

API_KEY = 'OYngCpNzt2IAp8354HVzSpUpE'
API_SECRET_KEY = 'imV3AQHuVFn4iIiuMf9c7Gh7oM3JnAWhJ3R8SCLIEKMWoyMEgB'
BEARER_TOKEN  = 'AAAAAAAAAAAAAAAAAAAAAM0FigEAAAAAYE8iYluOHLhF9LH7oAFiAivBul0%3DZ5qCajIi1xehXJ2zpXtKE5A7x4WmDXhBg9wzQRaCGE8PmFPIOV'
ACCESS_TOKEN = '1583197037033562135-0IqXbzoCEwBpHpABbVAazGE15OvW6G'
ACCESS_TOKEN_SECRET = 'ZEj3yYCkZVYmxhJohsny0lKPaQ2ZZjKwd6yUNzDnzjX0M'
CLIENT_ID = 'YlViTkNlX19GQk1sSXRFTEs1aFI6MTpjaQ'
CLIENT_SECRET = 'o3F64GJkem5Jcyj8k6rueu-OGeiVH1WbJ04r_rqnkdtJ-7cXV6'

auth = tp.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tp.API(auth)

def PublicarTweet(message):
    api.update_status(status=message)

def ImprimirTimeline():
    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(f'{tweet.user.screen_name}:\n{tweet.text}\n{"*"*60}')

def BuscarTweets(palabra):
    id = None
    count = 0
    while count <= 50:
        tweets = api.search_tweets(q='#'+palabra, lang="en", max_id=id)
        for tweet in tweets:
            f = open('./News.txt', 'a', encoding='utf-8')
            f.write(tweet.json + '\n - ')
            f.close
            count += 1
        id = tweet.id

# filtrar por palabras
# la api.filter(languages=['es'], track=["Madrid Londres"])


def Busqueda():
    tweet_list = []
    for t in tp.Cursor(api.search_tweets, q='#News', lang='en', count=100).items(100):
        tweet_json = json.dumps(t._json)
        tweet_list.append(tweet_json)
    return tweet_list

lista = Busqueda()

for obj in lista:
    print(obj)

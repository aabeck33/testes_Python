'''
    Acesso ao Twitter, Facebook e Instagram

    AppName: aabeck_search

    https://docs.tweepy.org/en/stable/
    https://developer.twitter.com/en/portal

    https://developers.facebook.com/
    https://developers.facebook.com/docs/instagram-basic-display-api/reference

    https://levelup.gitconnected.com/automating-instagram-posts-with-python-and-instagram-graph-api-374f084b9f2b
    https://www.google.com/search?q=minera%C3%A7%C3%A3o+de+dados+com+python&oq=minera%C3%A7%C3%A3o+de+dados+com+python&aqs=chrome..69i57j0i22i30l3.7550j0j7&sourceid=chrome&ie=UTF-8

'''
import tweepy as tw
import pandas as pd

query = 'União+Química'

consumer_key = 'pe4muAUluJ9nkSlBTtD9Bu9d1'
consumer_secret='5tvGT9foFlqKKM1rShvJN5Lgl23f8WEM2hIEOEcpkPztbufzcP'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAHHIggEAAAAAa4gxFjKd2OPePucyuLm09gavApQ%3DzeNqIREB6l2TK4YVrwoUPZpIESdj0sSf5XxgVSDLFfl2xL8FP0'

access_token = '33373360-RVznNvUK6sbzCxItmTM5YXuBTVL67S0LyWGeK1afJ'
access_token_secret = 'TkzTOvsNfFO9EJSiZ3XxssdN5P6vv4KPneilaqFlcfWLz'

auth = tw.OAuth1UserHandler(
   consumer_key, consumer_secret, access_token, access_token_secret
)

#cliente = tw.API(auth)

cliente = tw.Client(bearer_token=bearer_token, 
            consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, 
            access_token_secret=access_token_secret)

resultado = cliente.search_recent_tweets(query, max_results=100)
print(resultado)
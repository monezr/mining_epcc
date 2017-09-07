import tweepy

from tweepy import OAuthHandler

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth)

opcion = int(input("\nMENU\n\t"+
                   "1.Mostrar mi timelime\n"+"Que quieres hacer: "));

while(opcion != 7):
    if(opcion == 1):
        for status in tweepy.Cursor(api.user_timeline).items(10):
            print status.text+'\n'
        break;

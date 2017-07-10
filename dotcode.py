import tweepy

from tweepy import OAuthHandler

consumer_key = ' 5fB1XI3rJEvGbvWmJ1HK0ddhh'
consumer_secret = ' jsS3sZOW1PDg1KBdtffAVD6uC43hejX6v4Lc245p5RYbAFcaeT'
access_token = '1060794506-xoq3yDN6WY1OXrQqXTBTA7ZwjZ2s18dZ6MopxeF'
access_secret = 'QaUeRj9Zw1pUTURn3JMVXYfBTBb0hEBTir6ulEu97yzA4'

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
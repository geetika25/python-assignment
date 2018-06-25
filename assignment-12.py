#assignment-12

#Q.1- What is an access token? Generate your access token for any API.(for example Twitter,Spotify etc).


#An access token is generated by the logon service when a user logs on to the system and the credentials provided by the user are authenticated against the authentication database.
#The authentication database contains credential information required to construct the initial token for the logon session, including its user id, primary group id, all other groups it is part of, and other information.
#An access token is an object encapsulating the security identity of a process 

#how to create your access token for any API : 
# step 1.create Twitter Account : twitter provide an API through which we can create our application.
# step 2.go to website app.Twitter.common
#     (i)create new application
# step 3. Requirements :
	  # (i)consummer_key
	  # (ii)consummer_secrete
	  # (iii)access_token
	  # (iv)access_token_secrete
#step  4. Generate Access Token	  



#Q.2- Get the IP address of some common sites like Google, Facebook by using DNS lookup.


#the ip address of facebook.com by using DNS lookup.
# C:\Users\atc>nslookup facebook.com
# Server:  UnKnown
# Address:  192.168.43.1

# Non-authoritative answer:
# Name:    facebook.com
# Addresses:  2a03:2880:f12f:83:face:b00c:0:25de
          # 157.240.16.35

#the ip address of google by using DNS lookup.
# C:\Users\atc>nslookup google.com
# Server:  UnKnown
# Address:  192.168.43.1

# Non-authoritative answer:
# Name:    google.com
# Addresses:  2404:6800:4002:802::200e
          # 172.217.31.14		  
		  
		  
#Q.3- Using Tweepy library try to extract tweets from Twitter.


import tweepy
consumer_key=''#enter you consumer_key here.
consumer_secret=''#enter your consumer_secret here.
access_token=''#enter your access_token here.
access_token_secret='' #enter your access_token_secret here.
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)
tweets = api.search('#notwithoutmydog ',lang="en",count=5,tweet_mode='extended')
#print(tweets)
for tweet  in tweets:
 print("------------------")
 print(tweet.full_text)
 print("------------------")
 
 
#to take user input.
import tweepy
hash_tag=(input("Enter your hashtag here : "))
c=int(input("Enter number of counts  : "))
consumer_key=''#enter you consumer_key here.
consumer_secret=''#enter your consumer_secret here.
access_token=''#enter your access_token here.
access_token_secret='' #enter your access_token_secret here.
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)
tweets = api.search(hash_tag,lang="en",count=c,tweet_mode='extended')
#print(tweets)
for tweet  in tweets:
 print("------------------")
 print(tweet.full_text)
 print("------------------")
 
#Q.4- What is a difference between library and API. Figure it out with examples.


#A Library is a chunk of code that you can call from your own code, to help you do things more quickly/easily. For example, a Bitmap Processing library will provide facilities for loading and manipulating bitmap images, saving you having to write all that code for yourself.
#Typically a library will only offer one area of functionality (processing images or operating on zip files)

#example : numpy,scrapy

#An API (application programming interface) is a term meaning the functions/methods in a library that you can call to ask it to do things for you - the interface to the library

#example : when used in the context of web development.
# -*- coding:utf8 -*-
import tweepy,sys,re,urllib
filename=str(sys.argv[1])
CONSUMER_KEY=keys.keys["CONSUMER_KEY"]
CONSUMER_SECRET=keys.keys["CONSUMER_SECRET"]
ACCESS_KEY=keys.keys["ACCESS_KEY"]
ACCESS_SECRET=keys.keys["ACCESS_SECRET"]

list=["a.html","b.html","c.html","d.html","e.html","f.html","g.html"]
auth=tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
#put in your CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET 
api=tweepy.API(auth)
outputfile=open(filename,'a+')
tweets=api.user_timeline("TechCrunch")
newl='\n\n'
newk='***************\n'
leng=len(outputfile.read())
outputfile.seek(leng,0)
outputfile.write(newk)
for tweet,name in zip(tweets,list):
    try:
        outputfile.write(tweet.text)
        outputfile.write(newl)
        outputfile.write(newk)
        link=tweet.text
        lk=re.search("(https://t.co/\w+)",link)	
        mylink=lk.group()
        print mylink	
        #name="%s.html"%mylink[13:]
        print name
        f=urllib.urlopen(mylink)
        content=f.read()
        g=open(name,'w')
        g.write(content)
        g.close()		
    except UnicodeEncodeError:
        pass	
    
outputfile.close()
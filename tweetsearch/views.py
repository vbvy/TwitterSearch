from tweetsearch import app
from flask import render_template           #to return html file 
from tweepy import OAuthHandler             #helps in authentication for api usage
import tweepy                               
from flask import request                   


# after 
consumer_key = 'WdHrcTz9uiKoVVYmXpSnMNh1L'
consumer_secret = 'MGvLbf0CDUnRhZOjJvmNDGwJxj4q2hsqiLI6HN5CAMMzC4wxKL'
access_token = '94486385-Od0OLc6UmvnAxnR7A5BhSiA9nzDwVzPHKC6PQD85u'
access_token_secret = 'O9MV3M9OMBJAeHP2z5CeonjigBHue4PjafgLpcfLTKqZb'

# search count
count_limit=100



@app.route('/',methods=['POST','GET'])        #URL that appears on top, method by default is GET
def twitter_search():
    if request.method == 'POST':
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)                                         #tweepy API's instance to call search
        query_param = request.form['keyword']                          #requests from the template
        if query_param=='':
            return render_template('index.html')
        search_results = api.search(q=query_param, count=count_limit)  #if auth are right, call gets successful
        #print search_results
        
        search_text=[]
        for i in search_results:
            search_text.append(i.text)
        #print search_text
        
        return render_template('index.html',search_list=search_text)
    return render_template('index.html')

  
   

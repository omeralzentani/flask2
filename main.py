import matplotlib.pyplot as plt
import seaborn as sns
import pytrends
from pytrends.request import TrendReq
import pandas as pd

from io import StringIO

from googlesearch import search

import time
import datetime
import urllib.request
from datetime import datetime, date, time
from flask import Flask,render_template,request,make_response
import matplotlib.pyplot as plt
from bidi.algorithm import get_display
import bidi
import urllib.parse
import requests
import tkinter as tk
from bs4 import BeautifulSoup
import re
import os
from wordcloud import WordCloud
import arabic_reshaper
from bidi.algorithm import get_display
from tkinter import *
from tkinter import ttk
import tkinter as tk
from pandastable import Table
import pandas as pd
import time
import datetime
from datetime import datetime, date, time
from time import sleep
from collections import Counter
       
import pytrends
from pytrends.request import TrendReq
app = Flask(__name__,template_folder='html')
text1=[]
text=[]
links=[]
keywords2=[]
      
keywords=[]

@app.route("/",methods=['GET','POST'])
def home():
 
   
    if request.method=="POST" and request.form['search'] and request.form['page']:
        if request.form['submit_button'] == 'استخراج الكلمات المفتاحية':
            global p
            p=int(request.form['page'])
            global t
            t=0
            text.clear()
            keywords.clear()
            for i in text:
                i.remove()
            for i in keywords:
                i.remove()
            print(keywords)
            link=request.form['search']
            links.clear()

            for j in search(link, tld="co.in", num=10, stop=p , pause=2,lang='ar'):
                print(j)
                links.append(j)
            for i in links:
                try:
                    global page
                    page = requests.get(str(i))
                except:
                    print('no')
                soup = BeautifulSoup(page.content, 'html.parser')
                for l in soup.find_all("a"):
                    n=(l.text)
                    print(n)
                    letters_only_text = re.sub("[^a-zA-Zء-ي]", " ", n)
 
                    text.append(letters_only_text)
                for l in soup.find_all("p"):
                    n=(l.text)
                    letters_only_text = re.sub("[^a-zA-Zء-ي]", " ", n)

                    text.append(letters_only_text)
                    print(n)
                for l in soup.find_all("h1"):
                    n=(l.text)
                    letters_only_text = re.sub("[^a-zA-Zء-ي]", " ", n)

                    text.append(letters_only_text)
                    print(n)
                for l in soup.find_all("h2"):
                    n=(l.text)
                    letters_only_text = re.sub("[^a-zA-Zء-ي]", " ", n)

                    text.append(letters_only_text)
                    print(n)
                for l in soup.find_all("h3"):
                    n=(l.text)
                    print(n)
                    letters_only_text = re.sub("[^a-zA-Zء-ي]", " ", n)

                    text.append(letters_only_text)
                for l in soup.find_all("h4"):
                    n=(l.text)
                    print(n)
                    letters_only_text = re.sub("[^a-zA-Zء-ي]", " ", n)

                    text.append(letters_only_text)
                for l in soup.find_all("h5"):
                    n=(l.text)
                    print(n)
                    letters_only_text = re.sub("[^a-zA-Zء-ي]", " ", n)

                    text.append(letters_only_text)
            

            f = open("demofile2.txt", "r+")
            f.truncate(0)
            print(f)
            for i in text:
                f.write(i)
                
            f.close()
            f=open("demofile2.txt","r")
            k=(f.read())
            print(k)
            reg = re.compile('\S{4,}')
            global lenkeywords
            keywords2.clear()
            
            c = Counter(ma.group() for ma in reg.finditer(k))
            print (c)
          
            

            for i in c:
                if(c[i])>10:
                    keyword=(i,c[i])
                    keywords.append(i)
                    print(i)
            print(keywords)
            return render_template("seo.html",value=keywords)

            
            
            #kk=[keywords[p]]
        
            #pytrends = TrendReq(hl='ar')
            #pytrends.build_payload(kk
             #                        , cat=0, timeframe='today 5-y', geo='', gprop='')

            #df = pytrends.interest_by_region()
            #pd.set_option('display.max_rows', df.shape[0]+1)

            #print(df)
            #suggestions_dict = pytrends.suggestions(keyword=str(kk))
            #m=(pd.DataFrame(suggestions_dict).drop('mid', axis=1))
            #print(m)
           # related_=pytrends.related_topics()
            
           # related=pytrends.related_queries()
           # related_df=(pd.DataFrame(data=related))
           # kkk=(related_df.head(10))
           # print(kkk)
            #return render_template("seo.html",value=related_.to_html())
           # return render_template('seo.html',  tables=[kkk.to_html(classes='data')], titles=kkk.columns.values)
        
   #
    #        print(related_)
        #print(related)
        elif request.form['submit_button'] == 'extract':
            try:
                keywords2len=len(keywords2)
                if keywords2len>2:
                    keywords2.clear()
                    key2.clear()
               
                print(keywords2)
                print((request.form['w3review']))
                global key1
                key1= (request.form['w3review'])
                key2=key1.split(',')
                

                print(type(key2))
                for i in key2:
                    keywords2.append(i)
                    print(i)
               
                
                return render_template("seo.html",values=".")
            except:
                return render_template("seo.html",values="يرجى استخراج الكلمات المفتاحية")

                
            
        elif request.form['submit_button'] == 'الكلمة التالية':
            try:
            
                t+=1
 
            
                kk=[keywords2[t]]
            
                pytrends = TrendReq(hl='ar')
                pytrends.build_payload(kk
                                     , cat=0, timeframe='today 5-y', geo='', gprop='')

                df = pytrends.interest_by_region()
                pd.set_option('display.max_rows', df.shape[0]+1)

                #print(df)
            #suggestions_dict = pytrends.suggestions(kk)
                related_=pytrends.related_topics()
                data=pytrends.related_queries()
                #global related_df 
                related_df=(pd.DataFrame(data=data))
                #print(pd.DataFrame(related_df).drop('mid', axis=1))
                
                global kkk
                kkk=(related_df)

                print(kkk)
                

                return render_template('seo.html',  tables=[kkk.to_html(classes='data')], titles=kkk.columns.values)
            except:
                return render_template("seo.html",values="لاتوجد نتائج")
             
        elif request.form['submit_button'] == 'رجوع':
            try:
            
                t-=1
 
            
                kk=keywords2[t]
            
                pytrends = TrendReq(hl='ar')
                pytrends.build_payload(kk
                                     , cat=0, timeframe='today 5-y', geo='', gprop='')

                df = pytrends.interest_by_region()
                pd.set_option('display.max_rows', df.shape[0]+1)

                #print(df)
            #suggestions_dict = pytrends.suggestions(kk)
                related_=pytrends.related_topics()
                data=pytrends.related_queries()
                #global related_df 
                related_df=(pd.DataFrame(data=data))
                #print(pd.DataFrame(related_df).drop('mid', axis=1))
                
                global jjj
                jjj=(related_df)

                print(jjj)
                

                return render_template('seo.html',  tables=[jjj.to_html(classes='data')], titles=jjj.columns.values)
            except:
                return render_template("seo.html",values="لاتوجد نتائج")
             
        elif request.form['submit_button'] == 'اقتراحات':
            try:
            
            
                
                t=t
            
                kk=[keywords2[t]]
            
                pytrends = TrendReq(hl='ar')
                pytrends.build_payload(kk
                                     , cat=0, timeframe='today 5-y', geo='', gprop='')

                df = pytrends.interest_by_region()
                pd.set_option('display.max_rows', df.shape[0]+1)

                #print(df)
            #suggestions_dict = pytrends.suggestions(kk)
                related_=pytrends.related_topics()
                data=pytrends.related_queries()
                #global related_df 
                related_df=(pd.DataFrame(data=data))
            #print(pd.DataFrame(related_df).drop('mid', axis=1))
                
                global ttt
                ttt=(related_df)

                print(ttt)
                

                return render_template('seo.html',  tables=[ttt.to_html(classes='data')], titles=ttt.columns.values)
            except:
                return render_template("seo.html",values="لاتوجد نتائج")
            
        elif request.form['submit_button'] == 'تحميل':
            try:
            
                data = {
                "calories": [420, 380, 390],
                "duration": [50, 40, 45]
                  }

            #load data into a DataFrame object:
                df = pd.DataFrame(data)
            
                resp = make_response(related_df.to_csv())
                resp.headers["Content-Disposition"] = "attachment; filename=export.csv"
                resp.headers["Content-Type"] = "text/csv"
                return resp
            except:
                return render_template("seo.html",values="لاتوجد بيانات")

    return render_template("seo.html")
    







        #   k="besmeaalah"
        
        #return render_template("seo.html",values=related.to_html())





       





    
    

        #k=(n.read())
        

        #reshaped_text = arabic_reshaper.reshape(n)
        #text_text = bidi.algorithm.get_display(reshaped_text )

        #wordcloud = WordCloud().generate(text_text)
        #wordcloud.to_file("word2.png")
          
       
           
    
      
                
if __name__ == "__main__":
    app.run()











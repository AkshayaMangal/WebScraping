""" Smoothies with incredients such as Turmeric,Pumpkin seeds,Cherries,Blueberries,Chamomile,Dark Chocolate,Green Tea (Matcha),Natural Lavender Extract 
There are certain foods that may help ease anxiety and can be beneficial for promoting healthy brain function."""

import requests
from bs4 import BeautifulSoup
import csv


r=requests.get("https://vibranthappyhealthy.com/smoothie-recipes-for-anxiety/").text
soup=BeautifulSoup(r,'lxml') 

csv_file=open ("Smoothie.csv","w")
csv_writer=csv.writer(csv_file)
csv_writer.writerow(["Smoothie","Incredients","How to prepare"])

Headline=soup.find("h1",class_="entry-title fn")
print(Headline.text)                                    #11 Smoothie Recipes for Anxiety
                                      
l1=[]
c=3
p=0
l1=[50,57,64,72,79,85,92,97,102,107,112]                    #list with all the paragraphs index with "how to prepare"
l2=[]
l3=[]
l4=[]
for i in l1:
    l2.append((soup.find_all("p")[i].text))                 #list with all the paragraphs text with "how to prepare"



for name in soup.find_all("h3"):            
        
    print(name.text)  
    smoothie_name=name.text                                               #All smoothie names
    print(soup.find_all("strong")[17].text)                                 #Repeating "what you'll need"                         
    article=soup.find_all("ul")
    print(article[c].text)
    incredients1=article[c].text 
    l3.append([article[c].text])
    
    for i in l3:
        incredients=i
        print(incredients)
        for j in incredients:
            l4.append(j.replace("\n",""))
            print(l4)
            for k in l4:
                ind=k+"\t"
            l4=[]
        
    l3=[]
                                              #printing all the incredient list
    c=c+1
    if c==14:
        break
    print(soup.find_all("strong")[16].text)                     #printing all the "How to prepare"                                                              
    print(l2[p])
    How_to_prepare=l2[p]
    p=p+1
    print(" ")
    csv_writer.writerow([smoothie_name,ind,How_to_prepare])
csv_file.close()
   
   
  
    
   
   
   
    
       
       
          
        

    
    
    
    
    



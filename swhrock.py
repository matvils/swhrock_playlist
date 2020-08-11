from bs4 import BeautifulSoup
import dryscrape
import time
from datetime import datetime
import sys, os

session = dryscrape.Session()
page_link = 'https://radioswhrock.lv/pedejas-50-dziesmas/'
text_old = ""
text=""
z=0
while z==0 :
    try:
        session.visit(page_link)
        response = session.body()
        bs = BeautifulSoup(response, features="lxml")
        mydivs = bs.find(class_="current-playing")
        text = mydivs.get_text()
    except:
        next
    print("  ******************************  ")
    if text != text_old:
        laiks = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        today = datetime.today().strftime('%d-%m-%Y')
        filepath = 'swh_rock_list.txt' 
        item =  str(laiks)+ " * "+ text
        with open(filepath, 'a') as f:
            f.write("%s\n" % item)
        print(item)
    text_old = text
    time.sleep(60)

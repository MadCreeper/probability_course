# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36

# -*-coding:utf-8-*-
import re
import urllib.parse
import urllib.request
from http import cookiejar
from bs4 import BeautifulSoup
from urllib.request import urlopen
import json
import ssl  
import csv
import datetime
ssl._create_default_https_context = ssl._create_unverified_context    #不加这个会报错(SSL)

cookie = cookiejar.CookieJar()
cookie_handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(cookie_handler)
opener.addheaders = [("User-Agent", "Term Project, PLEASE DON'T BAN ME, THANKYOU! Send message to 13918719254 if needed! Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, \
                       like Gecko) Chrome/58.0.3029.110Safari/537.36")]

info_url = "https://canteen.sjtu.edu.cn/CARD/Ajax/Place/"

def crawl():
    response = opener.open(info_url).read()
    soup = BeautifulSoup(response,features="html.parser")
    #print(soup)
    json_str = soup.text
    data_dict = json.loads(json_str)
    canteen_empty_seats = []
    names = []
    for canteen in data_dict:
        canteen_empty_seats.append(str(canteen['Seat_u']))
        names.append(canteen['Name'])

    print(','.join(canteen_empty_seats))
    #print(','.join(names))
    try:
        with open('data.csv', 'a', newline='') as f_object:  
            # Pass the CSV  file object to the writer() function
            writer_object = csv.writer(f_object)
            # Result - a writer object
            # Pass the data in the list as an argument into the writerow() function
            curdate = str(datetime.datetime.now().month) + '.' + str(datetime.datetime.now().day)
            curtime = str(datetime.datetime.now().hour) + ':' + str(datetime.datetime.now().minute)
            dtlist = [curdate, curtime]
            writer_object.writerow(dtlist + canteen_empty_seats)  
            # Close the file object
            f_object.close()
    except Exception as E:
        print(E)
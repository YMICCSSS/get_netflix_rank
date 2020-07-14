from selenium import webdriver
from time import sleep
import requests
import datetime
from bs4 import BeautifulSoup as b4
get = datetime.datetime.now()

mon_dic={1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",
         7:"July",8:"August",9:"September",10:"October",11:"November",
         12:"December"}

month = mon_dic.get(get.month,"")
month_int = get.month
day = get.day

# driver_path = r"C:\geckodriver\geckodriver.exe"
# driver = webdriver.Firefox(executable_path=driver_path)
get_movie=requests.get(f"http://ddm.com.tw/blog/post/netflix-daily-top10-{month}-2020#2020年{month_int}月{day}日")
get_movie =b4(get_movie.text,"lxml")

search_field = get_movie.find("div",class_="Zi_ad_ar_iR")
drama_name = search_field.find_all("li")
print(f"2020-{month_int}-{day} Netflex 前十名 ")
print("")
for i in range(3,13):
    print(drama_name[i].text)

get_today = f"2020-{month_int}-{day} Netflex 前十名 "
first = drama_name[3].text
second = drama_name[4].text
third = drama_name[5].text
four = drama_name[6].text
five = drama_name[7].text
six = drama_name[7].text
seventh = drama_name[9].text
eight = drama_name[10].text
nine = drama_name[11].text
ten = drama_name[12].text



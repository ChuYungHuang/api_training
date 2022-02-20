# 從 Dad jokes 網站爬取笑話，並可以讓使用者指定『關鍵字』，將相關資料收集下來，儲存到一個 txt 檔中。

# Packages
import requests
import json
import random
import time

def search_time():
    t = time.localtime()
    search_time = time.strftime("%Y/%m/%d %H:%M:%S", t)
    return search_time

url = "https://icanhazdadjoke.com/search"
search = input("Search:")
response = requests.get(url,headers={"Accept":"application/json"},params={"term":f"{search}"})
response_text = json.loads(response.text)
results = response_text["results"]
total_jokes = response_text["total_jokes"]

with open("jokes.txt","a") as txt:
    if results != []:
        joke = random.choice(results)["joke"]
        print(search_time())
        print(f"Total jokes:{total_jokes}")
        print(f"One of [{search}]'s joke:\n{joke}")
        txt.write(f"{search_time()}\n")
        txt.write(f"Total jokes:{total_jokes}\n")
        txt.write(f"One of [{search}]'s joke:\n{joke}\n")
    else:
        print(search_time())
        print(f"No [{search}]'s joke here!")
        txt.write(f"{search_time()}\n")
        txt.write(f"No [{search}]'s joke here!\n")
# 從 Dad jokes 網站爬取笑話，並可以讓使用者指定『關鍵字』，將相關資料收集下來，儲存到一個 txt 檔中。

# Packages
import requests
import json
import random

url = "https://icanhazdadjoke.com/search"
search = input("Search:")
response = requests.get(url,headers={"Accept":"application/json"},params={"term":f"{search}"})
response_text = json.loads(response.text)
results = response_text["results"]
total_jokes = response_text["total_jokes"]

if results != []:
    joke = random.choice(results)["joke"]
    print(f"Total jokes:{total_jokes}")
    print(f"One of them:\n{joke}")
    with open("jokes.txt","a") as txt:
        txt.write(f"Total jokes:{total_jokes}\n")
        txt.write(f"One of them:\n{joke}\n")
else:
    print("No joke here")
    with open("jokes.txt","a") as txt:
        txt.write(f"Search[{search}]:No joke here\n")

import requests
import json

def main():
    while True:
        url = "http://localhost:1400"
        getItem = input("Enter the topic you would like to learn more about: ")
        itemDict = {'item': str(getItem)}
        postItem = requests.post(url,data=itemDict)
        postRes = postItem.json()
        print(str(postRes))
        #itemStr = postItem.text

main()
    
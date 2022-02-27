import requests
import json

def main():
    getItem = input("Enter the topic you would like to learn more about, enter exit to quit: ")
    while (getItem != ("exit" or "Exit")):
        if (getItem == ("exit" or "Exit")):
            break
        url = "http://localhost:1400"
        itemDict = {'item': str(getItem)}
        postItem = requests.post(url,data=itemDict)
        postRes = postItem.json()
        print(str(postRes))
        print("-------------------------------------")
        getItem = input("Enter the topic you would like to learn more about, enter exit to quit: ")
        #itemStr = postItem.text

main()
    
import requests
import json
from difflib import get_close_matches

title = []
description = []
contributer = []
price = []
author = []
isbns = []
Script_Switch = True


key = "XXX"
url = requests.get(
    f'https://api.nytimes.com/svc/books/v3/lists/best-sellers/history.json?api-key={key}'
)

NYTS_API_JSON_FILE = json.loads(url.text)
for index in NYTS_API_JSON_FILE["results"]:
    title.append(index["title"][1:].upper())
    description.append(index["description"])
    contributer.append(index["contributor"])
    author.append(index['author'].upper())
    price.append(index['price'])
    isbns.append(index["isbns"])

print(
    "Please pick an option for your search of the NYT's most recent Best Sellers List. \n The more characters you put in for your querey (< 5) the better the result!"
)

while Script_Switch:
    try:
        print("1. Search with Title ")
        print("2. Search with ISBN")
        print("3. Search with Author")
        print("4. Quit")
        option = int(input(">>>"))
        if option == 1:
            search = input("Enter title: ").upper()
            print("[INFO] Searching ...")
            optimized_search = get_close_matches(search, title)
            if optimized_search != []:
                location = title.index(optimized_search[1])
                print(
                    "===RESULT==="
                )
                print(f"""
                    Title: {title[location]}
                    Description: {description[location]}
                    Contributor: {contributer[location]}
                    price: {price[location]}
                    author: {author[location]}
                    isbns: {isbns[location]}
                """)
            else:
                print("OOPS! Entered Query is not matched \n")
        elif option == 2:
            search = input("Enter ISBN: ")
            print("[INFO] Searching ...")
            optimized_search = get_close_matches(search, isbns)
            if optimized_search != []:
                location = isbns.index(optimized_search[0])
                print(
                    "===RESULT==="
                )
                print(f"""
                    Title: {title[location]}
                    Description: {description[location]}
                    Contributor: {contributer[location]}
                    price: {price[location]}
                    author: {author[location]}
                    isbns: {isbns[location]}
                """)
            else:
                print("OOPS! Entered Query is not matched \n")
        elif option == 3:
            search = input("Enter author's name: ").upper()
            print("[INFO] Searching ...")
            optimized_search = get_close_matches(search, author)
            if optimized_search != []:
                location = author.index(optimized_search[0])
                print(
                    "===RESULT==="
                )
                print(f"""
                    Title: {title[location]}
                    Description: {description[location]}
                    Contributor: {contributer[location]}
                    price: {price[location]}
                    author: {author[location]}
                    isbns: {isbns[location]}
                """)
            else:
                print("OOPS! Entered Query is not matched \n")
        elif option == 4:
          print("End of application! ")
          Script_Switch = False
        else:
            print("Hmm! Not a valid option try agian :) \n")
    except Exception as e:
        print("[ERROR] OOPS! something went wrong, try again! \n")

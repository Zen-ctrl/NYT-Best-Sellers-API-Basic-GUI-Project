## NYT Best Sellers Optimized Searcher BETA
Using the Best Sellers API from The New York Times,  my application (which is in BETA) looks through the main NYT's API for the best sellers of this month and gives a result based on the user's input of either a book's title, ISBN, or author. When the user gives a close enough query (5 characters or more),  the book, (if it is a best seller for the current month the user is in), is fetched along with the book's title, description, contribute, price, author, and finally ISBN numbers. 




---

## Packages

The following are packages I used for this BETA application:

- [Import Requests](https://docs.python.org/3/library/urllib.request.html?highlight=requests) 
	- I use this package to help me do a URL request for The New York Times API
- [Import json](https://docs.python.org/3/library/json.html?highlight=json)
	- I use this package to help me load the .json directly from The New York Times API
- [Difflib --> get_close_matches](https://docs.python.org/3/library/difflib.html?highlight=get_close_matches)
	- I use the Difflib package to help me import the algorithmic searcher get_close_matches. This will help with using an optimized searcher and it will also condense the amount of code I would have to write.
- Extra packages
	- From the GUI aspect of this project (which is incomplete but I still thought it would be nice to mention).....
		- [I used the tkinter package](https://docs.python.org/3/library/tkinter.html): to help create a crude application interface for my script. It made a search box with it along with a button you can click to initiate your search query. 
		- [I also imported multiprocessing threading.](https://docs.python.org/3/library/multiprocessing.html?highlight=multiprocessing#module-multiprocessing) When I was watching a tutorial on tkinter, it was mentioned that for opening images or anything graphically related, Importing multiprocessing can optimize the GUI for the device it is run on. This would help speed up the application by using different paths running in parallel on the computer.  

---

## Intro block
In the non-GUI version of my code, I start out by importing the following packages/libraries. These are: requests, json, and difflib's get_close_matches.
These packages are very essential to the working of the code as they respectively serve the following purposes: allowing for URL requests, allowing for utilization of the .json file, searching for close keywords via algorithmic matching.  
```python
import requests
# 
import json
# allowing for utilization of the .json
from difflib import get_close_matches
# searching for close keywords via algorithmic matching
```
I continue my code by creating empty lists for the information that I am hoping to return to the user via terminal with appended information snatched from The New York Times Best Seller API.  These are the lists I created:

```python
title = []

description = []

contributer = []

price = []

author = []

isbns = []
```
Next, for PEP-8 optimization, I attempted to save line space by creating a variable named "key" which would store The New York Time's Developer API key that would allow me to gain access to the Best Sellers API directory. I also create a variable called "url" and set it to the requests function (using the request package) of the URI for The New York Time's Best Seller API.

```python
key = "XXXX"
url = requests.get(f'https://api.nytimes.com/svc/books/v3/lists/best-sellers/history.json?api-key={key}')
```


## What I Would do Next


## Your full python script



```python
import requests
import json
from difflib import get_close_matches

title = []
description = []
contributer = []
price = []
author = []
isbns = []


key = "YOU KEY GOES HERE!!!!"
url = requests.get(
    f'https://api.nytimes.com/svc/books/v3/lists/best-sellers/history.json?api-key={key}'
)

text = json.loads(url.text)
for index in text["results"]:
    title.append(index["title"][1:].upper())
    description.append(index["description"])
    contributer.append(index["contributor"])
    author.append(index['author'].upper())
    price.append(index['price'])
    isbns.append(index["isbns"])

print(
    "Please pick an option for your search of the NYT's most recent Best Sellers List. \n The more characters you put in for your querey (< 5) the better the result!"
)

while True:
    try:
        print("1. Search with Title ")
        print("2. Search with ISBN")
        print("3. Search with Author")
        print("4. Quit")
        opt = int(input(">>>"))
        if opt == 1:
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
        elif opt == 2:
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
        elif opt == 3:
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
        elif opt == 4:
            print("End of application! ")
            flag = False
        else:
            print("Hmm! Not a valid option try agian :) \n")
    except Exception as e:
        print("[ERROR] OOPS! something went wrong, try again! \n")

```


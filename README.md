# HacKSU_Reddit_Scraper
A lesson using Python to search through a json object and find posts based on a keyword or a specified subreddit.

*Written by Joshua Behler*

## Intro
Reddit is a social media platform where users can post to various "Subreddits", each with a unique topic. Reddit allows users to download their webpages in an organized fashion in order to gather data. Today, we will be making a Python Program that does just this. For this lesson, you will need Python 3.8 installed. You can download Python from [here](https://python.org)
## Setting up Python
In order to create your bot, you will need to install the requests module. To do so, follow these steps:

1: Open up your computer's terminal. For Windows, this is Command Prompt/Powershell. For Mac and Linux, this is Linux.

2: Execute the following command:
```
pip install requests
```
If all works, the requests module should install and become available for use.
## Coding
Now we will code the bot. Open your preferred IDE (IDLE is preferred for this tutorial). Add the line ```import requests``` to the top of your file. This will allow us to use the module we just installed.

Next, we're gonna create the function that will do all the heavy work. Add ```def scan(word,sub):```. This creates a function named scan that takes two parameters. 

Next, we're gonna declare the url we are going to be scanning, using the sub parameter we passed over. We will construct it like this:
```url = "https://reddit.com/r/"+sub+"/new/.json"```
Notice the `/.json` at the end. This line converts the webpage into a JSON object, which we can easily step through. Try this yourself: go to any page on Reddit and add `/.json` to the end. You'll get a page with a bunch of plain text.

Next, we're gonna actually do the downloading. Add the line:
```response = requests.get(url,headers = {'User-agent':'Scanner'})```
This tells Reddit that you are a User-agent named Scanner and want to download the page. You can change "Scanner" to be anything you want. Sometimes, Reddit may deny your request, we we should write a handler that catches that. Add
```
if(not response.ok):
    print("Error:",response.status_code)
    return
```
This will print an error message if we encounter an error while requesting.

Next up, we want to convert all that data into a Python dictionary. This will let us traverse through the data and locate our specified key-phrase. Add
```data = response.json().get('data')['children']```
This line takes our downloaded result, and then extracts the data and children sub-dictionaries from it. The 'children' dictionary is the one that contains all the Reddit posts.

Next up, we're gonna add our for loop. The for loop will travel through the children, checking the title and body for our key-phrase. The second it finds it, we print the information, and then return.
```
for x in data:
    if(word in x['data']['selftext'] or word in x['data']['title']):
        print("Found",word)
        print("Sub:",x['data']['subreddit'])
        print("Title:",x['data']['title'])
        print(x['data']['selftext'])
        print()
        return
print("Couldn't find",word)
```
This will be what ends our function. x is each individual post that we loop through, 'data' is the name of the sub-dicitionary that contains the information about each post, and then each subsequent word is a keyword mapping to the data.

Lastly, we want to call our function over and over, so we implement an infinite loop that waits for user input to call the function.
```
while(True):
    scan(input("Enter a word or phrase: "),input("Enter a subreddit to scan: "))
```

If you have done everything correctly, your file should look like this:
```
import requests

def scan(word,sub):
    url = "https://reddit.com/r/"+sub+"/new/.json"
    response = requests.get(url,headers = {'User-agent':'Scanner'})
    if(not response.ok):
        print("Error:",response.status_code)
        return

    data = response.json().get('data')['children']
    for x in data:
        if(word in x['data']['selftext'] or word in x['data']['title']):
            print("Found",word)
            print("Sub:",x['data']['subreddit'])
            print("Title:",x['data']['title'])
            print(x['data']['selftext'])
            print()
            return
    print("Couldn't find",word)

while(True):
    scan(input("Enter a word or phrase: "),input("Enter a subreddit to scan: "))
```

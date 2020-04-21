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

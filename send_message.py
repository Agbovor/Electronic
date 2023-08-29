import requests


eventName = "send email"
api_key = "kuonrPeTJC06djmqQ410mXu_ZZ7uMwBpx4Eg2F3chd3"

#create url
url = (f"https://maker.ifttt.com/trigger/{eventName}/json/with/key/kuonrPeTJC06djmqQ410mXu_ZZ7uMwBpx4Eg2F3chd3")

jsonData = {
"Name": "Alex",
"Age": "22"
}

response = requests.post(url, jsonData)

print(response.text)
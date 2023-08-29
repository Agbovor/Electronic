import requests
class IFTTT_NOTIFICATION:
    def __init__(self, eventName, api_key, jsonData = None):
        self.eventName = eventName
        self.api_key = api_key
        self.jsonData = jsonData

    def make_request(self):
        url = f"https://maker.ifttt.com/trigger/{self.eventName}/json/with/key/{self.api_key}"

        try:
            print("sending...")
            response = requests.post(url, self.jsonData)
            print(response)
            print(response.text)
            print("sent sucessfully")
        except Exception as e:
            print("run into an error", e)
# def send_message():


#     eventName = "send email"
#     api_key = "kuonrPeTJC06djmqQ410mXu_ZZ7uMwBpx4Eg2F3chd3"

#     #create url
#     url = (f"https://maker.ifttt.com/trigger/{eventName}/json/with/key/kuonrPeTJC06djmqQ410mXu_ZZ7uMwBpx4Eg2F3chd3")

#     jsonData = {
#     "Name": "Alex",
#     "Age": "22"
#     }
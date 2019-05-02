import json
import sys
import requests

# Question 7
response = requests.get("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=PewDiePie&key=AIzaSyCKNriJu8UlckJbLSuhZS1iZ5CoIuKSQSg")
pewds = json.loads(response.content)
pewdSubs = pewds['items'][0]['statistics']['subscriberCount']
response = requests.get("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=tseries&key=AIzaSyCKNriJu8UlckJbLSuhZS1iZ5CoIuKSQSg")
tseries = json.loads(response.content)
tSubs = tseries['items'][0]['statistics']['subscriberCount']
diff = int(pewdSubs) - int(tSubs)
print("PewDiePie has", pewdSubs, "subscribers and T-Series has", tSubs, "subscribers.\nThe difference between them is", diff)

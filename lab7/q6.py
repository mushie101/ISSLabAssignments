# Question 6
import requests
import json

# For Invoker
response = requests.get("https://api.opendota.com/api/players/431931403/wl?hero_id=74&significant=0")
obj = json.loads(response.content)

def getWp (obj):
    matches = int(obj['win']) + int(obj['lose'])
    try:
        wlperc = (int(obj['win']) / matches)
    except:
        wlperc = -1
    return wlperc, matches

wp, m = getWp (obj)
if wp == -1:
    print("No games have been played with this hero\n\n")
else:
    print("Win-loss percentage is", wp, "\n\n")


# For heroes with hero ID upto lim
hp = 0
hero = 1
lim = 10
for i in range(1, lim+1):
    response = requests.get("https://api.opendota.com/api/players/431931403/wl?significant=0&hero_id=" + str(i))
    obj = json.loads(response.content)
    print(str(i) + ": ", obj)
    wp, ms = getWp (obj)
    if ms >= 6:
        if wp > hp:
            hp = wp
            hero = i

response = requests.get("https://raw.githubusercontent.com/kronusme/dota2-api/master/data/heroes.json")
heroes = json.loads(response.content)
print("\nThe hero with highest win percenetage is " + heroes['heroes'][hero-1]['localized_name'] + " with a win percentage of " + str(hp*100) + "%")
print("This data is for heroes with hero ID upto", lim)


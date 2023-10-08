import requests, json

url = "https://discord.com/api/v9/hypesquad/online"
token = input("Your discord token: ")
print("HOUSE IDS:\n1. Bravery\n2. Brilliance\n3. Balance")
idh = int(input("\nHouse id?: "))
haeders = {
    "authorization": token,
    "content-type": "application/json",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9018 Chrome/108.0.5359.215 Electron/22.3.24 Safari/537.36",
    "cookies": "__dcfduid=bdb3cc005b1211eead16c3ae1ce56d77; __sdcfduid=bdb3cc015b1211eead16c3ae1ce56d776711b5ea99567fb5e557fdcd9875bb20d9d112519ec1d7893539743950511e48; __stripe_mid=dd9d396f-fbee-4918-acf1-da8abda5d632c27c6e; cf_clearance=rGqHaIue6HSRiJBj2yvFjx0kKqOODg8Uxu8.ednsDro-1696192964-0-1-b33c2c17.986e76e0.eb5003b3-0.2.1696192964; __cfruid=1a1d7103705521e98aad89a5b9063cd445f2483d-1696347659; _cfuvid=2mky0Jry4P1LHYEOJLnOo4LH6EoHKUDtztifkLdmaxE-1696347659777-0-604800000; __stripe_sid=4d63638d-30dd-42ad-afe7-943478fe4b1550b324"
}
a = {
    "house_id": idh
}
req = requests.post(url=url, headers=haeders, json=a)
house_ids = {1: "Bravery", 2:"Brilliance", 3:"Balance"}
s = house_ids[idh]
if req.status_code == 204:
    print(f"You got house id: {s}")
else:
    print("Error")
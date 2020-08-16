import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("XXXXXXX", 
    "XXXXXX")
auth.set_access_token("XXXXXXXXXXX", 
    "XXXXXXXX")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

def bubble_list(user):
    followed_list = api.friends_ids(id=user)
    lists_list = [followed_list[x:x+99] for x in range(0, len(followed_list), 99)]
    dmc_list = api.create_list(name=user  + "'s Timeline", mode="private", description="See through {}'s Filter Bubble".format(user))
    for users in lists_list:
        try:
            add = api.add_list_members(users, list_id=dmc_list.id)
            print(add)
        except Exception as e: print(e)

print("Enter a username to generate a duplicate of his timeline")
user = input()
bubble_list(user)
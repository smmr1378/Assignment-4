import instaloader
import getpass

f = open("followrs.txt", "r")
old_followers = []
for line in f:
    old_followers.append(line)
f.close()

L = instaloader.Instaloader()
username = input("Enter username: ")
password = getpass.getpass("Enter password: ")
L.login(username, password)
print("hooora!!! successfully login" )
profile = instaloader.Profile.from_username(L.context, "ali")

new_followers = []
for follower in profile.get_followers():
    new_followers.append(follower)

for old_follower in old_followers:
    if old_follower not in new_followers:
        print(old_follower)


    f = open("followrs.txt", "w")
    for follower in new_followers:
        f.write(follower + "\n")
f.close()



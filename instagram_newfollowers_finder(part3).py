import instaloader
import getpass

f = open("followrs.txt", "r")
old_list = []
for line in f:
    old_list.append(line)
f.close()

L = instaloader.Instaloader()
username = input("Enter username: ")
password = getpass.getpass("Enter password: ")
L.login(username, password)
print("hooora!!! successfully login" )
profile = instaloader.Profile.from_username(L.context, "ali")

new_list = []
for follower in profile.get_followers():
    new_list.append(follower)
new_followers = []
for old_follower in old_list:
    if follower  not in  old_follower:
        new_followers.append(follower)
        print(new_followers)


    f = open("followrs.txt", "w")
    for follower in new_followers:
        f.write(follower + "\n")
f.close()



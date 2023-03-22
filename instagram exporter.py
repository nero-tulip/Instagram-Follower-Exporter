import instaloader
import csv
from tqdm import tqdm
import os
import urllib.request
import time

# Define the proxy address and port
proxy_address = '65.20.224.102:80'

# Create an opener that uses the proxy
proxy_handler = urllib.request.ProxyHandler({'http': proxy_address})
opener = urllib.request.build_opener(proxy_handler)

# Install the opener as the default opener for all requests
urllib.request.install_opener(opener)

# Create an Instaloader instance and log in to Instagram
bot = instaloader.Instaloader()
username = 'USERNAME'
password = 'PASSWORD'
bot.context.login(username, password)

# Get the profile of the user whose followers you want to scrape
profile = instaloader.Profile.from_username(bot.context, 'goodgoodwestend')

# Create a list to store the data
data = [["Username", "Followers", "Followees", "Profile Link"]]

# Iterate through all the followers of 'funkyfoodau'
for follower in tqdm(profile.get_followers(), desc="Scraping followers"):
    # Get the follower's profile information
    username = follower.username
    followers = follower.followers
    followees = follower.followees
    profile_link = "https://www.instagram.com/" + username
    
    # Add the profile information to the data list
    data.append([username, followers, followees, profile_link])

    time.sleep(20)

# Write the data to a CSV file
with open('/Users/USERNAME/Documents/Instagram Export/follower_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Username", "Followers", "Followees", "Profile Link"])
    writer.writerows(data[1:])

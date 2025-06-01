import requests

user_id = 000000000  # Replace with your target user ID
cursor = ""
follower_ids = []

while True:
    url = f"https://friends.roblox.com/v1/users/{user_id}/followers?limit=100&cursor={cursor}"
    response = requests.get(url)
    data = response.json()

    for user in data["data"]:
        follower_ids.append(str(user["id"]))
        print(f"Scrapped {user["id"]}")


        with open("followers.txt", "w") as f:
            f.write("\n".join(follower_ids))

    cursor = data.get("nextPageCursor")
    if not cursor:
        break

    
print(f"Saved {len(follower_ids)} follower IDs to followers.txt")

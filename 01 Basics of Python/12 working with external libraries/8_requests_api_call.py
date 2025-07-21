import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

if response.status_code == 200:
    data = response.json()
    print("Title:", data["title"])
else:
    print("Request failed with status:", response.status_code)


# This code fetches a random user from the FreeAPI and prints the username and country.
def fatch_random_user_freeapi():
    response = requests.get('https://api.freeapi.app/api/v1/public/randomusers/user/random')
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return username, country
    else:
        raise Exception("failed to fetch data")


def main():
    try:
        username, country = fatch_random_user_freeapi()
        print("username: ", username)
        print("country:", country)
    except Exception as e:
        print(f"fatch random user api error", {str(e)})

if __name__ == '__main__':
    main()



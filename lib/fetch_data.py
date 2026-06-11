import requests

def fetch_data():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

    if response.status_code == 200:
        return response.json()

    return {}

def save_to_file(data):
    with open("api_output.txt", "w") as file:
        file.write(f"Title: {data.get('title', 'No title')}\n")
        file.write(f"Body: {data.get('body', 'No body')}\n")

if __name__ == "__main__":
    post = fetch_data()
    save_to_file(post)
    print("Data fetched and saved to api_output.txt")
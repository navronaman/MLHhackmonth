import requests
import taipy as tp
from dotenv import load_dotenv
import os

load_dotenv()

# You can use your API_KEY from "https://api-ninjas.com/profile"
API_KEY = os.getenv("API_KEY")
print(API_KEY)

query = ""

def get_api_response(query, api_key=API_KEY):
    api_url = f'https://api.api-ninjas.com/v1/nutrition?query={query}'
    
    headers = {
	"X-RapidAPI-Key": f"{API_KEY}",
	"X-RapidAPI-Host": "nutrition-by-api-ninjas.p.rapidapi.com"
    }

    response = requests.get(api_url, headers={'X-Api-Key': f'{api_key}'})
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        return None
        print("Error:", response.status_code, response.text)
            
    
    

if __name__ == "__main__":
    
    query = input("Enter food item: ")
    
    print(get_api_response(query))
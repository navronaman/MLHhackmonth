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
        print("Error:", response.status_code, response.text)
        return None
        
def get_names_of_meal(json_file):
    
    try:
        names = []
        for item in json_file:
            names.append(item["name"].title())
            
        return names
            
    except Exception as e:
        print(f"Error: {e}")
        return None
            
def get_total_info(json_file):
    """
    Returns (1) total calories,
    (2) total fat, [in grams]
    (3) total protein, [in grams]
    (4) total sugar,
    (5) total fibre,
    (6) total carbs
    """
    
    total_dict = {
        "calories": 0.0,
        "fat": 0.0,
        "protein": 0.0,
        "sugar" : 0.0,
        "fiber": 0.0,
        "carbs": 0.0
    }
    
    for item in json_file:
        total_dict["calories"] += item["calories"]
        total_dict["fat"] += item["fat_total_g"]
        total_dict["protein"] += item["protein_g"]
        total_dict["sugar"] += item["sugar_g"]
        total_dict["fiber"] += item["fiber_g"]
        total_dict["carbs"] += item["carbohydrates_total_g"]
        
    total_dict = {k: round(v, 1) for k, v in total_dict.items()}
    
    return total_dict
    
            
    
    

if __name__ == "__main__":
    
    query = input("Enter food item: ")
    
    json_file = get_api_response(query)
    print(json_file)
    print(get_names_of_meal(json_file=json_file))
    print(get_total_info(json_file=json_file))
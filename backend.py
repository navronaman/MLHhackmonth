import requests
from dotenv import load_dotenv
import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(BASEDIR, '.env'))

# You can use your API_KEY from "https://api-ninjas.com/profile"
API_KEY = os.getenv("OG_API_KEY")
print(API_KEY)

query = ""

def get_api_response(query, api_key=API_KEY):
    
    print("\n I'm at API response")
    
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
    
    print("\n I'm at name of meals")
    
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
    
    print("\n I'm at get info and stuff")
    
    total_dict = {
        "Calories": 0.0,
        "Fat": 0.0,
        "Protein": 0.0,
        "Sugar": 0.0,
        "Fiber": 0.0,
        "Carbs": 0.0
    }

    # Your existing code to populate the dictionary
    for item in json_file:
        total_dict["Calories"] += item["calories"]
        total_dict["Fat"] += item["fat_total_g"]
        total_dict["Protein"] += item["protein_g"]
        total_dict["Sugar"] += item["sugar_g"]
        total_dict["Fiber"] += item["fiber_g"]
        total_dict["Carbs"] += item["carbohydrates_total_g"]
        
    total_dict = {k: round(v, 1) for k, v in total_dict.items()}
    
    return total_dict
    
def cloud_dict(json_file):
    return {
        "Meal Items": get_names_of_meal(json_file),
        "Nutrition Info": get_total_info(json_file)
    }
    
    
    

if __name__ == "__main__":
    
    query = input("Enter food item: ")
    
    json_file = get_api_response(query)
    print(json_file)
    print(get_names_of_meal(json_file=json_file))
    print(get_total_info(json_file=json_file))
    print(cloud_dict(json_file))
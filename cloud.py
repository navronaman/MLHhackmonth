# For the firebase integration
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
from datetime import datetime

# Create a folder in the portal called keys, and get your serviceAccount
cred = credentials.Certificate("key/serviceAccountKey.json")

firebase_admin.initialize_app(cred, {
   "databaseURL": "https://calories-tracker-aade3-default-rtdb.firebaseio.com/",
    "storageBucket": "calories-tracker-aade3.appspot.com"
})

def format_time2(current_time):
    # Format the date and time
    formatted_date_time = current_time.strftime("%m_%d_%Y %I_%M_%S %p")
    
    return formatted_date_time



def inti_cloud(cloud_dict_of_meal, username):
    print("Cloud integration started")

    today_date = datetime.now()


    ref = db.reference(username)
    date_ref = ref.child(today_date.strftime("%B %d, %Y"))
    
    meal_ref = date_ref.child(f"Meal at {format_time2(today_date)}")
    meal_ref.set(cloud_dict_of_meal)
    print(ref.get())
    
    
def get_data(username):
    ref = db.reference(username)
    return ref.get()

if __name__ == "__main__":
    
    api_rep = get_data("navronaman")
    print(api_rep)
    
    inti_cloud()


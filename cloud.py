# For the firebase integration
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
from datetime import datetime

# Create a folder in the portal called keys, and get your serviceAccoun
cred = credentials.Certificate("key/serviceAccountKey.json")

firebase_admin.initialize_app(cred, {
   "databaseURL": "https://calories-tracker-aade3-default-rtdb.firebaseio.com/",
    "storageBucket": "calories-tracker-aade3.appspot.com"
})



today_date = datetime.now()
print(today_date)

def inti_cloud():
    print("Cloud integration started")

    ref = db.reference("Trial")
    date_ref = ref.child("Hello")


    date_ref.set({
        "User entered a meal at this time": {
            "meal_items": "french_fries",
        }
    })


    print(ref.get())

if __name__ == "__main__":
    inti_cloud()


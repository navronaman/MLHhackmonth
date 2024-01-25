# For the firebase integration
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
from datetime import datetime

# Create a folder in the portal called keys, and get your serviceAccoun
cred = credentials.Certificate("keys/serviceAccountKey.json")

firebase_admin.initialize_app(cred, {
   "databaseURL": "https://calories-tracker-aade3-default-rtdb.firebaseio.com/",
    "storageBucket": "gs://calories-tracker-aade3.appspot.com"
})




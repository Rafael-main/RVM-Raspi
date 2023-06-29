import time
import threading
import uuid
import random

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import RPi.GPIO as GPIO
from simplemfrc522 import SimpleMFRC522

# # Initialize RFID reader
reader = SimpleMFRC522()

# Initialize Firebase credentials and Firestore client
cred = credentials.Certificate("./rvm-fire-firebase-adminsdk-tmfzs-dece4493b4.json")  # Replace with your service account key path
firebase_admin.initialize_app(cred)
db = firestore.client()

def read_rfid():
    # Main loop
    try:
        while True:
            # Scan for cards
            id, text = reader.read()

            # Convert UID to string
            if id:
                uid_str = ''.join(f'user-{str(uuid.uuid4())[:5]}')

                add_data = {
                    'id': uid_str,
                    'imageUrl': 'm',
                    'points': 100,
                    'public': True,
                    'rank': '0',
                    'rfidtag': '789c',
                    'username': 'ricci'
                }

                update_data = {'rfidtag': 'mnl9132'}

                doc_num = 1833901

                add(add_data)
                update(doc_num, update_data)

    except KeyboardInterrupt:
        GPIO.cleanup()


def add(data):
    # Convert UID to string
    doc_num = random.randrange(1000000,9999999)
    
    
    # Send UID to Firestore
    doc_ref = db.collection('Users').document(f'{doc_num}')
    doc_ref.set(data)

def update(doc_num, update_data):
    user_doc =  db.collection("Users").document(f'{doc_num}')
    user_doc.update(update_data)

update(1833901)
# add()

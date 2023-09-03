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

cred = credentials.Certificate("./rvm-fire-firebase-adminsdk-tmfzs-dece4493b4.json") 
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

class RvmFire:

    def readUser(self, uid):
        user_doc = db.collection("Users").document(str(uid))

    def updateRFIDTag(self, rfidpass, update_data):
        docs = (
            db.collection("Users")
            .where(filter=FieldFilter("capital", "==", rfidpass))
            .stream()
        )

        for doc in docs:
            print(f"{doc.id} => {doc.to_dict()}")
        user_doc =  db.collection("Users").document(f'{uid}')
        user_doc.update(update_data)

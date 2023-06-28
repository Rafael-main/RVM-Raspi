import time
import threading

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import RPi.GPIO as GPIO
import MFRC522

# Initialize RFID reader
MIFAREReader = MFRC522.MFRC522()

# Initialize Firebase credentials and Firestore client
cred = credentials.Certificate("path/to/serviceAccountKey.json")  # Replace with your service account key path
firebase_admin.initialize_app(cred)
db = firestore.client()

# Main loop
try:
    while True:
        # Scan for cards
        (status, TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

        # If a card is detected
        if status == MIFAREReader.MI_OK:
            # Get the UID of the card
            (status, uid) = MIFAREReader.MFRC522_Anticoll()

            # Convert UID to string
            uid_str = ''.join(str(i) for i in uid)

            # Send UID to Firestore
            doc_ref = db.collection(u'rfid_scans').document()
            doc_ref.set({u'uid': uid_str})

            print("UID scanned and sent to Firestore: {}".format(uid_str))

except KeyboardInterrupt:
    GPIO.cleanup()

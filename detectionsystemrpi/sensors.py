import os
from firebase_admin import firestore
from firebase_admin import credentials
from google.cloud import storage, exceptions

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "**INSERT FIREBASE AUTHENTICATION**"
cred = credentials.Certificate("*INSERT FIREBASE AUTHENTICATION*")

class Sensors:
 #constructor
    def __init__(self, floor, desk, sensor):
        db = firestore.Client()
        desk_ref = db.collection(floor).document(desk)
        sensors_ref = desk_ref.collection(u'Sensors').document(sensor)
        self.doc_ref=sensors_ref

    def setSensorStatus(self, status):
           self.doc_ref.set({
               u'Status': status
           })

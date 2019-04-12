import os
from firebase_admin import firestore
from firebase_admin import credentials
from google.cloud import storage, exceptions

os.environ[
        "GOOGLE_APPLICATION_CREDENTIALS"] = "**INSERT FIREBASE AUTHENTICATION**"
cred = credentials.Certificate("**INSERT FIREBASE AUTHENTICATION**")

class Settings:

#id of the sensor
sensorID = u'qeDmnlyKZ55KECFAoTs3'
 #constructor
    def __init__(self):
        self.db = firestore.Client()

#loads sensor settings
    def getSensorSettings(self):
        try:

            value = self.db.collection(u'SensorSetting').document(sensorID)
            values = value.get().to_dict()
            return values

        except exceptions.NotFound:
            print(u'No such document!')
            return 0

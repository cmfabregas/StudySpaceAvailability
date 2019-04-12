import os
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from google.cloud import storage, exceptions


class Sensors:

    os.environ[
        "GOOGLE_APPLICATION_CREDENTIALS"] = "**INSERT CREDENTIALS**"
    cred = credentials.Certificate(
        "**INSERT CREDENTIALS HERE**")

    #constructor
    def __init__(self, floor, desk, sensor):
        db = firestore.Client()
        desk_ref = db.collection(floor).document(desk)
        sensors_ref = desk_ref.collection(u'Sensors').document(sensor)
        self.doc_ref=sensors_ref;

    def getSensor1Status(self):
        try:
            doc = self.doc_ref.get().to_dict()
            value = doc['Status']
            # print(value)
            # print(u'Document data: {}'.format(doc))
        except exceptions.NotFound:
            print(u'No such document!')

        return value

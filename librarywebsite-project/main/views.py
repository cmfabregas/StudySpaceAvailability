from django.shortcuts import render
from pyrebase import pyrebase
from django.contrib import auth
from firebase_admin import firestore
from firebase_admin import credentials
import os
from .sensors import Sensors
# Create your views here.

config = {
    ##INERT API CREDENTIALS HERE
    'apiKey': "",
    'authDomain': "",
    'databaseURL': "",
    'projectId': "",
    'storageBucket': "",
    'messagingSenderId': ""
}

firebase = pyrebase.initialize_app(config)
authenticate= firebase.auth()
database = firebase.database()


def countSensor1():
    RPI=[]
    for x in range(3):
        y=x+1
        RPI.append(Sensors(u'Floor1', u'desk%d'%y, u'sensor1'))
    X = []
    X.append(RPI[0].getSensor1Status())
    X.append(RPI[1].getSensor1Status())
    X.append(RPI[2].getSensor1Status())
    return X.count(True)
#end of detection

def signIn(request):
    return render(request, 'main/signIn.html')

def postsign(request):
    email = request.POST.get('login')
    passw = request.POST.get('pass')
    try:
        user = authenticate.sign_in_with_email_and_password(email,passw)
    except:
        message="Invalid Username or Password"
        return render(request, "main/signIn.html",{"message":message})
    print(user)
    session_id=user['idToken']
    request.session['uid'] = str(session_id)

    floor1 = countSensor1()
    return render(request, 'main/welcome.html', {"email":email, "floor1":floor1})

def home(request):
    session_id = request.session['uid']
    email = getUserEmail(session_id)
    floor1 = countSensor1()
    return render(request, 'main/welcome.html', {"email":email, "floor1":floor1})

def logout(request):
    auth.logout(request)
    return render(request, 'main/signIn.html')

def getUserEmail(session_id):
    a = authenticate.get_account_info(session_id)
    a = a['users']
    a = a[0]
    email = a['email']
    return email

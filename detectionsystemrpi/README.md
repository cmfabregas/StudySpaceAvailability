# DetectionSystemRPI

How to run on a raspberry pi zero w/ camera:
===


Install the Python Virtual Environment package:
```pip3 install virtualenv```

Create the Virtual Environment:
```virtualenv detectionenvironment```

Activate Virtual Environment:
```source detectionenvironment/bin/activate```

Then install dependencies by:
```pip3 install -r requirements.txt```

Insert Firebase API Credentials --> ```sensors.py & settings.py```

Insert sensorID on the firebase cloud firestore (document ID)

Run: ```python3 humandetection.py```

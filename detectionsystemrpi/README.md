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


Insert sensorID on the firebase cloud firestore (document ID):

This will need to be configured on the firebase datastore with a collection called ```SensorSetting``` --> generate a Document with Auto ID copy the ID and paste it on the sensorID variable in ```sensors.py``` and create two fields ```Desk``` and ```Floor``` with values for Desk number Ex: ```desk1``` and floor number Ex: ```floor```. 


Run: ```python3 humandetection.py```

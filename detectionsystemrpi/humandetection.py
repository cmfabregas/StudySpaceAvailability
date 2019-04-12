from picamera import PiCamera
import time
import io
from google.cloud import vision
from google.cloud.vision import types
from sensors import Sensors
from settings import Settings
from takeimage import TakeImage


humanthreshold = 0.75; #threshold for human
itemsthreshold = 0.70; #threshold for items

#checks if a face is detected in the image
def checkhuman(labels):
	print("human detection: "),
	for label in labels:
		print(label.description,label.score)
		if label.description == 'Face' and label.score > humanthreshold:
			return True
		elif label.description =='Hair' and label.score > humanthreshold:
			return True
		elif label.description =='Facial hair' and label.score > humanthreshold:
			return True
		elif label.description =='Arm' and label.score > humanthreshold:
			return True
		elif label.description =='Chin' and label.score > humanthreshold:
			return True
		elif label.description =='Shirt' and label.score > humanthreshold:
			return True
		elif label.description =='Beard' and label.score > humanthreshold:
			return True
		elif label.description =='Eyewear' and label.score > humanthreshold:
			return True
		elif label.description =='Glasses' and label.score > humanthreshold:
			return True
		elif label.description =='Forehead' and label.score > humanthreshold:
			return True
		elif label.description =='Eye' and label.score > humanthreshold:
			return True
		elif label.description =='Nose' and label.score > humanthreshold:
			return True
		elif label.description =='Eyebrow' and label.score > humanthreshold:
			return True
		elif label.description =='Jaw' and label.score > humanthreshold:
			return True
		elif label.description =='Cheek' and label.score > humanthreshold:
			return True
		elif label.description =='Finger' and label.score > humanthreshold:
			return True
		elif label.description =='Suit' and label.score > humanthreshold:
			return True
		elif label.description =='Formal wear' and label.score > humanthreshold:
			return True
		elif label.description =='Tuxedo' and label.score > humanthreshold:
			return True
		elif label.description =='Businessperson' and label.score > humanthreshold:
			return True
	return False

def checkitems(labels):
	print("item detection: "),
	for label in labels:
		print(label.description,label.score)
		if label.description == 'Electronics' and label.score > itemsthreshold:
			return True
		if label.description == 'Waterbottle' and label.score > itemsthreshold:
			return True
		if label.description == 'Electronic instrument' and label.score > itemsthreshold:
			return True
		if label.description == 'Electronic device' and label.score > itemsthreshold:
			return True
		if label.description == 'Computer keyboard' and label.score > itemsthreshold:
			return True
		if label.description == 'Computer hardware' and label.score > itemsthreshold:
			return True
		if label.description == 'Technology' and label.score > itemsthreshold:
			return True
		if label.description == 'Material property' and label.score > itemsthreshold:
			return True
	return False


#get floor desk and sensor
#key to each pi

#sensor settings for database
setting = Settings()
values = setting.getSensorSettings()
print(values)


sensor1 = Sensors(values['Floor'], values['Desk'], u'sensor1')
sensor2 = Sensors(values['Floor'], values['Desk'], u'sensor2')

##initiates PiCamera
camera = PiCamera()

##run while loop for 15 min
t_end = time.time() + 60 * 15
while time.time() < t_end:
	##take picture
	takeimage = TakeImage(camera)

	#reads the image taken by the picamera
	vision_client = vision.ImageAnnotatorClient()
	file_name = 'example.jpg'

	#reads image
	with io.open(file_name, 'rb') as image_file:
		content = image_file.read()
	image = types.Image(content=content)
	response = vision_client.label_detection(image=image)
	labels = response.label_annotations

	#checks if human is present
	humanstatus = checkhuman(labels)
	#checks if items are present
	itemsstatus = checkitems(labels)

	#sends sensor status to firebase database
	sensor1.setSensorStatus(humanstatus)
	sensor2.setSensorStatus(itemsstatus)

import picamera
import boto3
from espeak import espeak
import time
import RPi.GPIO as GPIO
import json

exclusions = ['Room', 'Furniture', 'Indoors', 'Interior Design', 'Dining Room', 'Electrical Device', 'Appliance', 'Human', 'People']
camera = picamera.PiCamera()

# Create an S3 client
s3 = boto3.client('s3')

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)

fileName = '/var/www/html/vision.jpg'
bucket = 'vision-control-files'

collection_id = "Family"

def search_faces_by_image(bucket, key, collection_id, threshold=60, region="us-east-1"):
	rekognition = boto3.client("rekognition", region)

	try:
		response = rekognition.search_faces_by_image(
			Image={
				"S3Object": {
					"Bucket": bucket,
					"Name": key,
				}
			},
			CollectionId=collection_id,
			FaceMatchThreshold=threshold,
		)
		return response['FaceMatches']
	except:
		return None


while True:
	input_state = GPIO.input(14)

	if input_state == False:
		espeak.synth("taking picture and analyze")
		camera.capture('/var/www/html/vision.jpg')

		# Uploads the given file using a managed uploader, which will split up large
		# files automatically and upload parts in parallel.
		s3.upload_file(fileName, bucket, fileName)

		client = boto3.client('rekognition')

		response = client.detect_labels(Image={'S3Object': {'Bucket': bucket, 'Name': fileName}}, MinConfidence=75)

		print('Detected labels for ' + fileName)

		print(json.dumps(response))


		print('-------------------------------------')
		# only say labels not in the exclusion list, because they are generic words
		items_said = 0
		for label in response['Labels']:
			print(label['Name'] + ' : ' + str(label['Confidence']))
			if label['Name'] not in exclusions:
				if label['Name'] == 'Person':
					faces = search_faces_by_image(bucket, fileName, collection_id)
					if faces is not None:
						for record in faces:
							face = record['Face']
							espeak.synth(face['ExternalImageId'][:-3])
							time.sleep(2)
							print("Matched Face ({}%)".format(record['Similarity']))
							print("  FaceId : {}".format(face['FaceId']))
							print("  ImageId : {}".format(face['ExternalImageId'][:-3]))

				espeak.synth(label['Name'])
				time.sleep(2)
				items_said = items_said + 1


		# if nothing than generic words where found say generic words
		if items_said == 0:
			for label in response['Labels']:
				print('say again :' + label['Name'] + ' : ' + str(label['Confidence']))
				espeak.synth(label['Name'])
				items_said = items_said + 1
				time.sleep(2)

		if items_said == 0:
			espeak.synth('nothing detected')
		print('-------------------------------------')



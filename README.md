# HelpToSee
Is a Raspberry Pi project that takes an image via a camera, sends the image to an S3 bucket in AWS where it gets analyzed by AWS rekognition to detect labels (or objects) in the image. If a human was detected it is trying to detect who it is by using a reference collection that is registered in rekognition. Once the analysis is done the labels and names of detected people are send back to the raspberry PI where espeak is used to output the labels and person names to a speaker. 

![Architecture](https://github.com/Hofi2010/HelpToSee/raw/master/HelpToSeeArchitecture.001.jpeg)

## Hardware Setup
Below the hardware setup I used. One Raspberry Pi 3, powered by a battery pack. A Raspberry Pi Camera attached in the front and trigger button in the back. Whenever the user presses the button an image is taken and uploaded to AWS S3. AWS Rekognition service analyses the images and sends back the labels and face ids. The raspberry pi outputs the labels and person names via the headphones in my setup to the user. 

![Prototype](https://github.com/Hofi2010/HelpToSee/raw/master/HelpToSee-Prototype.JPG)

This setup can be helpful for people with visual impairements. I debated an iphone app, but a physical button as a trigger and a simple self contained device such as the raspberry pi will be much easier for a visual impaired person to handle as they most likely cannot operate the iphone. 

## Raspberry PI Preperation
In order to run the software install the following components:
1. Pyhtion 2.7
2. AWS CLI
3. boto3
4. Raspberry PI Camera for Python library
5. GPIO Python Library

This application needs WiFi conection and therefore can be a bit slow

## AWS Preperations
You have to create a collection for rekognition with photos of people you want to detect. It is better to have multiple photos for each person to increase detection accuracy. The file "AWS Faces Rekognition CLI" includes all the command line command to create a library and index faces into it. Is is easiest to upload the images to AWS S3 for registration with the collection.

## Conclusions
Initial testing of the setup and with AWS rekognition revealed that the raspberry pi camera has some problem in low light situation,, which makes detection of objects and people  difficult. In good light situations on the other hand the results are quite encouraging. With a very small image collection I was able to successfully detect the faces of all our family members and the object recognition is quite impressive. Not perfect, but quite good. To decrease some annoyance I am filtering out certain categories that are too general as it impacts the user experience. Who wants to listen to 5 or 6 labels that describes the same thing, e.g. Human,People, Person etc. 

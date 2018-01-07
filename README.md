# HelpToSee
Is a Raspberry Pi project that takes an image via a camera, sends the image to an S3 bucket in AWS where it gets analyzed by AWS rekognition to detect labels (or objects) in the image. If a human was detected it is trying to detect who it is by using a reference collection that is registered in rekognition. Once the analysis is done the labels and names of detected people are send back to the raspberry PI where espeak is used to output the labels and person names to a speaker. 

![Architecture](https://github.com/Hofi2010/HelpToSee/raw/master/HelpToSeeArchitecture.001.jpeg)

# Hardware Setup
Below the hardware setup I used. One Raspberry Pi 3, powered by a battery pack. A Raspberry Pi Camera attached in the front and trigger button in the back. Whenever the user presses the button an image is taken and copied to AWS S3.

![Prototype](https://github.com/Hofi2010/HelpToSee/raw/master/HelpToSee-Prototype.JPG)

# Raspberry PI Preperation
In order to run the software install the following components:
1. Pyhtion 2.7
2. AWS CLI
3. boto3
4. Raspberry PI Camera for Python library
5. GPIO Python Library

# AWS Preperations
You have to create a collection for rekognition with photos of people you want to detect. It is better to have multiple photos for each person to increase detection accuracy. The file "AWS Faces Rekognition CLI" includes all the command line command to create a library and index faces into it. Is is easiest to upload the images to AWS S3 for registration with the collection.


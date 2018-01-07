# HelpToSee
Is a Raspberry Pi project that takes an image via a camera, sends the image to an S3 bucket in AWS where it gets analyzed by AWS rekognition to detect labels (or objects) in the image. If a human was detected it is trying to detect who it is by using a reference collection that is registered in rekognition. Once the analysis is done the labels and names of detected people are send back to the raspberry PI where espeak is used to output the labels and person names to a speaker. 

![Architecture](https://github.com/Hofi2010/HelpToSee/raw/master/HelpToSeeArchitecture.001.jpeg)


![Prototype](https://github.com/Hofi2010/HelpToSee/raw/master/HelpToSee-Prototype.JPG)


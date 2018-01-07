# HelpToSee
Is a Raspberry Pi project that takes an image via a camera, sends the image to an S3 bucket in amazon where it gets analyzed by aws rekognition to detect labels (or objects) in the image. If a guman was detected it is trying to detect who it is by using a reference collection that is registered in rekognition. Once the analysis is done the labels and names of detected humans are send back to the raspberry PI where we use espeak to output the labels and person names to a speaker. 

![Architecture](https://github.com/Hofi2010/HelpToSee/raw/master/HelpToSeeArchitecture.001.jpeg)


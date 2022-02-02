# image_to_text
Covert words from an image to a text file using Rekognition

This program is run through cmd. You upload an image to the specified S3 bucket (hardcoded into the file, it is "upload-image-feb-2022 by default"), and feed the program the file name so it can find it in the bucket. It uses the detectText function from AWS Rekognition and outputs the detected text to a txt file to the desktop of the user. The formatting is kept the same as it is in the image.

This kind of program can be good for converting physical notes or documents to text that can be copied or edited on the computer.

import boto3
import os

#setup
client = boto3.client('rekognition')
s3 = boto3.resource('s3')
upload_bucket = 'upload-image-feb-2022'
bucket = s3.Bucket(upload_bucket)

#getting the name of the file to read
files = [file.key for file in list(bucket.objects.all())]
image_file = input("image file name (with extension): ")

try:
    # retrieving the image from bucket
    img = s3.Object(bucket_name=upload_bucket, key=image_file).get()

    # detecting text with rekognition
    response = client.detect_text(Image={'S3Object': {'Bucket': upload_bucket, 'Name': image_file}})
    text = response['TextDetections']

except:
    # if img not found in bucket
    print("no file of that name was found in the bucket " + upload_bucket)

# creating new file on desktop
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
file = open(desktop+'\\GeneratedText.txt', "w+")

# writing to file + printing results
for word in text:
    if(word['Type']=='LINE'):
        file.write(word['DetectedText']+'\n')

print('success: generated text at '+desktop+'\\GeneratedText.txt')
file.close()
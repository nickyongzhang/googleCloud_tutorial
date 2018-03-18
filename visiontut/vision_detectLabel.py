import io
from google.cloud import vision
from google.cloud.vision import types

vision_client = vision.ImageAnnotatorClient()
file_name = '375px-Guido_van_Rossum_OSCON_2006_cropped.png'

with io.open(file_name, 'rb') as image_file:
    content = image_file.read()
    image = types.Image(content=content)

response = vision_client.label_detection(image=image)
labels = response.label_annotations
for label in labels:
    print(label.description,label.score)

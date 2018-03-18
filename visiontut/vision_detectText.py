import io
from google.cloud import vision
from google.cloud.vision import types

vision_client = vision.ImageAnnotatorClient()
file_name = 'machine-learning-playlist.png'
#change a file to experiment
# file_name = 'block-of-text.png'

with io.open(file_name, 'rb') as image_file:
    content = image_file.read()
    image = types.Image(content=content)

response = vision_client.text_detection(image=image)
labels = response.text_annotations
for label in labels:
    print(label.description,label.score)

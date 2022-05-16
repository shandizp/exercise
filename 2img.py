import requests
r = requests.get('https://placebear.com/200/300.jpg')

#file = open("sample_image.png", "wb")
from PIL import Image
from io import BytesIO

i = Image.open(BytesIO(r.content))
i.show()


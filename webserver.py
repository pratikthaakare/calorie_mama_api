from PIL import Image
foo = Image.open("food1.jpg")
foo = foo.resize((544,544),Image.ANTIALIAS)
foo.save("foo.jpg")

import requests

headers = {
    'Content-Type': 'image/jpeg',
}

params = (
    ('user_key', '4795e522933e3939c30eb100dd748ad9')
)

data = open('/home/vinayak/PycharmProjects/Calorie_Mama_API/foo.jpg', 'rb').read()

r = requests.post('https://api-2445582032290.production.gw.apicast.io/v1/foodrecognition?user_key=4795e522933e3939c30eb100dd748ad9', headers=headers, data=data)
print(r.text)
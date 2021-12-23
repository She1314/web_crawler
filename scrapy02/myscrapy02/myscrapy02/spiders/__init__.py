# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

# from pymongo import MongoClient
#
# client = MongoClient(host='127.0.0.1', port=27017)
# db = client.spider
# collection = db.spider
# user = {"name": "方文略"}
# collection.insert_one(user)
# for i in collection.find():
#     print(i)
#
# client.close()
from PIL import Image, ImageDraw, ImageFont
import random
import string


class ImageVerify(object):
    def __init__(self, width=140, height=40, size=30, length=4):
        self.width = width
        self.height = height
        self.size = size
        self.length = length

    def random_str(self):
        str = string.ascii_letters + '1234567890'
        image_code = [i for i in random.choices(population=str, k=self.length)]
        return ''.join(image_code)

    def random_color(self, start, end):
        return tuple(random.randint(start, end) for i in range(3))

    def image_code(self):
        image = Image.new(mode='RGB', size=(self.width, self.height), color=(255, 255, 255))
        draw = ImageDraw.Draw(im=image)
        font_fil = r'C:\WINDOWS\FONTS\SIMFANG.TTF'
        font = ImageFont.truetype(font=font_fil, size=self.size)
        for i in range(len(self.random_str())):
            draw.text(xy=(30 * i + 10, 3), text=self.random_str()[i], fill=self.random_color(60, 255), font=font)
        return image


if __name__ == '__main__':
    image = ImageVerify()
    img = image.image_code()
    with open(file='test.png', mode='wb') as f:
        img.save(fp=f, format='PNG')

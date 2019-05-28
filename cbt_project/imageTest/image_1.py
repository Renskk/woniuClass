# -*- coding: utf-8 -*-
import time
from PIL import Image, ImageGrab


class ImageMatch:
    def __init__(self):
        pass

    def find_image(self, image):
        # ImageGrab.grab().save('./image_data/1.png')
        time.sleep(0.5)
        big_image = ImageGrab.grab().convert('RGBA')
        # big_image = Image.open('./image_data/1.JPG')
        small_image = Image.open(image)
        bwidth, bheight = big_image.size
        swidth, sheight = small_image.size
        brgba = big_image.load()
        srgba = small_image.load()
        for y in range(bheight - sheight):
            for x in range(bwidth - swidth):
                if brgba[x, y] == srgba[0, 0] and brgba[x + swidth - 1, y + sheight - 1] == srgba[
                    swidth - 1, sheight - 1] \
                        and brgba[x + swidth - 1, y + sheight - 1] == srgba[swidth - 1, 0]:
                    if self.stupid_image(x, y, sheight, swidth, brgba, srgba):
                        center_x = int(x + swidth / 2)
                        center_y = int(y + sheight / 2)
                        # print(center_x,center_y)
                        return center_x, center_y

    def stupid_image(self, x, y, sheight, swidth, brgba, srgba):
        same = 0
        diff = 0
        for j in range(swidth):
            for i in range(sheight):
                if brgba[x + j, y + i] == srgba[j, i]:
                    same += 1
                else:
                    diff += 1
        if same / (same + diff) >= 0.8:
            return True
        else:
            return False


if __name__ == '__main__':
    ImageMatch().find_image('image_data/login.png')

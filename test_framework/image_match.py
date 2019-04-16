import time, os, random
from PIL import ImageGrab, Image

# 基于模板匹配算法实现的图像识别
class ImageMatch:
    def __init__(self):
        pass

    def find_image(self, image):
        small = Image.open(image)
        swidth, sheight = small.size    # 小图的宽和高

        sdata = small.load()

        # 根据用户截图的像素值是否带Alpha通道来决定如何对当前屏幕截图
        if len(sdata[0,0]) == 4:
            big = ImageGrab.grab().convert('RGBA')
        else:
            big = ImageGrab.grab()

        bdata = big.load()
        bwidth, bheight = big.size  # 大图的宽和高

        # 纵向还是横向？橫向
        for y in range(bheight - sheight):
            for x in range(bwidth-swidth):

                if bdata[x, y] == sdata[0, 0] and bdata[x+swidth-1, y+sheight-1] == sdata[swidth-1, sheight-1]:
                    if self.check_match(bdata, x, y, sdata, swidth, sheight):
                        center_x = int(x + swidth/2)
                        center_y = int(y + sheight/2)
                        # print("找到图片，对应位置为: [%d, %d]" % (center_x, center_y))
                        return center_x, center_y

        return -1, -1


    # 在小图中的(0, 0)对应大图的(x, y)，同时循环小图的宽和高的次数，来进行像素点的完全比对。
    # def check_match(self, bdata, x, y, sdata, swidth, sheight):
    #     for j in range(sheight):
    #         for i in range(swidth):
    #             if bdata[x + i, y + j] != sdata[i, j]:
    #                 return False
    #     return True


    # 利用匹配度来完善模板匹配，把小图的所有像素点全部对比一遍，根据相同像素点占所有像素点的比例来决定是否匹配成功
    def check_match(self, bdata, x, y, sdata, swidth, sheight):
        same = 0
        diff = 0
        for j in range(sheight):
            for i in range(swidth):
                if bdata[x + i, y + j] == sdata[i, j]:
                    same += 1
                else:
                    diff += 1
        similarity = same / (same + diff)
        # print("匹配度为：%f." % similarity)
        if  similarity >= 0.9:
            return True
        else:
            return False


if __name__ == '__main__':
    im = ImageMatch()
    time.sleep(3)
    im.find_image()

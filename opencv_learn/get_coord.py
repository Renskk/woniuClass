import cv2, time
from PIL import ImageGrab


class ctr:
    def __init__(self):
        pass

    def opencv2(self, image_temp):
        image = ImageGrab.grab()
        image.save(r"image/test.png")

        # 读取名称为 p20.png 的图片，并转成黑白
        img = cv2.imread(r"image/test.png", 0)

        # 读取需要检测的芯片图片（黑白）
        img_template = cv2.imread(image_temp, 0)

        # 得到芯片图片的高和宽
        w, h = img_template.shape[::-1]

        # 模板匹配操作
        res = cv2.matchTemplate(img, img_template, cv2.TM_SQDIFF_NORMED)

        # 得到最大和最小值得位置
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        top_left = min_loc  # 左上角的位置
        click = (top_left[0] + w/2, top_left[1] + h/2)  # 匹配图像的中心坐标点
        return click


if __name__ == '__main__':
    ctr().opencv2(r"image/username.png")
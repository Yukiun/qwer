from PIL import Image
import argparse

log = print
parser = argparse.ArgumentParser()
parser.add_argument('file')

args = parser.parse_args()
IMG = args.file


def grayscale(image):
    w = image.width
    h = image.height
    for i in range(w):
        for j in range(h):
            position = (i, j)
            r, g, b, a = image.getpixel(position)
            Gray = int(r * 0.3 + g * 0.59 + b * 0.11)
            image.putpixel(position, (Gray, Gray, Gray, a))
    # 保存图像文件
    log('成功')
    image.save('{}.png'.format('黑白'))


def main():
    # 打开图像文件
    im = Image.open(IMG)
    # 注意由于不是每个图像都有 a 所以这里强制转换成 RGBA 格式
    img = im.convert('RGBA')
    grayscale(img)

    # 保存图像文件
    # img.save('0(1).jpg')


if __name__ == '__main__':
    main()

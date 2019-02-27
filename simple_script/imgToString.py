from PIL import Image
import argparse

# argparse是一个命令解析器
"""
description:
    将图片像素转换为字母重新绘制输出
"""

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

parser = argparse.ArgumentParser()

parser.add_argument('file')
parser.add_argument('-o','--output')
parser.add_argument('--width',type=int,default=144)
parser.add_argument('--height',type=int,default= 96)

args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]


def save_to_file(file_name, contents):
    fh = open(file_name, 'w')
    fh.write(contents)
    fh.close()


def main():
    im = Image.open(IMG)
    image = im.convert('RGBA')
    w = int(image.width/20)
    h = int(image.height/20)
    im = im.resize((w,h),Image.NEAREST)
    txt = ""
    for i in range(h):
        for j in range(w):
            txt += ' ' + get_char(*im.getpixel((j,i)))
        txt += '\n'
    print(txt)
    save_to_file('{}.txt'.format(IMG), txt)


if __name__=="__main__":
    main()
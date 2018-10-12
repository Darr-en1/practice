from PIL import Image

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunx"
                  "rjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


IMG = "../picture/ascii_dora.png"
WIDTH = 120
HEIGHT = 80

# OUTPUT = "output.txt"

def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]


if __name__ == '__main__':
    im = Image.open(IMG)
    im = im.resize((WIDTH,HEIGHT), Image.NEAREST)

    txt = ''

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i)))
            print(im.getpixel((j,i)))
        txt += '\n'

    print(txt)


    with open("../picture/output.txt",'w') as f:
        f.write(txt)

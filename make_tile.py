from PIL import Image
import pytz
import datetime
import sys

def open_digit(c):
    return Image.open(f"{c}/{c}.png")

if __name__=="__main__":
    filename = "calendar.png"
    scale = 0
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    if len(sys.argv) > 2:
        scale = int(sys.argv[2])
    number = str((pytz.utc.localize(datetime.datetime.utcnow()).astimezone(pytz.timezone("Europe/Berlin")).date()-datetime.date(2020,3,1)).days+1)
    a,b,c = (open_digit(c) for c in str(number))
    base = Image.open("baseframe.png")

    digit_top=7
    digit_width=8
    digit_height=18

    base.alpha_composite(a,(2, digit_top))
    base.alpha_composite(b,(2+digit_width+1, digit_top))
    base.alpha_composite(c,(2+2*(digit_width+1), digit_top))
    if scale:
        base=base.resize((32*scale, 32*scale), Image.NEAREST)
    base.save(filename)


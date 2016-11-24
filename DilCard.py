 #!/usr/bin/env python
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os
import random

index = 0;
with open('list.txt') as f:
    lines = f.read().splitlines();
length = len(lines);
f.close();


for x in range(0, 3):
    img = Image.open("CavernDeep.png")
    imgBack = Image.open("CavernDeepBack.png")
    New_Img = Image.new('RGB', (1588,1123))
    draw = ImageDraw.Draw(img)
    drawTwo = ImageDraw.Draw(imgBack)
# font = ImageFont.truetype(<font-file>, <font-size>)
    FONT_PATH = os.environ.get("FONT_PATH", "/usr/share/fonts/blacksam/blacksam'sgold.ttf")
    font = ImageFont.truetype(FONT_PATH, 35)
    fontTwo = ImageFont.truetype(FONT_PATH, 80)
# draw.text((x, y),"Sample Text",(r,g,b))
    draw.text((70,90),"Slimy Pollywog",(255,255,255,000),font=font)
    draw.text((70, 130),lines[index],(255,255,255,000),font=font)
    drawTwo.text((70,90),"Slimy Pollywog",(255,255,255,000),font=font)
    drawTwo.text((70, 130),lines[index],(255,255,255,000),font=font)
    drawTwo.text((270,235),"Blackbeard Haircut Scale:",(001,001,001,100),font=font)
    drawTwo.text((280,260),str(random.randrange(100)),(245,012,012,100),font=fontTwo)
    drawTwo.text((270,370),"Emanuel Wynn Timeliness:",(001,001,001,100),font=font)
    drawTwo.text((280,400),str(random.randrange(100)),(245,012,012,100),font=fontTwo)
    drawTwo.text((270,510),"Jolly Roger Scale:",(001,001,001,100),font=font)
    drawTwo.text((280,540),str(random.randrange(100)),(245,012,012,100),font=fontTwo)
    drawTwo.text((270,650),"Gentle Pirate Scale:",(001,001,001,100),font=font)
    drawTwo.text((280,690),str(random.randrange(100)),(245,012,012,100),font=fontTwo)
    drawTwo.text((270,800),"Thomas Tew Gallantry Scale:",(001,001,001,100),font=font)
    drawTwo.text((280,840),str(random.randrange(100)),(245,012,012,100),font=fontTwo)
    drawTwo.text((270,930),"Henry Avery Raiding Scale:",(001,001,001,100),font=font)
    drawTwo.text((280,970),str(random.randrange(100)),(245,012,012,100),font=fontTwo)
    #fileName = lines[index] + "-CardFront.png"
    #fileNameTwo = lines[index] + "-CardBack.png"
    fileNameThree = lines[index] + ".png"
    New_Img.paste(img, (0,0));
    New_Img.paste(imgBack, (800,0));
    #img.save(fileName);
    #imgBack.save(fileNameTwo);
    New_Img.save(fileNameThree);

    index += 1;

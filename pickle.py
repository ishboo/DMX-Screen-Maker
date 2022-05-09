from PIL import Image, ImageDraw, ImageFont
import csv
font = ImageFont.truetype("trebuc.ttf", 40)
font2 = ImageFont.truetype("trebuc.ttf", 20)
width=160*20
height=24*20+10
canvas = Image.new('RGB', (width, height), 'grey')
img_draw = ImageDraw.Draw(canvas)
img_draw.rectangle([(0,0),(width-1,height-1)], outline ="red")


def festoon(x,y,universe,channel,length,direction):
    text=str(universe) + '.' + str(channel)
    img_draw.text((x*20,y*20+8), text, fill="white",font=font2)
    outline="blue"
    for lights in range(length):
        patch.writerow((x,y,universe,channel))
        img_draw.rectangle([(x*20,y*20),(x*20+8,y*20+8)], outline = outline)
        outline="red"
        if direction == 'L':
            x += 1
        if direction == 'D':
            y += 1
        channel += 4
# open the file in the write mode
f = open(r'\\10.2.20.101\d3 Projects\GBS\objects\Table\festoons.csv', 'w')

# create the csv writer
patch = csv.writer(f)

# write the header row, not specifying it as a tuple will make each character a column
patch.writerow('xyua')
with open('nodes.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        festoon(int(row[0]),int(row[1]),int(row[2]),int(row[3]),int(row[4]),str(row[5]),)
        x=int(row[2])
# close the file
f.close()
canvas.save(r'D:\Dropbox (FragmentNine)\SHARE - The Go Big Show\Pixel Maps\festoons.png')

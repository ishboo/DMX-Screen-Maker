from PIL import ImageFont, ImageDraw, Image
import csv

class Node:
    #x1,y1,x2,y2,step,universe,address,length,direction=0,0,0,0,1,1,1,1,'L'
    def __init__(self,x,y,u,a,l,d,z,s,c):
        self.x1,self.y1,self.universe,self.address,self.length,self.direction,self.split,self.step,self.chans=x,y,u,a,l,d,z,s,c
        if self.direction == 'L':
            self.x2=self.x1-l*self.step
            self.y2=self.y1
        if self.direction == 'R':
            self.x2=self.x1+l*self.step
            self.y2=self.y1
        if self.direction == 'U':
            self.x2=self.x1
            self.y2=self.y1-l*self.step
        if self.direction == 'D':
            self.x2=self.x1
            self.y2=self.y1+l*self.step
    def display(self):
        print('x:'+str(self.x1)+' y:'+str(self.y1)+' x:'+str(self.x2)+' y:'+str(self.y2))

class NodeArray:
    nodes=[]
    def addNode(self,x,y,u,a,l,d,z,s,c):
        self.nodes.append(Node(x,y,u,a,l,d,z,s,c))
        print('Node Added')
    def buildArray(self,t):
        skip=False
        for r in range(t.numRows):
            if skip:
                self.addNode(t[r,0],t[r,1],t[r,2],t[r,3],t[r,4],t[r,5],t[r,6],t[r,7],t[r,8])
            skip=True

    def display(self):
        print('Length is:'+str(len(self.nodes)))
        for node in self.nodes:
            node.display()
    def __init__(self,t):
        self.nodes=[]
        self.name=t.name
        self.buildArray(t)

    def resolution(self):
        width=4
        height=4
        for node in self.nodes:
            if node.x2>width:
                width=node.x2+1
            if node.y2>height:
                height=node.y2+1
            if node.x1>width:
                width=node.x1+1
            if node.y1>height:
                height=node.y1+1
        print(str(width)+'x'+str(height))
        return [width,height]


    def updateTable(self):
        font = ImageFont.truetype("trebuc.ttf", 40)
        font2 = ImageFont.truetype("trebuc.ttf", 20)
        width=self.resolution()[0]*20
        height=self.resolution()[1]*20
        canvas = Image.new('RGB', (width, height), 'grey')
        print([width,height])
        img_draw = ImageDraw.Draw(canvas)
        img_draw.rectangle([(0,0),(width-1,height-1)], outline ="red")



        def festoon(x,y,universe,channel,length,direction,split,step,chans):
            text=str(universe) + '.' + str(channel)
            img_draw.text((x*20,y*20+8), text, fill="white",font=font2)
            outline="blue"
            for lights in range(length):
                displayChannel=lights*chans+1
                if split>0:
                    real=lights+1
                    top=split
                    while top<real:
                        top+=split
                    bot=top-split
                    displayChannel=(top-real+bot)*chans+1
                patch.writerow((x,y,universe,displayChannel))
                img_draw.rectangle([(x*20,y*20),(x*20+8,y*20+8)], outline = outline)
                outline="red"
                if direction == 'L':
                    x -= 1*step
                if direction == 'D':
                    y += 1*step
                if direction == 'R':
                    x += 1*step
                if direction == 'U':
                    y -= 1*step
        # open the file in the write mode
        #f = open(str(op('vars')[0,0]), 'w')
        f = open(self.name+'.csv', 'w')

        # create the csv writer
        patch = csv.writer(f)

        # write the header row, not specifying it as a tuple will make each character a column
        patch.writerow('xyua')
        for node in self.nodes:
            festoon(node.x1,node.y1,node.universe,node.address,node.length,node.direction,node.split,node.step,node.chans)

        # close the file
        f.close()
        canvas.save(self.name+'.png')


def onTableChange(dat):
    array=None
    array=NodeArray(dat)
    array.updateTable()
    op('image').par.reload.pulse()
    return

'''
@author: Madhu, Karthik
Reads a csv input file with names and designations,name of event, date
and outputs png image files - badges.
'''

import Image, ImageDraw, ImageFont
import os
import csv

class badgeGenerate(object):
    
    def generate(self, name, desig, color):
        
        self.im = Image.open("template.png")
        self.dr = ImageDraw.Draw(self.im)
        self.drawString(100,170,color,name,'arial.ttf',70)
        self.drawString(150,270,color,desig,'arial.ttf',50)
        self.im.save(''+name+'.png')

    def drawString(self, x, y, color, string, font, size):

        ft = ImageFont.truetype(font,size)
        self.dr.text((x, y), string, fill=color, font=ft)
        
        
    
    
class input(object):

    def csvread(self, filename):
         
         reader = csv.reader(open(filename))
         for row in reader:
            if row[1] != 'Name':
                self.name = row[1]
                self.desig = row[2]
                self.color = row[3]
            
                b = badgeGenerate()
                b.generate(self.name, self.desig, self.color)


         
            

inp = input()
    
inp.csvread('BadgeInput1.csv')

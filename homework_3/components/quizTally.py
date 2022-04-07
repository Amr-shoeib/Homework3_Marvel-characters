from email.mime import image
from tkinter import Image
from xml.dom.pulldom import CHARACTERS
from components import vars
from PIL import Image
from emoji import emojize

def total(value):
    # do some logic to see which character you selected

    if value <= 10:
        vars.character = vars.characters[0]
        
    elif value >= 10:
        vars.character = vars.characters[1]
        

        print (emoji.emojize('It is :fire:,:boom:,:punch:,:muscle:')) + vars.character
        
        
        vars.character = Image.open ("Hulk.jpg")
        Image.show()

        vars.character = Image.open ("Thor.jpg")
        Image.show()

        vars.character = Image.open ("Captin America.jpg")
        Image.show()

    
    
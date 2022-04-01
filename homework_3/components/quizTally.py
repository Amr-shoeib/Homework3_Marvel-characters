from email.mime import image
from tkinter import Image
from xml.dom.pulldom import CHARACTERS
from components import vars
from PIL import CHARACTERS

def total(value):
    # do some logic to see which character you selected

    if value <= 10:
        vars.character = vars.characters[0]

        print("It's :fire:, :punch:,:muscle:"+ vars.character)
        # add some emoji icons, or show the character image using the Pillow package
        
        vars.character = Image.open ('Hulk.jpg')
        Image.show()

        vars.character = Image.open ('Thor.jpg')
        Image.show()

        vars.character = Image.open ('Captin America.jpg')
        Image.show()

    
       
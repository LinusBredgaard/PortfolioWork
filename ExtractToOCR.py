import pytesseract
from PIL import Image
import os
import shutil
from os import path



textfilename = "Output.txt"
Names = os.listdir()
Num = len(Names)
Num = Num-1

print(Names)


while Num !=-1:
    if Names[Num].endswith(".png") | Names[Num].endswith(".PNG"):
        Tests=pytesseract.image_to_string(Image.open(Names[Num]), config='equ +eng')
        f=open(textfilename, 'a')
        f.write(Tests + "@|?")
        f.close()
        source_path=Names[Num]
        new_location=shutil.move(source_path, "Images")
        #os.remove(Names[Num])
        Num = Num-1
    else:
        Num = Num-1

print("You have ran out of files/There are no png's left")


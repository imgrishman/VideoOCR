import pytesseract as tess
from PIL import Image
import hashlib

tess.pytesseract.tesseract_cmd= r"C:\Users\grish\OneDrive\Desktop\fresh\tract\tesseract.exe"
def extract(img) : 
    #img = Image.open(r'C:\Users\grish\OneDrive\Desktop\fresh\image1431.jpg')
    text= tess.image_to_string(img)
    #print(text)
    with open(r"C:\Users\grish\OneDrive\Desktop\fresh\save.txt",'a') as f:
        f.write(text)
    f.close()

def rm() :
#1
    output_file_path =r'C:\Users\grish\OneDrive\Desktop\fresh\ocrtext.txt'
    input_file_path = r'C:\Users\grish\OneDrive\Desktop\fresh\save.txt'

    #2
    completed_lines_hash = set()

    #3
    output_file = open(output_file_path, "w")

    #4
    for line in open(input_file_path, "r"):
        hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
    #6
    if hashValue not in completed_lines_hash:
        output_file.write(line)
        completed_lines_hash.add(hashValue)
    #7
    output_file.close()
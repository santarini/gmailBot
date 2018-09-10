import os
import img2pdf

with open("name.pdf","wb") as f:
    f.write(img2pdf.convert([i for i in os.listdir('C:/Users/santa/Desktop/bana/') if i.endswith(".jpg")]))

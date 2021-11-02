'''
Malaria Detection
Anggota Kelompok:
Bryant Andersson Tantra - 2301854706 
Muhamad Geonuurii Rizki Ramadhan - 2301895763
Kania Katherina - 2301873541
Albert Kurniawan - 2301872955

Link Youtube: https://youtu.be/gbQmgp_oC1U

'''

import cv2
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog 
from tensorflow.keras.models import load_model
import numpy as np

def wrt(st,fname):
    file = open(fname,"w+")
    file.write(st)
    file.close() 

def red(fname):    
    file = open(fname,"r")
    f=file.read()
    file.close() 
    return f

def openfilename(): 
   filename = filedialog.askopenfilename(title ='UPLOAD IMAGE') 
   return filename 

def open_img():
   try: 
      x = openfilename()
      wrt(x,"upload");print(x);
      img =Image.open(x)
   except:
      x = 'assets/error.png'
      print(x);
      img =Image.open(x)
   img = img.resize((325, 200), Image.ANTIALIAS) 
   img = ImageTk.PhotoImage(img) 
   panel = tk.Label(window, image = img) 
   panel.image = img 
   panel.place(x=600, y=150)

def detects():
   cell="\n Loading..."
   output.set(cell)
   try:
      new_model = load_model('cell_classification_model')
      images = []
      image = cv2.imread(red("upload"))
      image_from_array = Image.fromarray(image, "RGB")
      size_image = image_from_array.resize((50, 50))
      images.append(np.array(size_image))
      images = np.array(images)
      result = np.argmax(new_model.predict(images),1)
      cell="    TERINFEKSI            " if result[0]==1 else "TIDAK TERINFEKSI"
      output.set("\n   "+cell+ "  \n");print(cell)
   except:
      output.set(cell);print("EXCEPTION")

window = tk.Tk()
window.title("Malaria Detection")
window.iconbitmap('assets/logo.ico')
window.geometry("1440x810")

output=tk.StringVar();

bgimage = Image.open("assets/Background.png")
background = ImageTk.PhotoImage(bgimage.resize((1440, 810)))
tk.Label(window,image=background).place(x=0,y=0)


img =Image.open("assets/1200px-No_image_3x4.png")
img = img.resize((325, 200), Image.ANTIALIAS) 
img = ImageTk.PhotoImage(img) 
panel = tk.Label(window, image = img) 
panel.image = img 
panel.place(x=600, y=150)

uploadimage = Image.open("assets/upload.png")
upload = ImageTk.PhotoImage(uploadimage.resize((250,100)))
tk.Button(window, text = "upload",image = upload,command = open_img).place(x=150, y=150)

detectimage = Image.open("assets/detect.png")
detect = ImageTk.PhotoImage(detectimage.resize((250,100)))
tk.Button(window, text = "detect",image = detect,command = detects).place(x=150, y=390)

tk.Label(window, text="\n    OUTPUT\n",width=25,font=("Bauhaus 93", 20)).place(x=600, y=410)
tk.Label(window, text=" ",textvariable = output,font=("Bauhaus 93", 20)).place(x=600, y=410)

window.mainloop()
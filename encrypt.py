from PIL import Image
import numpy,random,sys
import tkinter as tk
from tkinter import filedialog
print ('-- Image Encryption and Decryption --')
print ('*************************************')
file1 = filedialog.askopenfile(mode='r', filetype=[('jpeg file', '*.jpeg')])
file_name = file1.name
img=Image.open(file_name)
#img.show()
arr=numpy.asarray(img)
arr1=arr.copy()
x,y,z=arr.shape
n=y-(random.randint(y//4,y//2))
n1=x-(random.randint(x//4,x//2))
m,m1=random.randint(1,10),random.randint(1,10)
b,c=random.randint(1,10),random.randint(1,10)
it=random.randint(50,200)
def flip():
    global x,b,n1
    for i in range(b,x-1,n1*200000):
        arr1[i:i+n1]=numpy.fliplr(arr1[i:i+n1])
def yflip():
    global y,n,b
    for i in range(b,y-1,n*200000):
        arr1[:,i:i+n]=numpy.fliplr(arr1[:,i:i+n])
print('')
for i in range(it):#encryption
    flip()
    c+=m
    yflip()
    b+=m1

    print ('\r{}'.format((i/it)*100),end='',flush=True)
    sys.stdout.flush()
print('')
#text encryption
li= [n,n1,m,m1,b,c,it]
print('Your key : ',' '.join(str(e) for e in li))
print ('*************************************')


enimg = Image.fromarray(numpy.uint8(arr1)).convert('RGB')
enimg.show()
enimg.save(r'sampleencrypt.png')

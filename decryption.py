from PIL import Image
import numpy,random
img=Image.open(r'sampleencrypt.png')
arr=numpy.asarray(img)
arr1=arr.copy()
x,y,z=arr.shape
#key
val = input("Enter your key: ")
li=val.split(' ')#enter key here
li1=[int(i) for i in li]
n,n1,m,m1,b,c,it=li1
def flip():
    global x,b,n1
    for i in range(b,x-1,n1*2):
        arr1[i:i+n1]=numpy.fliplr(arr1[i:i+n1])
def yflip():
    global y,n,b
    for i in range(b,y-1,n*2):
        arr1[:,i:i+n]=numpy.fliplr(arr1[:,i:i+n])
for i in range(it):#decryption
    b-=m1
    yflip()
    c-=m
    flip()
enimg = Image.fromarray(numpy.uint8(arr1)).convert('RGB')
enimg.show()
enimg.save(r'sampledecrypt.png')
from .st7567 import ST7567
import math
import random
import time

st7567 = ST7567()

def vLine(x):
    i=0
    while True:
        if(i==63):
            st7567.show()
            break
        st7567.set_pixel(x, i, 1)
        i=i+1
    
        
def hLine(y):
    i=0
    while True:
        if(i==127):
            st7567.show()
            break
        st7567.set_pixel(i, y, 1)
        i=i+1
        
def stairCase(x, y, w, h):
    isX=1
    while True:
        if(127-x-w<=0):
            i=x-1
            st7567.set_pixel(x, i, 1)
            i=i+1
            while True:
                if(i==127):
                    st7567.show()
                    break
        if(127-y-h<=0):
            i=y-1
            st7567.set_pixel(i, y, 1)
            i=i+1
            while True:
                if(i==63):
                    st7567.show()
                    break
        if(isX):
            i=x+w
            while True:
                if(i==w):
                    continue
                st7567.set_pixel(x, i ,1)
                i=i+1
        if(!isX):
            i=y+h
            while True:
                if(i==h):
                    continue
                st7567.set_pixel(i, y,1)
                i=i+1
                st7567.show()
                
def randomPoint(t):
    x = random.randrage(127)
    y = random.randrage(63)
    st7567.set_pixel(x, y, 1)
    time.sleep(t)
    st7567.clear()
    
def clearBacklight(r):
    st7567.set_all(255,0,0)
    st7567.show()
    

    
            
 
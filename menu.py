import Lab5Library
while True:
    print("1. vLine")    
    print("2. hLine")
    print("3. stairCase")
    print("4. randomPoint")
    print("5. claerBackLight")
    item = input ()
    if(item=="1"):
        vLine()
    
    if(item=="2"):
        hLine()    
    
    if(item=="3"):
        print("start point")
        sp = input()
        print("w")
        w = input()
        print("h")
        h = input()
        stairCase()
        
    if(item=="4"):
        print("time:")
        t = input()
        randomPoint()
        
    if(item=="5"):
        clearBackLightK()
        
    
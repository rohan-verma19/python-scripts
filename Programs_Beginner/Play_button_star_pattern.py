size = int(input("what is size?"))
if size >= 3:
    if size%2 == 0:
        size = (size+1)
    elif size%2 != 0:
        size = size
else:
    size = 3
           
for i in range(1,int(int(size+1)/2)+1):
    if i == 1:
        print("*")
    else:    
        print("*"," "*(i-2),"*",sep = "")
           
for t in range(int(int(size-1)/2),0,-1):
    if t == 1:
        print("*")
    else:    
        print("*"," "*(t-2),"*",sep = "")       


"""
**
* *
*  *
*   *  
*    *
*   *
*  * 
* *
**
"""

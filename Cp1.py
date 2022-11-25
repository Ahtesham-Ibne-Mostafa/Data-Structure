def shiftLeft( source, k):
    for j in range(0,k):
        for i in range(1,len(source)):
            source[i-1]=source[i]
            source[i]=0
    return source
    
source=[10,20,30,40,50,60]
k=int(input('Enter the number of cells to be shifted :'))
shiftLeft(source,k)
print(source)
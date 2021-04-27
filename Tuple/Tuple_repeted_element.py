a=(10,2,0,3,4,0,10,5,0,5)
print("Original tuple \n",a)
for i in a:
    if a.count(i) > 1:
        print(i," ")

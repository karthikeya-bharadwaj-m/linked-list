FP = float(input("enter final price:"))
D = float(input("enter discount between 0 and 100 percent"))
if (0<D<100):
    OP = FP/ (1-(D/100))
    print(OP)
else:
    print("NO")
    
    

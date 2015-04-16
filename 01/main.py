for i in range(1,10):
        print(" "*8*i,end="")
        for j in range(i,10):
            w=str.format("{0:1}*{1:1}={2:<4}",i,j,i*j)
            print(w,end="")
        print()

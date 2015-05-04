import math
class Ellipse:
    def Ellipse(self,a,b):
        return(math.pi*a*b)
class Square:
    def Square(self,c):
        return(c*c)
class Rectangle:
    def Rectangle(self,d,e):
        return d*e
class Circle:
    def Circle(self,f):
        return math.pi*f*f
class Myclass(Ellipse,Square,Rectangle,Circle):
    count=0
    def compute_area(self,shapes):
        q=[]
        p=Myclass()
        a=shapes
        b=a.split(',')
        i=0
        k=0
        while(i<len(b)):
            b[i]='p.'+b[i]
            if(ord(b[i][len(b[i])-1])>=48 and ord(b[i][len(b[i])-1])<=57):
                b[i]=b[i]+','+b[i+1]
                q.append(i+1)
                i=i+1
            i=i+1
        for j in q:
            del b[j-k]
            k=k+1
        for i in range(0,len(b)):
            exec('Myclass.count+='+b[i])
        return(Myclass.count)
p=Myclass()
print("总面积是：",p.compute_area(input("输入图形列表，如Ellipse(24,30),Square(10),Rectangle(4,3):")))

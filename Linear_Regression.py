import numpy as np
import matplotlib.pyplot as plt
a=list(map(float,input().split()))
b=list(map(float,input().split()))
l=len(a)
x=np.array(a)
y=np.array(b)
mean_x=np.mean(x)
mean_y=np.mean(y)
num=0
den=0


#applying formula
for i in range(l):
    num=num+(x[i]-mean_x)*(y[i]-mean_y)     #num=sum(x-mean(x))*sum(y-mean(y))
    den=den+(x[i]-mean_x)**2                #den=sum(x-mean(x))^2


#actual values
m=num/den                                # value of m
c=mean_y-(m*mean_x)                     # c=y-m*x
print("Values of m and c: ",m,c)



p=[]
#predicted values
for i in range(1,l+1):
    pr_y=m*i+c
    p.append(pr_y)
pr=np.array(p)
print("Predicted values: ",*pr)


#distance between actual and predicted values using R-Squared method
mean_pr=np.mean(pr)
rnum=0
rden=0
for i in range(l):
    rnum=rnum+(pr[i]-mean_pr)**2
    rden=rden+(y[i]-mean_y)**2
r=rnum/rden
print("R value:",round(r,2))             #print R value

#graph
plt.scatter(x,y)
plt.plot(x,pr,'g-')
plt.plot(4)
plt.xlabel('x')
plt.ylabel('y')
plt.title("Linear Regression")
plt.show()

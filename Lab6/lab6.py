
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
from numpy.polynomial.polynomial import polyfit
n1=np.array([17.5,22,29.5,44.5,64.5,80])
n2=np.array([38,36,24,20,18,28])
n=np.column_stack((n1,n2))
l=len(n1)
p=[0]*(l+1)
Lval=[]
Uval=[]
for i in range(l):
    print("i=",i)
    if(i==0):
        r=int((n1[0]+n1[1])/2)
        lower=n1[0]-(r-n1[0])
    else:
        lower=r+1
        r=n1[i]+(n1[i]-lower)
    Lval.append(lower)
    Uval.append(r)
    print("lower =",lower," right= ",r)
plt.scatter(n1,n2,s=20)
plt.title('Scatter plot')
plt.xlabel('Independent variable - age')
plt.ylabel('Dependent variablee - Deaths')
df = pd.DataFrame(n, columns = ['Age', 'Deaths']) 
age_sq=[]
death_sq=[]
xCrossY=[]
for i in range(l):
    age_sq.append(df['Age'][i]*df['Age'][i])
    death_sq.append(df['Deaths'][i]*df['Deaths'][i])
    xCrossY.append(df['Deaths'][i]*df['Age'][i])
df['lower']=Lval
df['upper']=Uval
df['Age_sq']=age_sq
df['Death_sq']=death_sq
df['xCrossY']=xCrossY
df=df[['Age','lower','upper','Deaths','Age_sq','Death_sq','xCrossY']]
s_age=sum(df['Age'])
s_deaths=sum(df['Deaths'])
s_age_sq=sum(df['Age_sq'])
s_xy=sum(df['xCrossY'])
b1=( s_xy - (s_age*s_deaths)/l ) / (s_age_sq  - (s_age*s_age)/l)
b0= ( s_deaths - (b1*s_age) )/l
print("b1=",b1)
print("b0=",b0)
y=b1*40 + b0
print(y)

y=b1*60 + b0
print(y)
plt.scatter(n1,n2,s=20)
plt.title('Scatter plot')
plt.xlabel('Independent variable - age')
plt.ylabel('Dependent variablee - Deaths')
x = n1
y = b1 * x + b0
b, m = polyfit(x, y, 1)
plt.plot(x, y, '.')
plt.plot(x, b + m * x, '-')
plt.show()
scipy.stats.pearsonr(n1,n2)



from math import sqrt
n,v,h=map(float,input('Введите длину нижнего и верхнего оснований и высоту:').split())
if n<=0 or v<=0 or h<=0:
    print('Ошибочные данные')
else:
    q=sqrt(3)/4
    sn=n*n*q
    sv=v*v*q
    V=1/3*h*(sn+sv+sqrt(sn*sv))
    ha=sqrt(h*h+(n-v)**2/12)
    Sp=1/2*ha*3*(n+v)
    print('Объем усеченной пирамиды:','{:7.3f}'.format(V))
    print('Площадь боковой поверхности усеченной пирамиды:','{:7.3f}'.format(Sp))

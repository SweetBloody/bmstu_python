from math import sqrt
a,b,c=map(float,input('Введите a,b,c:').split())
if a==0:
    if b==0:
        if c==0:
            print('x-любое')
        else:
            print('нет корней')
    else:
        x=-c/b
        print('Корень','{:7.3f}'.format(x))
else:
    D=b*b-4*a*c
    kD=sqrt(D)
    r=2*a
    if D>=0:
        if D==0:
            x=-b/r
            print('2 совпадающих корня равные','{:7.3f}'.format(x))
        else:
            x1=(-b+kD)/r
            x2=(-b-kD)/r
            print('Корни:','{:7.3f}{:7.3f}'.format(x1,x2))
    else:
        print('Нет действительных корней')

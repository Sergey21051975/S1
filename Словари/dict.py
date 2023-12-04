#создать-create
d={'a':1,12:21}
print(d)

d1=dict(asd=9,zxc='lk')

#update
d1['qwe']='wsx'
d1.update(er='re')
print(d1)

#clear
d1.clear()
print(d1)

#delete
del(d1)
#print(d1)

def di(**kwargs):
    return kwargs
print(di(ds=90,km='km'))

def da(*args):
    return args
print(da('sd',12,23))

lia=['qw',12,45,'asd']
lib=[34,65,'fd']
dic={k:v for k,v in zip(lia,lib)}
print(dic)
dic['gg']='uyt'
print(dic)
dic={v:k for k,v in dic.items()}#Меняем местами ключ и значение в словаре
print(dic)
print(dic.get(34))#возвращает значение ключа
print(type(dic.items()))

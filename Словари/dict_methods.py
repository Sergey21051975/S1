# Создать словарь
d={'a':'as',3:'fd'}
print(d.get(3))# вывод значения по ключу


al=[1,2,3,4,'asd'] #словарь из двух списков
alv=['q','wer','fff',4,5]
a={k:v for k,v in zip(al,alv)}
#print(a)

a=dict.fromkeys('1234567123',[])
#print(a)

b=['a','q','f','a','b']
c=set(b)#переводим список в множество
c=dict.fromkeys(c,0)
#print(c)
c['q']=9 #добавляем значение
#print(c)

keys={1,2,3,4,2,2}
value=[]
k=dict.fromkeys(keys,value)
value.append(55)
#print(k)


#dict.items() - возвращает пары (ключ, значение).
d=dict()
d['a']='asd'
d[12]=21
d['dfg']=345
print(d)
print(d.items())

#dict.keys() - возвращает ключи в словаре.
di={1:'qw',2:22,3:'fds'}
print(di.keys())

#dict.values() - возвращает значения в словаре.
print(di.values())

#dict.pop(key[, default]) - удаляет ключ и возвращает значение. 
#Если ключа нет, возвращает default (по умолчанию бросает исключение).
po={1:'ddd',2:'eee',3:234}
print(po.pop(1))


z1=[1,2,3,4,5,2,3]
z2=['a','s','d',444,555,222,333]
zd={k:v for k,v in zip(z1,z2)}
print(zd)

keys='zxcv'
value=['Z','X','C',777]
p=list(enumerate(keys))
print(type(p[2]))









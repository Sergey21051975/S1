#Напишите скрипт Python для сортировки
#(возрастания и убывания) словаря по значению.

adict={'a':2,'s':9,'d':5}
adict2=sorted(adict.items())
adict3=dict(adict2)
print(adict3)

#Напишите скрипт Python для добавления ключа в словарь.
a=dict()
a['qw']=34
a.update(rrr=56)
print(a)


#Напишите скрипт Python для объединения следующих словарей для создания нового.
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5: 50,6: 60}
dic4={**dic1,**dic2,**dic3}
print(dic4)

#Напишите скрипт Python, чтобы проверить, существует ли данный ключ в словаре.
ad={'a':2,'s':9,'d':5}
def ads(x):
    if x in ad:
        print(x,'yes')
    else:
        print('no')
ads('ka')
print(list(ad.values()))
    

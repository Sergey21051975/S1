adict={'a':22,'f':33,4:'55'}
adictk=adict.keys()
adictv=adict.values()
arev=reversed(adictk)                           #reversed()
arevval=reversed(adictv)
#print(arev,'\n',arevval)
adr=list(arev)                                  #list()
bdr=list(arevval)
#print(list(arev),'\n',list(arevval))
dz=zip(adr,bdr)                                 #zip()
dzl=list(dz)
print(dict(dzl))                                #dict()


asum=dict(q=2,w=5,e=7)
asumv=asum.values()
print(sum(asumv))                               #sum()
asumk=asum.keys()
print(len(asumk))                               #len()
print(type(asumk))                              #type()
print(dir(asumk))                               #dir()

x="String sdfg"
xl=(list(enumerate(x)))
print(xl)                                       #enumerate()
print(dict(xl))

                                                #lambda
f=lambda x,y: x*y
f1=f(5,8)
print('lambda',f1)

ftrue=lambda: True
print(ftrue())

li=[1,2,3,4,5]
limap=list(map(lambda x: x**2,li))              #map()
print(limap)

ls=[89,45,7,67]
ls1=sorted(ls)
print(ls1)
lstr='qwerqwre'
print(sorted(lstr,reverse=True))                #sorted()
dic={'a':23,'h':33,'b':'as'}
dics=sorted(dic.items(),reverse=True)           #reverse()
dicsd=dict(dics)
print(dicsd)

labs=[1,-3,5,-8,9]
print(sorted(labs,key=abs))                     #key=abs Сортировка списка по абсолютному значению





























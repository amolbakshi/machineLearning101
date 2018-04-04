s = "Hi there Sam!"
s2 = s.split(" ")
print(s2)
name = 'Earth'
dia = '1111'
print("The diameter of {name} is {dia} kilometers.".format(name=name,dia=dia))

lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(lst[3][1][2])

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
print(d.get('k1')[3].get('tricky')[3].get('target')[3])

def getDomain(str='test'):
    s=str.split('@')
    print(s[1])


getDomain('amol@bakshi.com')
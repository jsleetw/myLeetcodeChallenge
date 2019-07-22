dic = {'name': 'gg', 'gen': 'man'}
#for key, val in dic.items():
#    print(key, val)

a = [1, 2, 3, 4]
b = (10 * i for i in a)


def gerator():
    print('ok')
    yield 1
    print('next')
    yield 2

g = gerator()
#print(g)
#print(next(g))
#print(next(g))
#print(next(g))

#for i in g:
#    print(i)

def bar():
    print('before yield')
    count = yield 123
    print(count)
    yield 234
b = bar()

b.send(None)
b.send('abc')

from collections.abc import Iterable, Iterator

#print(isinstance([], Iterable))
#print(isinstance({}, Iterable))
#print(isinstance((), Iterable))
#print(isinstance('123', Iterable))
#print(isinstance(100,Iterable))

print(isinstance([], Iterator))
print(isinstance((), Iterator))
print(isinstance({}, Iterator))
print(isinstance('1111',Iterator))


## Extend

notas1 = [8, 10, 8.5]
notas2 = [8.3, 9, 7.5]

notas1.extend(notas2)

print(notas1)

## Slice

nums = list(range(5))

print(nums)
print(nums[:]) # do início ao fim
print(nums[2:]) # do 2o (incluso) até o fim
print(nums[:2]) # do início ao 2o (excluso)
print(nums[2:4]) # do 2o (incluso) ao 4o (excluso)
print(nums[:-1]) # do início ao último (excluso)
nums[2:4] = [8, 9] # atribuição
print(nums)

## List comprehension

L = [x**2 for x in range(1,7)]
print(L)

mixed = [1, 2, 'a', 3, 4.0]
mixed = [x**2 for x in mixed if type(x) != str]
print(mixed)

## List map

lista = ['b', 'n', 'n', 'd']
lista1 = list(map(lambda x: x + 'a', lista))
print(lista1)

## zip tuple

x = [1, 2, 3]
y = [4, 5, 6]
zipped = list(zip(x, y))
print(zipped)

## enumerate tuples

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
tuples = list(enumerate(seasons))

print(tuples)
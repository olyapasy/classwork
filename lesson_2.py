import string
import random
def chess_table():
    for i in range(1,8+1):
        for symbbol in 'ABCDEFGH':
            print(symbbol + str(i), end='\t')
        print()


chess_table()


lst = []

for i in range(1, 101):
    lst.append(i)

print(lst)

lst2 = [i for i in range(1, 101)]
print(lst2)

lst3 = [i**2 for i in range(1,101)]

print(lst3)

lst4 = [i**2
        for i in range(1, 101)
        if i % 5 == 0]


print(lst4)


text = 'По рзелульаттам илссеовадний одонго анлигйсокго унвиертисета, не иеемт занчнеия, в кокам пряокде рсапожолены ' \
       'бкувы в солве. Галвоне, чотбы преавя и пслоендяя бквуы блыи на мсете. Осатьлыне бкувы мгоут селдовтаь в ' \
       'плоонм бсепордяке, все-рвано ткест чтаитсея без побрелм. Пичрионй эгото ялвятеся то, что мы чиатем не кдаужю ' \
       'бкуву по отдльенотси, а все солво цликеом. '

zipped = [c for c in text if not (c in 'уеыаоэиюё')]
print(zipped)


alphabet = [chr(code) for code in range (ord('a'), ord('z')+1)]
print(''.join(alphabet))
print(string.ascii_lowercase)


my_digits = [str(code) for code in range(10)]
print(''.join(my_digits))
print(string.digits)



summ = sum(lst2)
print(summ)


print(max(lst2))
print(sum(lst2)/len(lst2))


print(sum([random.randint(10,20) for i in range(100)]))



lst_random = [random.randint(10,20) for i in range(100)]
print(sum(lst_random), lst_random)

lst5 = [1 for i in range(1,101) if i % 3 ==0]
print(sum(lst5), lst5)

lst6 = [5, 2, 3, 4, 1, 6][::-1]
num_of_swaps = sum([1 for idx, elem in enumerate(lst6) if idx+1 != elem])
print(num_of_swaps)


def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)

fact = factorial(10)
print(fact)
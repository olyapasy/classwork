import random
for i in range(1, 11):
    print(i)
    for j in range(1, 11):
        print("\t", j)


def print_cinema(rows=16,columns=5):
    for i in range(rows+1):
        print("Row %d:\t" % i, end=' ')
        for i in range(columns+1):
            print("%d:\t" % i, end=' ')

            is_vip_seat = (5 <= i <=10) and (10 <= j <= 15)
            if is_vip_seat:
                print('[%5s]' % j, end= '\t')
            else:
                print('%5s' % j, end='\t')

        print()


print_cinema(15,20)
print_cinema(3, 4)
print_cinema()


def count_table(rows = 10,columns = 10):
    for i in range(1, rows+1):
        for j in range(1, columns+1):
            print((i * j), end='\t')
        print()


count_table()


print('\n\n\n*********************************NESTED LISTS**********************************************')

matrix = [[1, 2, 3],
          [4,5,6],
          [7,8,9]]

print(matrix[0][0])
print(matrix[0][1])
print(matrix[0][2])


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' | ')
        print()


print_matrix(matrix)

def multiply_matrix(matrix,coeff):
    for i in range(len(matrix)):

        for j in range(len(matrix[i])):

            print(matrix[i][j]*coeff, end=' | ')
        print()

multiply_matrix(matrix, 10)
print_matrix(matrix)


def fill_matrix(matrix,lower_bound,upper_bound):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = random.randint(lower_bound,upper_bound)


fill_matrix(matrix,10,100)
print_matrix(matrix)

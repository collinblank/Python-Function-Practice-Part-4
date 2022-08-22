# Write a Python function called max_num()to find the maximum of three numbers.

def max_num(*number):
  max_number = 0
  for i in number:
    if i > max_number:
      max_number = i
  print(max_number)

#ANSWER
# max_num(8, 14, 3)

# Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(*multiply):
    product = 1
    for i in multiply:
        product = product * i
    return(product)
#ANSWER
# print(mult_list(8, 4, 3))


# Write a Python function called rev_string() to reverse a string.

def rev_string(string):
  return string[::-1]

#ANSWER
# print(rev_string('Collin'))


# Write a Python function called num_within() to check whether a number falls in a given range.
# Simple version
# def num_within(n):
#     if n in range(8, 10):
#       return True
#     else:
#       return False
# # ANSWER:
# # print(num_within(9))

def num_within(number, range_start, range_finish):
    return number in range(range_start, range_finish+1)
#ANSWER:
# print(num_within(10, 10, 10))




# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.

triangle = [[1], [1, 1]]
def pascal(n):
    #base case:
    if n < 1:
        print("print a valid number of rows")
    elif n == 1:
        print(triangle[0])
    else:
        row_number = 2
        while len(triangle) < n:
            row = []
            row_prev = triangle[row_number - 1]
            length = len(row_prev)+1
            for i in range(length):
                if i == 0:
                    row.append(1)
                elif i > 0 and i < length-1:
                    row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
                else:
                    row.append(1)
            triangle.append(row)
            row_number += 1

        for row in triangle:
            print(row)

# Answer:
# pascal(3)



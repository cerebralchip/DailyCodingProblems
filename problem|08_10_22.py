# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?

def product_of_all_except_i(arr):
    product = 1
    for i in arr:  # finds total product
        product *= i
    return [product/i for i in arr]  # applies division to each element


def product_except_i_no_division(arr):
    products = []
    for i in range(len(arr)):
        number = arr.pop(i)  # removes element at i
        product = 1
        for j in arr:  # finds product of all elements except i
            product *= j
        arr.insert(i, number)  # inserts that number back into the array
        products.append(product)  # adds product to list of products
    return products


print(product_except_i_no_division([3, 2, 1]))

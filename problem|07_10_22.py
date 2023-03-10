# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?
def add_up_to_k(numbers, k):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == k:
                return numbers[i], numbers[j]
    return False


numbers = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
k = 18

answer = add_up_to_k(numbers, k)
if answer:
    print("The numbers are: ", answer)
else:
    print("No two numbers in the list add up to", k)

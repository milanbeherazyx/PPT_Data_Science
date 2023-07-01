# Question No. -  1
# Write a Python program to reverse a string without using any built-in string reversal functions.

def reverse_string(string):
    return string[::-1]

# Question No. -  2
# Implement a function to check if a given string is a palindrome.

def is_palindrome(string):
    return string == string[::-1]

# Question No. -  3
# Write a program to find the largest element in a given list.

def find_largest_element(lst):
    return max(lst)

# Question No. -  4
# Implement a function to count the occurrence of each element in a list.

def count_occurrences(lst, element):
    return lst.count(element)

# Question No. -  5
# Write a Python program to find the second largest number in a list.

def find_second_largest(lst):
    sorted_lst = sorted(lst)
    return sorted_lst[-2]

# Question No. -  6
# Implement a function to remove duplicate elements from a list.

def remove_duplicates(lst):
    return list(set(lst))

# Question No. -  7
# Write a program to calculate the factorial of a given number.

def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

# Question No. -  8
# Implement a function to check if a given number is prime.

def is_prime(n):
    return False if n < 2 else all(n % i != 0 for i in range(2, int(n**0.5) + 1))

# Question No. -  9
# Write a Python program to sort a list of integers in ascending order.

def sort_list(lst):
    return sorted(lst)

# Question No. -  10
# Implement a function to find the sum of all numbers in a list.

def find_sum(lst):
    return sum(lst)

# Question No. -  11
# Write a program to find the common elements between two lists.

def find_common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

# Question No. -  12
# Implement a function to check if a given string is an anagram of another string.

def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

# Question No. -  13
# Write a Python program to generate all permutations of a given string.

def permutations(string):
    if len(string) == 1:
        return [string]
    perms = []
    for i in range(len(string)):
        char = string[i]
        remaining_string = string[:i] + string[i+1:]
        perms.extend(char + perm for perm in permutations(remaining_string))
    return perms

# Question No. -  14
# Implement a function to calculate the Fibonacci sequence up to a given number of terms.

def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        next_num = sequence[-1] + sequence[-2]
        sequence.append(next_num)
    return sequence

# Question No. -  15
# Write a program to find the median of a list of numbers.

def find_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    return (
        (sorted_lst[n // 2] + sorted_lst[(n // 2) - 1]) / 2
        if n % 2 == 0
        else sorted_lst[n // 2]
    )

# Question No. -  16
# Implement a function to check if a given list is sorted in non-decreasing order.

def is_sorted(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

# Question No. -  17
# Write a Python program to find the intersection of two lists.

def find_intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

# Question No. -  18
# Implement a function to find the maximum subarray sum in a given list.

def max_subarray_sum(lst):
    max_sum = current_sum = lst[0]
    for num in lst[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

# Question No. -  19
# Write a program to remove all vowels from a given string.

def remove_vowels(string):
    vowels = 'aeiouAEIOU'
    return ''.join(char for char in string if char not in vowels)

# Question No. -  20
# Implement a function to reverse the order of words in a given sentence.

def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])

# Question No. -  21
# Write a Python program to check if two strings are anagrams of each other.

def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

# Question No. -  22
# Implement a function to find the first non-repeating character in a string.

def find_first_non_repeating_char(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return next((char for char in string if char_count[char] == 1), None)

# Question No. -  23
# Write a program to find the prime factors of a given number.

def find_prime_factors(n):
    factors = []
    i = 2
    while i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        else:
            i += 1
    return factors

# Question No. -  24
# Implement a function to check if a given number is a power of two.

def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

# Question No. -  25
# Write a Python program to merge two sorted lists into a single sorted list.

def merge_sorted_lists(lst1, lst2):
    merged_list = []
    i, j = 0, 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] <= lst2[j]:
            merged_list.append(lst1[i])
            i += 1
        else:
            merged_list.append(lst2[j])
            j += 1
    merged_list.extend(lst1[i:])
    merged_list.extend(lst2[j:])
    return merged_list

# Question No. -  26
# Implement a function to find the mode of a list of numbers.

def find_mode(lst):
    num_count = {}
    for num in lst:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1
    max_count = max(num_count.values())
    return [num for num, count in num_count.items() if count == max_count]

# Question No. -  27
# Write a program to find the greatest common divisor (GCD) of two numbers.

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Question No. -  28
# Implement a function to calculate the square root of a given number.

def square_root(n):
    if n < 0:
        return "Invalid input"
    guess = n
    while True:
        new_guess = (guess + n/guess) / 2
        if abs(new_guess - guess) < 1e-6:
            return new_guess
        guess = new_guess

# Question No. -  29
# Write a Python program to check if a given string is a valid palindrome ignoring non-alphanumeric characters.

def is_valid_palindrome(string):
    alphanumeric_string = ''.join(char.lower() for char in string if char.isalnum())
    return alphanumeric_string == alphanumeric_string[::-1]

# Question No. -  30
# Implement a function to find the minimum element in a rotated sorted list.

def find_min_rotated(lst):
    low = 0
    high = len(lst) - 1
    while low < high:
        mid = (low + high) // 2
        if lst[mid] > lst[high]:
            low = mid + 1
        else:
            high = mid
    return lst[low]

# Question No. -  31
# Write a program to find the sum of all even numbers in a list.

def sum_of_even_numbers(lst):
    return sum(num for num in lst if num % 2 == 0)

# Question No. -  32
# Implement a function to calculate the power of a number using recursion.

def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent > 0:
        return base * power(base, exponent - 1)
    else:
        return 1 / (base * power(base, -exponent - 1))

# Question No. -  33
# Write a Python program to remove duplicates from a list while preserving the order.

def remove_duplicates_preserve_order(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst

# Question No. -  34
# Implement a function to find the longest common prefix among a list of strings.

def longest_common_prefix(strs):
    if not strs:
        return ""
    shortest_str = min(strs, key=len)
    for i, char in enumerate(shortest_str):
        if any(s[i] != char for s in strs):
            return shortest_str[:i]
    return shortest_str

# Question No. -  35
# Write a program to check if a given number is a perfect square.

def is_perfect_square(n):
    return False if n < 0 else int(n ** 0.5)**2 == n

# Question No. -  36
# Implement a function to calculate the product of all elements in a list.

def product_of_elements(lst):
    product = 1
    for num in lst:
        product *= num
    return product

# Question No. -  37
# Write a Python program to reverse the order of words in a sentence while preserving the word order.

def reverse_word_order(sentence):
    return ' '.join(sentence.split()[::-1])

# Question No. -  38
# Implement a function to find the missing number in a given list of consecutive numbers.

def find_missing_number(lst):
    n = len(lst) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(lst)
    return expected_sum - actual_sum

# Question No. -  39
# Write a program to find the sum of digits of a given number.

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

# Question No. -  40
# Implement a function to check if a given string is a valid palindrome considering case sensitivity.

def is_valid_palindrome_case_sensitive(string):
    return string == string[::-1]

# Question No. -  41
# Write a Python program to find the smallest missing positive integer in a list.

def find_smallest_missing_positive(lst):
    n = len(lst)
    for i in range(n):
        while 1 <= lst[i] <= n and lst[i] != lst[lst[i] - 1]:
            lst[lst[i] - 1], lst[i] = lst[i], lst[lst[i] - 1]
    return next((i + 1 for i in range(n) if lst[i] != i + 1), n + 1)

# Question No. -  42
# Implement a function to find the longest palindrome substring in a given string.

def longest_palindrome_substring(string):
    def expand_around_center(left, right):
        while left >= 0 and right < len(string) and string[left] == string[right]:
            left -= 1
            right += 1
        return string[left + 1:right]
    longest = ""
    for i in range(len(string)):
        odd_palindrome = expand_around_center(i, i)
        even_palindrome = expand_around_center(i, i + 1)
        if len(odd_palindrome) > len(longest):
            longest = odd_palindrome
        if len(even_palindrome) > len(longest):
            longest = even_palindrome
    return longest

# Question No. -  43
# Write a program to find the number of occurrences of a given element in a list.

def count_occurrences(lst, element):
    return lst.count(element)

# Question No. -  44
# Implement a function to check if a given number is a perfect number.

def is_perfect_number(n):
    if n < 2:
        return False
    factors = [1]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            factors.extend((i, n // i))
    return sum(factors) == n

# Question No. -  45
# Write a Python program to remove all duplicates from a string.

def remove_duplicates(string):
    return ''.join(set(string))

# Question No. -  46
# Implement a function to find the first missing positive integer in an unsorted list.

def find_first_missing_positive(lst):
    n = len(lst)
    for i in range(n):
        while 1 <= lst[i] <= n and lst[i] != lst[lst[i] - 1]:
            lst[lst[i] - 1], lst[i] = lst[i], lst[lst[i] - 1]
    return next((i + 1 for i in range(n) if lst[i] != i + 1), n + 1)

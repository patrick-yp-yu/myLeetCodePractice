# Given a string, find the frequencies of all the character.
# Method 1: 
def charFreq_sol1(inString: str):
    freq = {}
    for c in inString:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    return freq

# Method 2: Using dict.get()
def charFreq_sol2(inString: str):
    freq = {}
    for key in inString:
        freq[key] = freq.get(key, 0) + 1
        # The meansing is same as sol1
        # if find key, return (value + 1)
        # else, return (0 + 1 = 1)
    return freq

# Method 4: Using set() + Count():
# The count() is a built-in function in Python. 
# It will return the total count of a given element in a string.
def charFreq_sol3(inString: str):
    res = {c : inString.count(c) for c in set(inString)}  # dictionay {key : value }
    # The character c = {'H', 'd', 'l', 'o', '!', 'W', 'e', 'r', ' '}
    return res

# Method 4: Using collections.Counter()
import collections
def charFreq_sol4(inString: str):
    count = collections.Counter(inString)
    res1 = dict(count)     # Convert Counter type to dict
    return res1

# Method5:

print( charFreq_sol1("Hello World!"))
print( charFreq_sol2("Hello World!"))
print( charFreq_sol3("Hello World!"))
print( charFreq_sol4("Hello World!"))
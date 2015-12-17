sentence = "now is the time for all good people to come to the aid of their party"
words = sentence.split(' ')
# now sorting words in alphabetic order.
words = sorted(words)
print("Sentence in sorted order:\n")
print(words)
# creating a dictionary to store each word and its frequency. The key is the word and the value is the number.
numWords = {}

for i in range(0, len(words)):
    
    # if word is in the dictionary, we increase the count/frequency of the word by 1.
    if words[i] in numWords:
       
        numWords[words[i]] += 1
        
    else:
        
        numWords[words[i]] = 1
        
for key in numWords.keys():
    print(key, numWords[key])
    
# It is not possible to sort a dictionary, only to get a representation of a it that is sorted. Dictionaries are inherently order less, but other types, such as lists and tuples, are not. 
# So we need a sorted representation, which will be a list—probably a list of tuples.
        
# sort on value.
import operator
sorted_numWords = sorted(numWords.items(), key=operator.itemgetter(1))
print("Sorting dictionary by value:\n")
print(sorted_numWords)
print("\n")

#sort on key.
sorted_numWords = sorted(numWords.items(), key=operator.itemgetter(0))
print("Sorting dictionary by key:\n")
print(sorted_numWords)
print("\n")

# Below is another approach using collections, sorting on key.
import collections
sorted_numWords = collections.OrderedDict(sorted(numWords.items()))

for k, v in sorted_numWords.items():
    print(k, v)
    
print("Sorting dictionary by key:\n")
print(sorted_numWords)
print("\n")
    
# Other approaches using collections:
# a) dictionary sorted by key -- OrderedDict(sorted(d.items())
sorted_numWords = collections.OrderedDict(sorted(numWords.items(), key=lambda t: t[0]))

for k, v in sorted_numWords.items():
    print(k, v)

print("\n")
print("Sorting dictionary by key:\n")
print(sorted_numWords)
print("\n")

# b) dictionary sorted by value
sorted_numWords = collections.OrderedDict(sorted(numWords.items(), key=lambda t: t[1]))

for k, v in sorted_numWords.items():
    print(k, v)
    
print("\n")
print("Sorting dictionary by value:\n")
print(sorted_numWords)

# c) dictionary sorted by length of the key string
sorted_numWords = collections. OrderedDict(sorted(numWords.items(), key=lambda t: len(t[0])))

for k, v in sorted_numWords.items():
    print(k, v)
print("\n")    
print("Sorting dictionary by length of key string:\n")
print(sorted_numWords)
print("\n")

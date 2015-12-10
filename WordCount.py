from __future__ import division
from collections import defaultdict
from collections import Counter
# count lines, sentences, and words of a text file
# set all the counters to zero
lines, blanklines, sentences, words, uniqueWords = 0, 0, 0, 0, 0

print('-' * 50)
try:
    # use a text file
    filename = 'D:\LiClipse Workspace\PythonExamples\Othello.txt'
    textf = open(filename, 'r')
except IOError:
    print('Cannot open file %s for reading' % filename)
    import sys
    sys.exit(0)
#Reads one line at a time.
for line in textf:
    #Test to print line. It can be commented out.
    #print(line)
    lines += 1
  
    if line.startswith('\n'):
        blanklines += 1
    else:
        #Assume that each sentence ends with . or ! or ?
        #Count these characters.
        sentences += line.count('.') + line.count('!') + line.count('?')
    
        #Create a list of words.
        #Use None to split at any whitespace regardless of length.
        #So for instance double space counts as one space.
        tempwords = line.split(None)
        #Test to print - it can be commented out.
        #print(tempwords)
    
        #Word total count.
        words += len(tempwords)
    
        #Unique word total count.
        uniqueWords += len(set(tempwords))
    
    
textf.close()
print('-' * 50)
print("Lines                    : ", lines)
print("Blank Lines              : ", blanklines)
print("Sentences                : ", sentences)
print("Words                    : ", words)
print("Unique Words             : ", uniqueWords)
print("Average Sentence in Words: ", words/sentences)

#Optional console wait for keypress.
from msvcrt import getch
getch()

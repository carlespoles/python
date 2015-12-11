def countWords(words):
    if len(words) < 1:
        return 0
    else:
        return len(words[0]) + countWords(words[1:])
    
print(countWords("Welcome to Jamaica and have a nice day."))   

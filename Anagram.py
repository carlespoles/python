def check_anagram(w1, w2):
    list1 = []
    list2 = []
    for wd1 in w1:
        list1.append(wd1)

    for wd2 in w2:
        list2.append(wd2)

    list1.reverse()

    if list1 == list2:
        print("The words " + w1 + " and " + w2 + " are anagrams.")
    else:
        print("The words " + w1 + " and " + w2 + " are NOT anagrams.")

check_anagram("dog", "god")

def check_anagram(w1, w2):
    list1 = []
    list2 = []
    for wd1 in w1:
        list1.append(wd1)

    for wd2 in w2:
        list2.append(wd2)

    list1.reverse()

    if list1 == list2:
        return True
    else:
        return False


def list_anagram(item_list1, item_list2):
    list1 = []
    #Removing duplicates.
    item_list1 = list(set(item_list1))
    item_list2 = list(set(item_list2))

    for word1 in item_list1:
        for word2 in item_list2:
            if check_anagram(word1, word2):
                list1.append(word2)
                list1 = list((set(list1)))

    #print(list1)
    return list1


print(list_anagram(["dog", "star"], ["god", "rats"]))

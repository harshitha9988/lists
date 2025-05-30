def match_words(words):
    c=0
    a=[]
    for word in words:
        if len(word)>1 and word[0]== word[-1]:
            c+=1
            a.append(word)

    print("list of words with the first an last character same\n", a)
    return c

count=match_words(['abc','cfc', 'xyz', 'aba', '12221'])
print("The number of words having the same first and last character:", count)
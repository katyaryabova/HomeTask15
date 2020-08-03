list_count = {}
for word in input().split():
    list_count[word] = list_count.get(word, 0) + 1
    print(list_count[word] - 1, end=' ')

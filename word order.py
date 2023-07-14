n=int(input())
words={}
for i in range(n):
    word=input()
    br=1
    if word in words:
          words[word]=words[word]+1
    else:
        words[word]=br
print(len(words))
print(*list(words.values()))
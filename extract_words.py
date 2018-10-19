#!/usr/bin/python

gitwordsdb = open("gitworddb.txt",mode="r")
gitwords = gitwordsdb.readlines()
worddb = open("worddb.txt",mode="w")
words = []
for i in gitwords:
    if len(i.split(sep=" ")) >= 2:
        pass
    else:
        words.append(i)
        
for w in words:
    print((w.replace("/n","").replace("'","")),file=worddb)

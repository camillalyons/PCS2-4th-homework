from BKTree import BKtree, editDistanceFast
from anytree import Node

dictionaryList = []
with open('words.txt') as words:
    dictionary = words.readlines()
    for line in dictionary:
        line = line[:-2]
        dictionaryList.append(line)

def selectingWords(w):
    rightWords = []
    for word in dictionaryList:
        if len(word) == len(w):
            rightWords.append(word)
    return rightWords

def numberOfWordsFromDictionary(word):
    c = 0
    for el in dictionaryList:
        if len(word) == len(el):
            c += 1
    return c


def wordProblem(w,v):
    flag = 0
    dictList = selectingWords(w)
    dictIter = iter(dictList)
    tree = BKtree(dictIter, distance=editDistanceFast)

    c = numberOfWordsFromDictionary(w)

    words = tree.find(item = w, threshold = 1)

    w = Node(w)
    for el in words:
        el = Node(el, parent = w)

    for ww in words:
        if len(words) >= c:
            return w, 'and', v, 'are not equivalent words'
        newWords = tree.find(item = ww, threshold = 1)
        ww = Node(ww)
        for el in newWords:
            if flag == 0:
                el = Node(el, parent = ww)
                ww.parent = w
                if el.name == v and flag == 0:
                    return (el)
                    flag = 1
        if flag == 1:
            break
        for wo in newWords:
            if wo not in words:
                words.append(wo)


w = 'head'
v = 'tell'
print (wordProblem(w, v))



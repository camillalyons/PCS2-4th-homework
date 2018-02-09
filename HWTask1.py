from BKTree import BKtree, editDistanceFast
from anytree import Node, findall_by_attr

#getting all the words from the dictionary
dictionaryList = []
with open('words.txt') as words:
    dictionary = words.readlines()
    for line in dictionary:
        line = line[:-2]
        line.lower()
        dictionaryList.append(line)

#from all the words from the dictionary, we are picking only the ones with the same length as the starting word (w)
def selectingWords(w):
    rightWords = []
    for word in dictionaryList:
        if len(word) == len(w):
            rightWords.append(word)
    return set(rightWords)

#counting all the words of the right length
def numberOfWordsFromDictionary(word):
    return (len(rightwords))


def wordProblem(w,v):
    output = []
    flag = 0
    dictList = selectingWords(w)
    dictIter = iter(dictList)    #we need to make this an iterable for the bktree
    tree = BKtree(dictIter, distance=editDistanceFast)    #for a given word, w, the bktree returnes all the words from the dictionary with edit distance equal to 1

    c = numberOfWordsFromDictionary(w)    #the number of words of the right length

    words = [w]    #takes count of all the words
    w = Node(w)
    wordsInTheTree = [w]    #this list takes count of all the words in the tree

    for ww in words:
        if len(words) >= c:    #we have used up all the words from the dictoinary, so the 2 words are not equivalent
            return w, 'and', v, 'are not equivalent words'

        newWords = tree.find(item = ww, threshold = 1)    #this list containes all the words of editdistance 1 from the starting word
        father = findall_by_attr(w, ww)    #returnes a tuple with all the nodes that have the same name as the attribute we are seaching for
        father = father[0]    #we only need 1 node: this will be the parent of all the words in "newWords"
        for el in newWords:
            if flag == 0 and el not in wordsInTheTree:
                el = Node(el, parent = father)
                wordsInTheTree.append(str(el))
                if el.name == v and flag == 0:    #so we have found the final word
                    for x in el.path:    #appending all the nodes in the path of the final word
                        output.append(x.name)
                    for xx in output:
                        print (xx, end = ' ')
                    flag = 1
        if flag == 1:    #if we found the final word, we can break the program
            break

        for wo in newWords:
            if wo not in words:
                words.append(wo)



w = 'head'
v = 'tell'
wordProblem(w, v)

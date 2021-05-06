import urllib
import requests
import queue
def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    pass

def itemsToQueues(words,i):
    q = [None] * 256
    for j in range(0,256):
        q[j] = []
    for k in range(0,len(words)):
        index = len(words[k])-i-1
        if(index < 0):
            q[0].append(words[k])
        else:
            q[words[k][index]].append(words[k])
    return q

def queuesToArray(ques,numWords):
    c = []
    for i in range(0,len(ques)):
        for j in range(0, len(ques[i])):
            c.append(ques[i][j])
    return c

def radix_sort():
    lenest_word = calc_lenest_word()
    words = book_to_words()
    for i in range(0,lenest_word):
        c = itemsToQueues(words,i)
        words = queuesToArray(c,len(words))
    return words
def calc_lenest_word():
    maxlen = 1
    lst = book_to_words()
    for i in lst:
        if(len(i) > maxlen):
            maxlen = len(i)
    return maxlen
radix_sort()

import urllib
import requests
import queue
def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    pass

def counting_sort(words, k):
    len_words = len(words) 

    output = [None] * len_words

    count = [None] * 10

    for i in range(0, len_words):
        index = (words[i] / k)
        count[int(index % 10)] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]
    
    i = len_words - 1
    while i >= 0:
        index = (words[i] / k)
        output[count[int(index % 10)] - 1] = words[i]
        count[int(index % 10)] -= 1
        i -= 1
    i = 0

    for i in range(0, len(words)):
        words[i] = output[i]


def radix_sort(self,):
    lenest_word = calc_lenest_word()
    words = book_to_words()
    k = 1
    while lenest_word / k > 0:
        counting_sort(words,k)
        k *= 10

def calc_lenest_word():
    maxlen = 1
    lst = book_to_words()
    for i in lst:
        if(len(i) > maxlen):
            maxlen = len(i)
    return maxlen

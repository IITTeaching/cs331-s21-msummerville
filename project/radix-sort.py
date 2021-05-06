import urllib
import requests
import 
def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    pass

def radix_sort(self):
    len_word = calc_lenest_word()
    for i in range(0,len_word)
        
def calc_lenest_word():
    maxlen = 1
    lst = book_to_words()
    for i in lst:
        if(len(i) > maxlen):
            maxlen = len(i)
    return maxlen

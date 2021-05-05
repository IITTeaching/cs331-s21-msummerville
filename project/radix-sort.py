import urllib
import requests
setx PATH "%PATH%;C:\Python33\Scripts"
def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    pass

def radix_sort(self):
    pass 
def calc_word_lenest(self):
    pass
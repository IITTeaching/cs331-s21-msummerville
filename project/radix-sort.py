import urllib
import requests
import queue
def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    lst = radix_sort()
    proper = sorted(book_to_words())
    arr = []
    for i in range(len(lst)):
        arr.append(lst[i].decode("ascii"))
    return arr

def itemsToQueues(words,k,maxlen):
    q = [None] * 256
    for i in range(0,256):
        q[i] = []
    for j in range(0,len(words)):
        pos = get_pos(words[j], k, maxlen)
        q[pos].append(words[j])
    return q

def get_pos(word, k, maxlen):
    pos = maxlen - k - 1
    if pos >= len(word):
        return 0
    else:
        return word[pos]

def queuesToArray(queues,numWords):
    words = [ [] for i in range(numWords) ]
    index = 0
    for i in range(0, len(queues)):
        curque = queues[i]
        while len(curque) > 0:
            words[index] = curque.pop(0)
            index += 1
    return words

def radix_sort():
    lenest_word = calc_lenest_word()
    words = book_to_words()
    for i in range(0,lenest_word):
        words = queuesToArray(itemsToQueues(words,i,lenest_word),len(words))
    return words

def calc_lenest_word():
    maxlen = 1
    lst = book_to_words()
    for i in lst:
        if(len(i) > maxlen):
            maxlen = len(i)
    return maxlen

################################################################################
# TEST CASES
################################################################################

def test_book():
    arr = []
    words = book_to_words()
    for i in range(len(book_to_words())):
        arr.append(words[i].decode("ascii"))
    arr = sorted(arr)
    lst = radix_a_book()
    n = 0
    for i in range(len(arr)):
        if not arr[i]==lst[i]:
            print("Python Sort")
            print(arr[i])
            print()
            print("Radix Sort")
            print(lst[i])
            raise Exception
        n+=1
        print("Correct Comparisons = " + str(n))
    return True


def say_test(f):
    print(80 * "#" + "\n" + f.__name__ + "\n" + 80 * "#" + "\n")

def say_success():
    print("----> SUCCESS")

################################################################################
# MAIN
################################################################################
def main():
    for t in [test_book]:
        say_test(t)
        t()
        say_success()
    print(80 * "#" + "\nALL TEST CASES FINISHED SUCCESSFULLY!\n" + 80 * "#")

if __name__ == '__main__':
    main()

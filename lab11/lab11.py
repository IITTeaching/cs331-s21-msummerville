from unittest import TestCase
import random

def quicksort(lst,pivot_fn):
    qsort(lst,0,len(lst) - 1,pivot_fn)

def qsort(lst,low,high,pivot_fn):
    ### BEGIN SOLUTION
    if(high>low):
        var=pivot_fn(lst,low,high)-1
        qsort(lst,low,var,pivot_fn)
        qsort(lst,var+2,high,pivot_fn)
    ### END SOLUTION

def pivot_first(lst,low,high):
    ### BEGIN SOLUTION
    var=lst[low]
    i=high
    j=high
    while(i>low):
        if(var<lst[i]):
            temp=lst[j]
            lst[j]=lst[i]
            lst[i]=temp
            j-=1
        i-=1
    temp=lst[low]
    lst[low]=lst[j]
    lst[j]=temp
    return j
    ### END SOLUTION

def pivot_random(lst,low,high):
    ### BEGIN SOLUTION
    rnd = random.randint(low, high)
    var=lst[rnd]
    temp=lst[rnd]
    lst[rnd]=lst[low]
    lst[low]=temp
    i=high
    j=high
    while(i>low):
        if(var<lst[i]):
            temp=lst[j]
            lst[j]=lst[i]
            lst[i]=temp
            j-=1
        i-=1
    temp=lst[low]
    lst[low]=lst[j]
    lst[j]=temp
    return j
    ### END SOLUTION

def pivot_median_of_three(lst,low,high):
    ### BEGIN SOLUTION
    med = 0
    if((lst[low]>lst[(low+high)//2] and lst[low]<lst[high]) or (lst[low]<lst[(low+high)//2] and lst[low]>lst[high])):
        med=lst[low]
    elif((lst[(low+high)//2]>lst[low] and lst[(low+high)//2]<lst[high]) or (lst[(low+high)//2]<lst[low] and lst[(low+high)//2]>lst[high])):
        med=lst[(low+high)//2]
    else:
        med=lst[high]
    var = lst[med]
    temp=lst[med]
    lst[med]=lst[low]
    lst[low]=temp
    i=high
    j=high
    while(i>low):
        if(var<lst[i]):
            temp=lst[j]
            lst[j]=lst[i]
            lst[i]=temp
            j-=1
        i-=1
    temp=lst[low]
    lst[low]=lst[j]
    lst[j]=temp
    return j
    ### END SOLUTION

################################################################################
# TEST CASES
################################################################################
def randomize_list(size):
    lst = list(range(0,size))
    for i in range(0,size):
        l = random.randrange(0,size)
        r = random.randrange(0,size)
        lst[l], lst[r] = lst[r], lst[l]
    return lst

def test_lists_with_pfn(pfn):
    lstsize = 20
    tc = TestCase()
    exp = list(range(0,lstsize))

    lst = list(range(0,lstsize))
    quicksort(lst, pivot_first)
    tc.assertEqual(lst,exp)

    lst = list(reversed(range(0,lstsize)))
    quicksort(lst, pivot_first)
    tc.assertEqual(lst,exp)

    for i in range(0,100):
        lst = randomize_list(lstsize)
        quicksort(lst, pfn)
        tc.assertEqual(lst,exp)

# 30 points
def test_first():
    test_lists_with_pfn(pivot_first)

# 30 points
def test_random():
    test_lists_with_pfn(pivot_random)

# 40 points
def test_median():
    test_lists_with_pfn(pivot_median_of_three)

################################################################################
# TEST HELPERS
################################################################################
def say_test(f):
    print(80 * "#" + "\n" + f.__name__ + "\n" + 80 * "#" + "\n")

def say_success():
    print("----> SUCCESS")

################################################################################
# MAIN
################################################################################
def main():
    for t in [test_first,
              test_random,
              test_median]:
        say_test(t)
        t()
        say_success()
    print(80 * "#" + "\nALL TEST CASES FINISHED SUCCESSFULLY!\n" + 80 * "#")

if __name__ == '__main__':
    main()

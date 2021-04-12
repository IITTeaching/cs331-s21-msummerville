from unittest import TestCase
import random
import functools

################################################################################
# 1. IMPLEMENT THIS HEAP
################################################################################
class Heap:
    def __init__(self, key=lambda x:x):
        self.data = []
        self.key  = key

    @staticmethod
    def _parent(idx):
        return (idx-1)//2

    @staticmethod
    def _left(idx):
        return idx*2+1

    @staticmethod
    def _right(idx):
        return idx*2+2

    def heapify(self, idx=0):
        ### BEGIN SOLUTION
        while(self._left(idx) < len(self.data)):
            if(self._right(idx) < len(self.data) and self.key(self.data[self._right(idx)]) > self.key(self.data[self._left(idx)]) and self.key(self.data[self._right(idx)]) > self.key(self.data[idx])):
                temp = self.data[self._right(idx)]
                self.data[self._right(idx)] = self.data[idx]
                self.data[idx] = temp
                idx = self._right(idx)
            elif(self.key(self.data[self._left(idx)]) > self.key(self.data[idx])):
                temp = self.data[self._left(idx)]
                self.data[self._left(idx)] = self.data[idx]
                self.data[idx] = temp
                idx = self._left(idx)
            else:
                break
        ### END SOLUTION

    def add(self, x):
        ### BEGIN SOLUTION
        self.data.append(x)
        e = len(self.data) - 1
        while(self._parent(e) >= 0 and self.key(self.data[e]) > self.key(self.data[self._parent(e)])):
            temp = self.data[self._parent(e)]
            self.data[self._parent(e)] = self.data[e]
            self.data[e] = temp
            e = self._parent(e)
        ### END SOLUTION

    def peek(self):
        return self.data[0]

    def pop(self):
        ret = self.data[0]
        self.data[0] = self.data[len(self.data)-1]
        del self.data[len(self.data)-1]
        self.heapify()
        return ret

    def __iter__(self):
        return self.data.__iter__()

    def __bool__(self):
        return len(self.data) > 0

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return repr(self.data)

################################################################################
# 1. IMPLEMENT THIS HEAP
################################################################################

# (6 point)
def test_key_heap_1():
    from unittest import TestCase
    import random

    tc = TestCase()
    h = Heap()

    random.seed(0)
    for _ in range(10):
        h.add(random.randrange(100))

    tc.assertEqual(h.data, [97, 61, 65, 49, 51, 53, 62, 5, 38, 33])

# (6 point)
def test_key_heap_2():
    tc = TestCase()
    h = Heap(lambda x:-x)

    random.seed(0)
    for _ in range(10):
        h.add(random.randrange(100))

    tc.assertEqual(h.data, [5, 33, 53, 38, 49, 65, 62, 97, 51, 61])

# (6 points)
def test_key_heap_3():
    tc = TestCase()
    h = Heap(lambda s:len(s))

    h.add('hello')
    h.add('hi')
    h.add('abracadabra')
    h.add('supercalifragilisticexpialidocious')
    h.add('0')

    tc.assertEqual(h.data,
                   ['supercalifragilisticexpialidocious', 'abracadabra', 'hello', 'hi', '0'])

# (6 points)
def test_key_heap_4():
    tc = TestCase()
    h = Heap()

    random.seed(0)
    lst = list(range(-1000, 1000))
    random.shuffle(lst)

    for x in lst:
        h.add(x)

    for x in range(999, -1000, -1):
        tc.assertEqual(x, h.pop())

# (6 points)
def test_key_heap_5():
    tc = TestCase()
    h = Heap(key=lambda x:abs(x))

    random.seed(0)
    lst = list(range(-1000, 1000, 3))
    random.shuffle(lst)

    for x in lst:
        h.add(x)

    for x in reversed(sorted(range(-1000, 1000, 3), key=lambda x:abs(x))):
        tc.assertEqual(x, h.pop())

################################################################################
# 2. MEDIAN
################################################################################
def running_medians(iterable):
    ### BEGIN SOLUTION
    minHeap = Heap(lambda x:-x) 
    maxHeap = Heap(lambda x:x)
    medians = [iterable[0]]
    val = iterable[0]
    median = iterable[0]
    for i in range(1,len(iterable)):
        if(val > iterable[i]):
            if(len(maxHeap.data) > len(minHeap.data)):
                maxHeap.add(iterable[i])
                minHeap.add(val)
                zit = maxHeap.pop()
                val = zit
            else:
                maxHeap.add(iterable[i])
        else:
            if(len(maxHeap.data) < len(minHeap.data)):
                minHeap.add(iterable[i])
                maxHeap.add(val)
                zit = minHeap.pop()
                val = zit  
            else:
                minHeap.add(iterable[i])
        if(len(maxHeap) > len(minHeap)):
            median = (maxHeap.peek() + val) / 2
        elif(len(minHeap) > len(maxHeap)):
            median = (minHeap.peek() + val) / 2
        else:
            median = val
        medians.append(median)
    return medians
    ### END SOLUTION

################################################################################
# TESTS
################################################################################
def running_medians_naive(iterable):
    values = []
    medians = []
    for i, x in enumerate(iterable):
        values.append(x)
        values.sort()
        if i%2 == 0:
            medians.append(values[i//2])
        else:
            medians.append((values[i//2] + values[i//2+1]) / 2)
    return medians

# (13 points)
def test_median_1():
    tc = TestCase()
    tc.assertEqual([3, 2.0, 3, 6.0, 9], running_medians([3, 1, 9, 25, 12]))

# (13 points)
def test_median_2():
    tc = TestCase()
    vals = [random.randrange(10000) for _ in range(1000)]
    tc.assertEqual(running_medians_naive(vals), running_medians(vals))

# MUST COMPLETE IN UNDER 10 seconds!
# (14 points)
def test_median_3():
    tc = TestCase()
    vals = [random.randrange(100000) for _ in range(100001)]
    m_mid   = sorted(vals[:50001])[50001//2]
    m_final = sorted(vals)[len(vals)//2]
    running = running_medians(vals)
    tc.assertEqual(m_mid, running[50000])
    tc.assertEqual(m_final, running[-1])

################################################################################
# 3. TOP-K
################################################################################
def topk(items, k, keyf):
    ### BEGIN SOLUTION
    heap = Heap(lambda x:keyf(x)*-1)
    for i in range(0,k):
        heap.add(items[i])
    if(len(items) > k):
        for j in range(k,len(items)):
            if(keyf(items[j]) > keyf(heap.peek())):
                heap.add(items[j])
                heap.pop()
    newlist = [None]*k
    for g in range(0,k):
        newlist[k-g-1] = heap.pop()
    return newlist
    ### END SOLUTION

################################################################################
# TESTS
################################################################################
def get_age(s):
    return s[1]

def naive_topk(l,k,keyf):
    revkey = lambda x: keyf(x) * -1
    return sorted(l, key=revkey)[0:k]

# (30 points)
def test_topk_students():
    tc = TestCase()
    students = [ ('Peter', 33), ('Bob', 23), ('Alice', 21), ('Gertrud', 53) ]

    tc.assertEqual(naive_topk(students, 2, get_age),
                   topk(students, 2, get_age))

    tc.assertEqual(naive_topk(students, 1, get_age),
                   topk(students, 1, get_age))

    tc.assertEqual(naive_topk(students, 3, get_age),
                   topk(students, 3, get_age))

################################################################################
# TEST HELPERS
################################################################################
def say_test(f):
    print(80 * "*" + "\n" + f.__name__)

def say_success():
    print("SUCCESS")

################################################################################
# MAIN
################################################################################
def main():
    for t in [test_key_heap_1,
              test_key_heap_2,
              test_key_heap_3,
              test_key_heap_4,
              test_key_heap_5,
              test_median_1,
              test_median_2,
              test_median_3,
              test_topk_students
              ]:
        say_test(t)
        t()
        say_success()

if __name__ == '__main__':
    main()

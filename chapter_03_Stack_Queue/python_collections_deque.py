from collections import deque
# import threading

# A deque is a double-ended queue. It can be used to add or remove elements from both ends.

# initialize with append, appendleft, extend, extendleft,
# count('e'), index('e', range)
# remove('e'), clear(), insert(i,x)
# ****reverse, rotate(n=1/-1)****

deque_test1 = deque()

deque_test1.append(1)

deque_test1.append('dfcv')

deque_test1.appendleft(True)

print(deque_test1)

deque_test1.clear()

print(deque_test1)

deque_test1.extendleft('1234')

deque_test1.pop()

deque_test1.popleft()

deque_test1.reverse()

deque_test1.append('4')

deque_test1.appendleft('1')

#deque_test1.remove('1')

print(deque_test1)

print(deque_test1.index('1'))

deque_test1.rotate(2)

print(deque_test1)
print(deque_test1.index('1'))



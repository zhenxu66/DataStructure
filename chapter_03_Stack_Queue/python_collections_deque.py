from collections import deque

# A deque is a double-ended queue. It can be used to add or remove elements from both ends.

deque_test1 = deque()

deque_test1.append(1)

deque_test1.append('dfcv')

print(deque_test1)

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

deque_test1.rotate(2)

print(deque_test1)



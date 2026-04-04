# Problem Link : https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true

# Note that you should use Python 2 as interprter for this problem as hash() function is used in this problem which is not available in Python 3.
if __name__ == '__main__':
  n = int(raw_input())
  integer_list = map(int, raw_input().split())
  t=tuple(integer_list)
  print hash(t)
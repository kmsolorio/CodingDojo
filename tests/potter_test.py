from nose.tools import *
from katas.potter import *

def basket():
  return [{'book': 1, 'count':3}, {'book':2, 'count':1}, {'book': 4, 'count': 2}]

def test_creates_new_potter_with_basket():
  p = Potter(basket())
  assert(p.basket == basket())

def test_creates_book_sets_on_initialize():
  p = Potter(basket())
  assert_equals(p.book_sets, [ [1, 2, 4], [1, 4], [1] ])

def test_total():
  p = Potter(basket())
  assert(p.total() > 0)

def test_total_with_one_book():
  p = Potter([{'book': 1, 'count': 1}])
  assert(p.total() is 8)

def test_total_with_two_of_the_same_book():
  p = Potter([{'book': 1, 'count': 2}])
  assert(p.total() is 16)

def test_total_with_two_different_books():
  p = Potter([{'book': 1, 'count': 1}, {'book':2, 'count':1}])
  assert(p.total() == 14.40)

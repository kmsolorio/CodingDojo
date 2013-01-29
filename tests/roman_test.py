from nose.tools import *
from katas.roman import *

def test_roman_numeral_for_9():
  numeral = RomanNumeral(9).convert()
  assert_equal(numeral, "IX")

def test_roman_numeral_for_10():
  numeral = RomanNumeral(10).convert()
  assert_equal(numeral, "X")

def test_roman_numeral_for_28():
  numeral = RomanNumeral(28).convert()
  assert_equal(numeral, "XXVIII")

def test_roman_numeral_for_147():
  numeral = RomanNumeral(147).convert()
  assert_equal(numeral, "CXLVII")

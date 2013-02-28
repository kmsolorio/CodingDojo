class RomanNumeral(object):

  TH = { 1 : "M", 2 : "MM", 3 : "MMM" }
  H =  { 1 : "C", 2 : "CC", 3 : "CCC", 4 : "CD", 5 : "D", 6 : "DC", 7 : "DCC", 8 : "DCCC", 9 : "CM" }
  T =  { 1 : "X", 2 : "XX", 3 : "XXX", 4 : "XL", 5 : "L", 6 : "LX", 7 : "LXX", 8 : "LXXX", 9 : "XC" }
  O =  { 1 : "I", 2 : "II", 3 : "III", 4 : "IV", 5 : "V", 6 : "VI", 7 : "VII", 8 : "VIII", 9 : "IX" }

  Denominations = {
    1000 : TH,
    100  : H,
    10   : T,
    1    : O
  }

  def __init__(self, n):
    self.n = n
    self.orignial = n
    self.numeral = ""

  def convert(self):
    self._set_thousands()
    self._set_hundreds()
    self._set_tens()
    self._set_ones()
    return self.numeral

  def _set_thousands(self):
    self._convert(1000)

  def _set_hundreds(self):
    self._convert(100)

  def _set_tens(self):
    self._convert(10)

  def _set_ones(self):
    self._convert(1)

  def _convert(self, denomination):
    if self.n >= denomination:
      num = self.n / denomination
      self.n -= num * denomination
      self.numeral += RomanNumeral.Denominations[denomination][num]
    else:
      pass


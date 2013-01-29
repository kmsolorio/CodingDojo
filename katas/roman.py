class RomanNumeral(object):
  TH = { 1 : "M", 2 : "MM", 3 : "MMM" }
  H =  { 1 : "C", 2 : "CC", 3 : "CCC", 4 : "CD", 5 : "D", 6 : "DC", 7 : "DCC", 8 : "DCCC", 9 : "CM" }
  T =  { 1 : "X", 2 : "XX", 3 : "XXX", 4 : "XL", 5 : "L", 6 : "LX", 7 : "LXX", 8 : "LXXX", 9 : "XC" }
  O =  { 1 : "I", 2 : "II", 3 : "III", 4 : "IV", 5 : "V", 6 : "VI", 7 : "VII", 8 : "VIII", 9 : "IX" }

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
    if self.n >= 1000:
      t = self.n / 1000
      self.n -= t * 1000
      self.numeral += RomanNumeral.TH[t]
    else:
      pass

  def _set_hundreds(self):
    if self.n >= 100:
      h = self.n / 100
      self.n -= h * 100
      self.numeral += RomanNumeral.H[h]
    else:
      pass

  def _set_tens(self):
    if self.n >= 10:
      t = self.n / 10
      self.n -= t * 10
      self.numeral += RomanNumeral.T[t]
    else:
      pass

  def _set_ones(self):
    if self.n:
      self.numeral += RomanNumeral.O[self.n]
    else:
      pass



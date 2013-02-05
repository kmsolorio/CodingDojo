class Potter(object):

  value = 8
  discount = {1: 0, 2 : 0.10, 3 : 0.15, 4: 0.20, 5: 0.25 }

  def __init__(self, basket):
    self.basket = basket
    self._create_sets()
    self._set_totals()

  def total(self):
    return sum(self.book_set_values)

  def _create_sets(self):
    self._book_sets()
    for book in self.basket:
      for i in range(0,book['count']):
        self.book_sets[i].append(book['book'])

  def _book_sets(self):
    book_sets = []
    number_of_sets = max(self.basket, key = lambda item: item['count'])['count']
    for i in range(0, number_of_sets):
      book_sets.append([])
    self.book_sets = book_sets

  def _set_totals(self):
    totals = []
    for set in self.book_sets:
      book_count = len(set)
      discount = Potter.value * book_count * Potter.discount[book_count]
      totals.append((Potter.value * book_count) - discount)
    self.book_set_values = totals





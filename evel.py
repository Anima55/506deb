class Board:
	def __init__(self, sizes: Iterable[int]):
		val = self.get_empty_cell_value()
		self.cells = ?

	def __getitem__(self, idx: Iterable[int]):
		pass

	def __setitem__(self, idx: Iterable[int], val):
		pass


	@classmethod
	def get_empty_cell_value(cls):
		return None
    
from collections import defaultdict

class MultiMap:
	def __init__(self):
		self.grouped = defaultdict(list)

	def __str__(self):
		return ";".join(str(item) for item in self.grouped)

	def set_val(self, key, val):
		self.grouped[key].append(val)

	def get_val(self, key):
		found_key = False
		print(self.grouped)
		for index, record in enumerate(self.grouped.items()):
			record_key, record_val = record

			if record_key == key:
				found_key = True
				break
		if found_key:
			return (f"{record_key} - {record_val}")		
		else:
			return "No record found"

	def delete_val(self, key):
		d = self.grouped[key]
		print('d++',self.grouped.keys())

		found_key = False
		for index, record in enumerate(self.grouped.items()):
			print('record++', record)
			record_key, record_val = record

			if record_key == key:
				found_key = True
				break

		if found_key:
			del self.grouped[index]
			# self.grouped.items().pop(index)
		else:
			return "No record found"

m = MultiMap()
m.set_val('A', 10)
m.set_val('B', 4)
m.set_val('A', [5,6,7])
m.set_val('C', 7)
m.set_val('B', 1)

print(m.get_val('C'))
print(m)
m.delete_val('A')
print(m)

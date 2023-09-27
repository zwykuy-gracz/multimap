from collections import defaultdict

class MultiMap:
	def __init__(self, hash_size):
		self.hash_size = hash_size
		self.grouped = self.create_grouped_data()

	def __str__(self):
		return ";".join(str(item) for item in self.grouped)

	def create_grouped_data(self):
		grouped_data = defaultdict(list)
		return grouped_data

	def set_val(self, key, val):
		hashed_key = hash(key) % self.hash_size

		bucket = self.grouped[hashed_key]

		found_key = False
		for index, record in enumerate(bucket):
			record_key, record_val = record
			
			if record_key == key:
				found_key = True
				break

		if found_key:
			bucket[index] = (key, val)
		else:
			bucket.append((key, val))

	def get_val(self, key):
		hashed_key = hash(key) % self.hash_size
		
		bucket = self.grouped[hashed_key]

		found_key = False
		for index, record in enumerate(bucket):
			record_key, record_val = record
			
			if record_key == key:
				found_key = True
				break

		if found_key:
			return record_val
		else:
			return "No record found"

	def delete_val(self, key):
		hashed_key = hash(key) % self.hash_size

		bucket = self.grouped[hashed_key]

		found_key = False
		for index, record in enumerate(bucket):
			record_key, record_val = record
			
			if record_key == key:
				found_key = True
				break
		
		if found_key:
			bucket.pop(index)
		return

m = MultiMap(70)
m.set_val('A', 10)
m.set_val('B', 4)
m.set_val('A', [5,6,7])
m.set_val('C', 7)
m.set_val('B', 1)

print(m.get_val('A'))
print(m)
m.delete_val('C')
print(m)
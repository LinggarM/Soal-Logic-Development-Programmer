def alphabet_count(text):

	# Inisialisasi variable
	alphabet_counts = {}
	
	# Looping pada variable "text"
	for char in text:
		if char.isalpha():
			if char in alphabet_counts:
				alphabet_counts[char] += 1
			else:
				alphabet_counts[char] = 1

	# Membuat alphabet_list
	alphabet_list = []
	for i in range(65, 91):
		alphabet_list.append(chr(i))
		alphabet_list.append(chr(i + 32))

	# Filter alphabet dari key alphabet_counts
	filtered_list = [element for element in alphabet_list if element in list(alphabet_counts.keys())]

	# Sort key tiap alphabet
	sorted_counts = {j: alphabet_counts[j] for j in filtered_list}
	
	# Mengembalikan hasil
	return sorted_counts

# Contoh implementasi fungsi
text = "Hello World"
alphabet_counts = alphabet_count(text)
print(alphabet_counts)

# Contoh implementasi fungsi
text = "Bismillah"
alphabet_counts = alphabet_count(text)
print(alphabet_counts)

# Contoh implementasi fungsi
text = "MasyaAllah"
alphabet_counts = alphabet_count(text)
print(alphabet_counts)
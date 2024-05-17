def pattern_count(teks, pattern):
	
	# Inisialisasi variable
	count = 0
	
	# Looping pada variable "teks"
	for i in range(len(teks) - len(pattern) + 1):
		if teks[i:i+len(pattern)] == pattern:
			count += 1
	
	# Special case: Jika pattern kosong, maka count = 0
	if pattern == "":
		count = 0

	# Mengembalikan hasil
	return count

# Contoh implementasi fungsi
teks = "palindrom"
pattern = "ind"
print(pattern_count(teks, pattern))

teks = "abakadabra"
pattern = "ab"
print(pattern_count(teks, pattern))

teks = "hello"
pattern = ""
print(pattern_count(teks, pattern))

teks = "ababab"
pattern = "aba"
print(pattern_count(teks, pattern))

teks = "aaaaaa"
pattern = "aa"
print(pattern_count(teks, pattern))

teks = "hell"
pattern = "hello"
print(pattern_count(teks, pattern))
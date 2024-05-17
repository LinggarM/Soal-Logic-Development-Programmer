def sorting_array(arr_abjad_angka):
	
	# Inisialisasi variable
	arr_abjad = []
	arr_angka = []
	arr_sorted = []

	# Memisahkan abjad dan angka
	for i in arr_abjad_angka:
		if isinstance(i, str):
			arr_abjad.append(i)
		elif isinstance(i, int):
			arr_angka.append(i)

	# Sorting list abjad dan list angka
	arr_abjad.sort()
	arr_angka.sort()
	
	# Menggabungkan list abjad dan list angka
	arr_sorted = arr_abjad + arr_angka
	
	# Mengembalikan nilai
	return arr_sorted

# Contoh implementasi fungsi
arr_abjad_angka = [12,9,30,"A","M",99,82,"J","N","B"]
print(sorting_array(arr_abjad_angka))
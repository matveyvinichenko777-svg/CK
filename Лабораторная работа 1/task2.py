disk_size = 1.44

pages = 100
lines = 50
chars = 25
bytes_per_char  = 4

total_chars = pages * lines * chars
book_size = total_chars * bytes_per_char
disk_size_byte = disk_size * 1024 * 1024
books_count = int(disk_size_byte / book_size)

print("Количество книг, помещающихся на дискету:", books_count)

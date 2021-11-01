for hash in range(1,11):
	print("#" * hash)

hash = 1
while hash < 11:
	print("#" * hash)
	hash += 1
	
# Without string multiplication - ugly solution
	
for hash in range(1,11):
	count = 1
	hashes = ""
	while count <= hash:
		hashes += "#"
		count += 1
	print(hashes)
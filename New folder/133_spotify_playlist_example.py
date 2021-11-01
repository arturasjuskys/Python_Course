playlist = {
	"Name of the Playlist": "Patagonia Bus",
	"Creator": "Colt",
	"Songs": [
		{
		"Song Name": "title1",
		"Artist": ["artist1", "artist2"],
		"Album": "title1",
		"Duration": 2.5
		},
		{
		"Song Name": "title2",
		"Artist": ["artist1"],
		"Album": "title2",
		"Duration": 5.1
		},
		{
		"Song Name": "title3",
		"Artist": ["artist12", "artist27", "artist23"],
		"Album": "title3",
		"Duration": 3.0
		}
	]
}

total_length = 0
for song in playlist["Songs"]:
	total_length += song["Duration"]
print(total_length)

for song in playlist["Songs"]:
	print(song["Song Name"])
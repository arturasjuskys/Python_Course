#	This example will take fighters.cvs and will creater fighters3.cvs with height changed from cm to inch

def cm_to_in(cm):

	return round(float(cm) * 0.393701, 2)
with open("fighters.csv") as file:
	from csv import DictReader, DictWriter
	csv_reader = DictReader(file)
	fighters = list(csv_reader)
with open("fighters3.csv", "w") as file:
	from csv import DictReader, DictWriter
	headers = ("Name", "Country", "Height")    #    <<<===    here we change from Height (in cm) to just Height in new file
	csv_writer = DictWriter(file, fieldnames = headers)
	csv_writer.writeheader()
	for fighter in fighters:
		csv_writer.writerow({    #    <<<===    because to update new key in fighters.csv we needed to write them manually
			"Name": fighter["Name"],
			"Country": fighter["Country"],
			"Height": cm_to_in(fighter["Height (in cm)"])
		})
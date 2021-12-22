import csv, json


def add_item(rows, item_names):
	csv_name = rows["Name"]
	csv_common_name = rows["Common Name"]
	name = csv_common_name if csv_common_name != "NaN" else csv_name

	if name != "":
		item_names.append(name)


if __name__ == "__main__":
	csv_filepath = "Every item in Tekkit Classic - Data.csv"
	json_filepath = "item_names.json"


	item_names = []

	with open(csv_filepath) as csv_file:
		csv_reader = csv.DictReader(csv_file)
		for rows in csv_reader:
			add_item(rows, item_names)

	with open(json_filepath, "w") as f:
		json.dump(item_names, f)
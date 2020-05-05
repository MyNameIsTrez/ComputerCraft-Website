import os

directory = "renders/ComputerCraft/"

for fileName in os.listdir(directory):
	b = fileName.split("_", 2)[2:]
	# os.rename(folder + a, folder + b)
	print(fileName)
	print(b)
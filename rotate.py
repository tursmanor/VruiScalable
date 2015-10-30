import os
import sys

if os.path.isfile(sys.argv[2]):
	os.rename(sys.argv[2], sys.argv[2] + ".backup")

with open(sys.argv[1]) as f:
	for line in f:
		newfile = open(sys.argv[2], 'a')
		els = line.split(" ")
		if els[0] == "v" or els[0] == "vn":
			newfile.write(els[0] + " " + " ".join([str(-float(el)) for el in els[1:3]]) + " " + els[3])
			if "\n" not in els[3]:
				newfile.write("\n")
		else:
			newfile.write(line)
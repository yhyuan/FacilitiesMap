input = open("ontario.geojson", "r+")
output = open("ontario.simplified.geojson", "w")
with open('ontario.geojson') as fp:
	i = 0
	for line in fp:
		if (i >= 18 and i <= 18387):
			items = line.strip().split(',')
			output.write('[' + "{0:.6f}".format(float(items[0][1:].strip())) + ',' + "{0:.6f}".format(float(items[1][:-1].strip())) + '],')
		else:
			output.write(line)
		i = i + 1
output.close()
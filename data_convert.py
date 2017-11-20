import json

f = open('data.txt','r')
raw = f.readlines()
f.close()

def convert_int(word):
	if int(word)<0:
		return int(word)+360
	else:
		return int(word)

lon = map(convert_int, raw[19].split())

lat = []
for item in raw[21:]:
	lat.append(int(item.split()[0]))

data = []
for i in range(len(lat)):
	for j in range(len(lon)):
		value = raw[21+i].split()[2+j]
		if value == '****':
			value = '100'
		data.append([lon[j],lat[i],float(value)])

with open('D_region.json', 'w') as f:
    f.write(json.dumps(data))

print data
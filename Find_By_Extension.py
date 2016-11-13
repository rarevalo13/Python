import os
import sys
root = '/Users/ron/'
d = {'root': root,
     'Desktop': root + 'desktop',
     'Downloads': root + 'downloads',
     'Documents': root + 'documents',
     'Developer': root + 'developer',
     'Movies': root + 'movies',
     'Pictures': root + 'pictures'
     }


for path in d: 
	print(d[path])
	for file in os.listdir(d[path]):
		if file.endswith('.mobi'):
			print(file)

# path = input('What file directory do you wish to search? ')

# print(path)
# os.chdir(path)
# print(os.getcwd())

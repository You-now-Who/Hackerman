import re
string = open('python_files\words.txt').read()
new_str = re.sub('[^a-zA-Z0-9\n\.]', ' ', string)
open('python_files\words.txt', 'w').write(new_str)
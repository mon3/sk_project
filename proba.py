import re
text = 'hello'
for m in re.finditer('l', text):
	print(m.start())


text2 = 'hlelelelo'
for m in re.finditer('l', text2):
	print(m.start())
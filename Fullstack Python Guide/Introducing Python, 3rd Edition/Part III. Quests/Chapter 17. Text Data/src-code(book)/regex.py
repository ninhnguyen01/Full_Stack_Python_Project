import re
source = 'Young Frankenstein'
m = re.search('Frank', source)
if m:
     print(m.group())

m = re.match('.*Frank', source)
if m:  # match returns an object
    print(m.group())

m = re.sub('n', '?', source)
print(m)

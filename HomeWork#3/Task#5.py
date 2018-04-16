s = '''
We are not what we should be!
We are not what we need to be. 
But at least we are not what we used to be!'''

s1 = s.split()
number_of_words = len(s1)
print('Number of words in text: {}'.format(number_of_words), end='\n\n')

for i in range(len(s1)):
    s1[i] = s1[i].strip('.!')
print(s1, end='\n\n')

s1.sort()
print(s1, end='\n\n')

d = {}
for i in range(len(s1)):
    s1[i] = s1[i].lower()
for item in s1:
    d.update({item: s1.count(item)})
print(d)

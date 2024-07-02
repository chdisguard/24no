e = open('24.txt').readline()
m = 0
for r in '123456789':
    e = e.replace(r,'1')

while ('*00' in e) or ('*01' in e) or ('+00' in e) or ('+01' in e) or ('+*' in e) or ('*+' in e) or ('**' in e) or ('++' in e):
    e = e.replace('*00',' ')
    e = e.replace('*01',' 1')
    e = e.replace('+00',' ')
    e = e.replace('+01',' 1')
    e = e.replace('+*',' ')
    e = e.replace('*+',' ')
    e = e.replace('**',' ')
    e = e.replace('++',' ')
e = e.replace('* ', ' ')
e = e.replace('+ ', ' ')
e = e.replace(' *', ' ')
e = e.replace(' +', ' ')
e = e.split()
for i in range(len(e)):
    if eval(e[i]) == 0:
        if len(e[i]) > m:
            m = len(e[i])
print(m)

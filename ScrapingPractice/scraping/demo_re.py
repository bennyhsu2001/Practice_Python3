import re

s = "a123456789 z223456767 x343245 c4539-2-3"
ids = re.findall(r'[a-z]{1}[1-2]{1}\d{8}',s)
print(ids)  # ['a123456789', 'z223456767']


data = "From:Alex Wu (Alex N.T. Wu) <alexwu@gmail.com> Sat.Jan 5 09:14:16 2016"
match = re.search(r"[\w.-]+@[A-Za-z0-9_.-]+",data)
print(match.group())  # alexwu@gmail.com

greedyHa = re.compile(r'(Ha){3,5}')
mo1 = greedyHa.search('HaHaHaHaHa')
print(mo1.group()) # HaHaHaHaHa

nongreedyHa = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHa.search('HaHaHaHaHa')
print(mo2.group()) # HaHaHa


s = "xfooxxxxxxxfoo"
print(re.findall(r'.*foo',s))  # ["xfooxxxxxxxfoo"]
print(re.findall(r'.*?foo',s))  # ["xfoo","xxxxxxxfoo"]
print(re.search(r'.*foo',s).group())  # ["xfooxxxxxxxfoo"]
print(re.search(r'.*?foo',s).group())  # ["xfoo","xxxxxxxfoo"]


#(?P<groupname>regex)
phone = "001+886+2+12345678"
m = re.search(r'(?P<prefix>\d{3})\+(?P<country>\d{3})\+(?P<city>\d{1})\+(?P<phone>\d{8})',phone)
print(m.group("prefix"))
print(m.group("country"))
print(m.group("city"))
print(m.group("phone"))



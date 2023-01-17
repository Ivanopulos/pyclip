import pyperclip
import re
m = pyperclip.paste() # + "555"
#print(m)
bstr=72
#print(m)re.findall(r'\{.+\}', m)
n = re.findall(r'\{\}', m)
#n = re.sub(r'w\:fill\=\"(.{4,6})\"', "w:fill=\"AAAAAA\"", m)
print(n)
for b in n:
    m = m.replace("{}", "{" + str(bstr) + "}", 1)
    bstr += 1
pyperclip.copy(m)
print(m)
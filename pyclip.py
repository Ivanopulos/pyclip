import pyperclip
import re

m = pyperclip.paste()
m = re.sub(r"на.?сумму", ' ххх ', m)
m = re.sub(r"выполнение", ' ххх ', m)
m = re.sub(r"-", ' ххх ', m)
m = re.sub(r"ФАП(\w)", r'ФАП \1', m)
m = re.sub(r"  ", ' ', m)
n = re.findall(r'ФАП .{3,20} ххх', m)  # n = re.sub(r'w\:fill\=\"(.{4,6})\"', "w:fill=\"AAAAAA\"", m)
n = set(n) #уборка дублей
print(n)
for b in n:
    print(b)
print(m)




фыв="удаление лишней формулы из 6700"
# m = pyperclip.paste()
# m = re.sub(r"(?<!\))+\n.+\$[BC][A-Z]8(.+\n){3}\s+\.build\(\),", '', m)
# #m = re.sub(r"SpreadsheetApp\.newConditionalFormatRule\(\)\n.+\$[BC][A-Z]8(.+\n)+\s+\.build\(\),", '', m)
# pyperclip.copy(m)
# print(m)


фыв="добавление кавычки после формулы, равно и эндэнд для сцепки "#=N7&"Page 1'!A4"&"&"&N7&"Page 1'!B4"&"&"&N7&"Page 1'!D4""
# m = pyperclip.paste()
# m=re.sub(r"(Page 1'![ABD]\d{1,2})", r'\1"', m)
# m=re.sub(r"(?<!&)N7", '=N7', m)
# m=re.sub(r"&N7", '&"&"&N7', m)
# print(m)
# pyperclip.copy(m)

фыв="ре серч скобок"
# m = pyperclip.paste()  # коллекция для фигур хтмл
# a="gfsgdg4gfsdfg54g"
# b = re.search("\D(\d)\D", a)
# print(b[1])
фыв="нумеровалка фигурных скобок"
# # нумеровалка фигурных скобок
# bstr = 7412
# n = re.findall(r'\{\}', m)  # n = re.sub(r'w\:fill\=\"(.{4,6})\"', "w:fill=\"AAAAAA\"", m)
# print(n)
# for b in n:
#     m = m.replace("{}", "{" + str(bstr) + "}", 1)
#     bstr += 1
# pyperclip.copy(m)
# print(m)
фыв="склеивание ворда от битых скобок"
# # склеивание ворда битых скобок
# m = re.sub(r"(<w:t>\{\d*)</w:t>.*?(<w:t>(\d+)</w:t>).*?<w:t>(\d*\}</w:t>)", r"\1\3\4", m)
# m = re.sub(r"(<w:t>\{\d*)</w:t>.*?<w:t>(\d*\}</w:t>)", r"\1\2", m)
# pyperclip.copy(m)
фыв="пересортировка листа файлов на нетекстовую сортировку"
# # пересортировка листа
# a = ['1.png', '10.png', '11+.txt', '12+-.png', '13+20.png', '14+.txt', '15.png', '16.png', '17.png', '18+-.png', '19.png', '2.png', '20.png', '21.png', '22.png', '23.png', '24.png', '25.png', '26.png', '27+-.png', '28.png', '29.png', '3.png', '4+.txt', '5+-.png', '6.png', '7.png', '8+-.png', '8+.txt', '9.png']
# print(a)
# i=0
# while i < len(a)-1:
#     print(a)
#     if int(re.sub(r'\D*(\d+).+', r"\1", a[i])) > int(re.sub(r'\D*(\d+).+', r"\1", a[i+1])):
#         a[i], a[i+1] = a[i+1], a[i]
#         i = i - 2
#     i = max(i+1, 0)
# print(a)


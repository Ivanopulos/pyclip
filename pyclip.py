import pyperclip
import re
import pandas as pd
asd = "обработка для эксельки например заглав"
# m = pyperclip.paste()
# #m = re.sub(r'(\w)(\w+)', lambda m: m.group(1).upper() + m.group(2).lower(), m)
# #result = re.sub(r'(\w)(\w*)\s*', lambda m: m.group(1).upper() + m.group(2) + ' ', text)
# m = re.sub(r'(\d+)/(\d+)', r'Идентификатор ФП: \1, Идентификатор НП : \2', m)
# m = m.replace('\r\n', '\n')
# m = re.sub(r'^(\d+)$', r'Идентификатор ФП: \1', m, flags=re.MULTILINE)
# print(m)
# pyperclip.copy(m)
asd = "игра в слова, статистика началоконцов"
# from collections import Counter
#
# # Ваш исходный код
# m = pyperclip.paste()
# m = re.sub(r'[ьъы]', r'', m)
# m = re.sub(r'[й]', r'и', m)
# words = m.splitlines()
# letters_dict = {chr(i): {'start': 0, 'end': 0, 'end_letters': Counter()} for i in range(ord('а'), ord('я')+1)}
# letters_dict['ё'] = {'start': 0, 'end': 0, 'end_letters': Counter()}
#
# for word in words:
#     if word:
#         letters_dict[word[0]]['start'] += 1
#         letters_dict[word[-1]]['end'] += 1
#         letters_dict[word[0]]['end_letters'][word[-1]] += 1
#
# # Создаем датафрейм
# df = pd.DataFrame({k: {'start': v['start'], 'end': v['end'], 'top3': v['end_letters'].most_common(3)} for k, v in letters_dict.items()}).T
# df['start'] = df['start'].replace(0, 1e-10)
# df['ratio'] = df['end'] / df['start']
# df['dif'] = df['end'] - df['start']
#
# # Создаем отдельные столбцы для самых распространенных конечных букв и их количества
# df[['top1_letter', 'top1_count']] = df['top3'].apply(lambda x: x[0] if x else ('N/A', 0)).tolist()
# df[['top2_letter', 'top2_count']] = df['top3'].apply(lambda x: x[1] if len(x) > 1 else ('N/A', 0)).tolist()
# df[['top3_letter', 'top3_count']] = df['top3'].apply(lambda x: x[2] if len(x) > 2 else ('N/A', 0)).tolist()
#
# df.drop(columns='top3', inplace=True)  # Удаляем столбец 'top3', так как теперь у нас есть отдельные столбцы для этой информации
#
# # Сортируем по столбцу 'dif' и выводим результат
# df = df.sort_values('dif', ascending=False)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.expand_frame_repr', False)
# pd.options.display.float_format = None
# pd.options.display.float_format = '{:.0f}'.format
# print(df)
asd = "игра в слова, окончания"
# m = pyperclip.paste()
# m = re.sub(r'[ьъы]', r'', m)
# m = re.sub(r'[й]', r'и', m)
# #m = re.sub(r'[ё]', r'е', m)
# # разделение текста на список слов
# words = m.splitlines()
# # создаем пустой словарь для подсчета
# letters_dict = {chr(i): {'start': 0, 'end': 0} for i in range(ord('а'), ord('я')+1)}
# letters_dict['ё'] = {'start': 0, 'end': 0}
# # подсчет
# for word in words:
#     if word:
#         letters_dict[word[0]]['start'] += 1
#         letters_dict[word[-1]]['end'] += 1
# # создание DataFrame из словаря
# df = pd.DataFrame.from_dict(letters_dict, orient='index', columns=['start', 'end'])
# # добавление столбца с отношением
# df['ratio'] = df['end'] / df['start']
# df['dif'] = df['end'] - df['start']
# # сортировка по убыванию 4-го столбца (ratio)
# df = df.sort_values('dif', ascending=False)
# # возврат отсортированного DataFrame
# print(df)
asd = "подсчет тгсервиса 'остальное'"#/не видит дроби и пробелы***
# m = pyperclip.paste()
# m = m + "\r\n"  # иначе не ест последнее значение
# print(m)
# n = re.findall(r'(-?)(\d+)(?=[^\*]*\r)', m)
# n1 = re.findall(r'(-?)(\d+)(?=\*\*\*)', m)
# c = 0
# c1 = 0
# print(n, n1)
# print("Общие расходы:")
# for a, b in n:
#     c = c+int(a+b)
#     if a == "":
#         a = "+"
#     print(a + b)
# print("Отдельные перечисления:")
# for a, b in n1:
#     c1 = c1 + int(a + b)
#     if a == "":
#         a = "+"
#     print(a + b, "***")
# cs = ""
# if c1 > 0:
#     cs="+"
# print("Итого: "+str(c)+"/2" + cs + str(c1) + "="+str(int(c/2+c1))+"***")
asd = "подсчет тгсервиса 'расчеты'"# предкопирование в документ должно быть ибо последнее сообщение не цепляет
# m = pyperclip.paste()
# print(m)
# m = m + "\r\n"  # иначе не ест последнее значение
# m = re.sub(r'(\d+)\s(\d+)', r'\1\2', m)
# m = re.sub(r'(= ?)(\d+)', r"\1+\2", m)
# print(m)
# n = re.findall(r'(?<!gid)= ?([-+])(\d+)', m)
# n1 = re.findall(r'итого\s\+?(\d+ ?\d*)', m)
# n2 = int(n1[0])
# print(n, n1, n2)
# print("Предыдущий итог:", re.sub(r'(\d{3})$', r' \1', str(n2)))
# for a, b in n:
#     n2 = n2 + int(a + b)
#     print(a+re.sub(r'(\d{3})$', r' \1', str(b)), "(промежуточный итог:", re.sub(r'(\d{3})$', r' \1', str(n2)) + ")")
# n3 = re.sub(r'(\d{3})$', r' \1', str(n2))
# print("итого", n3)
# asd = "слова на а"
# m = pyperclip.paste()
# n = re.findall(r'^а\w+а:', m, flags=re.MULTILINE)
# print(n)
# for b in n:
#     print(b[:-1])
asd = "псеврекурсивное удаление скобок"
# m = pyperclip.paste()
# mlen = len(m)
# mlen1 = 99999999999
# while mlen < mlen1:
#     mlen1 = mlen
#     m = re.sub(r'(ЕСЛИ\([^\(\);]{1,10}\([^)]*?)\([^\(\)]*?\)', r'\1', m)
#     mlen = len(m)
# m = re.sub(r'(ЕСЛИ\()[^\(\);]{1,10}\([^)]*?\)', r'\1', m)
# m = re.sub(r' "";', r'', m)
# m = re.sub(r'" & ";', r'', m)

#            начало                # после базовой скобки
#                   до 10 не[();]        # найди финальную внутр скобку
# print(m) #
asd = "файндал и соед в строку"
# m = pyperclip.paste()
# n = re.findall(r'\d{7,},\w*\r', m)
# nn = ""
# for a in n:
#     nn = nn + a + '\n'
# pyperclip.copy(nn)
# print(nn)
asd = "удаление лишней формулы из 6700"
# m = pyperclip.paste()
# m = re.sub(r"(?<!\))+\n.+\$[BC][A-Z]8(.+\n){3}\s+\.build\(\),", '', m)
# #m = re.sub(r"SpreadsheetApp\.newConditionalFormatRule\(\)\n.+\$[BC][A-Z]8(.+\n)+\s+\.build\(\),", '', m)
# pyperclip.copy(m)
# print(m)
asd = "добавление кавычки после формулы, равно и эндэнд для сцепки "#=N7&"Page 1'!A4"&"&"&N7&"Page 1'!B4"&"&"&N7&"Page 1'!D4""
# m = pyperclip.paste()
# m=re.sub(r"(Page 1'![ABD]\d{1,2})", r'\1"', m)
# m=re.sub(r"(?<!&)N7", '=N7', m)
# m=re.sub(r"&N7", '&"&"&N7', m)
# print(m)
# pyperclip.copy(m)
asd = "ре серч скобок"
# m = pyperclip.paste()  # коллекция для фигур хтмл
# a="gfsgdg4gfsdfg54g"
# b = re.search("\D(\d)\D", a)
# print(b[1])
asd = "нумеровалка фигурных скобок"
# нумеровалка фигурных скобок
# bstr = 7412
# m = pyperclip.paste()
# n = re.findall(r'\{\}', m)  # n = re.sub(r'w\:fill\=\"(.{4,6})\"', "w:fill=\"AAAAAA\"", m)
# print(n)
# for b in n:
#     m = m.replace("{}", "{" + str(bstr) + "}", 1)
#     bstr += 1
# pyperclip.copy(m)
# print(m)
asd = "склеивание ворда от битых скобок"
# # склеивание ворда битых скобок
# m = re.sub(r"(<w:t>\{\d*)</w:t>.*?(<w:t>(\d+)</w:t>).*?<w:t>(\d*\}</w:t>)", r"\1\3\4", m)
# m = re.sub(r"(<w:t>\{\d*)</w:t>.*?<w:t>(\d*\}</w:t>)", r"\1\2", m)
# pyperclip.copy(m)
asd = "пересортировка листа файлов на нетекстовую сортировку"
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
asd = "расковыр руспрофиль по мз"
# m = pyperclip.paste()
# n = re.findall(r'(itemprop=""legalName"">)([^<]+)(.+?)(<span itemprop=""postalCode"">)(\d{6})(.+?)(<span itemprop=""address[LR][oe][cg][ai][lo][in][t]?[y]?"">)(.+?)(</span>)(, )(<span itemprop=""streetAddress"">)([^<]+)(.+?)(</span> <span class=""chief-title"">)([^<]+)(.+?)(<span.+?>)([^<]+)', m)
# print(n)
# data = []
# for m5, g, m6, m4, f, m3, m8, a, m1, m10, m2, e, m7, m9, h, m11, m12, j in n:
#     a = a.replace('</span>, <span itemprop=""addressLocality"">', ', ')
#     e = e.replace('&quot;', "")
#     print(g+"\t"+h+"\t"+j+"\t"+f+", "+a+", "+e)


    #row = [g, h, j, f, a, e]
    #data.append(row)
#df = pd.DataFrame(data)
#df.to_clipboard(index=False, header=False)
asd = "единицы измерения"
# units_var = pyperclip.paste()
# # адаптация пайклип к цсв
# units_var = re.sub(r';?\r\n;?', ';\r\n;', units_var)
# # обобщённые
# units_var = re.sub(r'\bтыс(яч)?(ах)?\b[ \.,)(]*(\w+)', r'тысъъ\3', units_var, flags=re.IGNORECASE)
# units_var = re.sub(r'\bмлн\b[ \.,)(]*(\w+)', r'млнъъ\1', units_var, flags=re.IGNORECASE)
#
# # очевидные по шаблону комментария
# units_var = re.sub(r'[^;]*процент[аоы]?[вх]?[^;]{,7}([;\.])', r'процент\1', units_var, flags=re.IGNORECASE)
# units_var = re.sub(r'[^;]*лет[^;]{,7}([;\.])', r'лет\1', units_var, flags=re.IGNORECASE)
# units_var = re.sub(r'[^;]*\b(\w*)человек[^;]{,7}[;\.]', r'\1человек;', units_var, flags=re.IGNORECASE)  # 'ъ' отсылка к разделителю
#
# units_var = re.sub(r'[^;]*\b(\w*)руб[л\.][еь]?[й]?[^;]{,7}[;\.]', r'\1руб;', units_var, flags=re.IGNORECASE)  # 'ъ' отсылка к разделителю
# units_var = re.sub(r'[^;]*\b(\w*)штук[^;]{,20}[;\.]', r'\1штук;', units_var, flags=re.IGNORECASE)
# units_var = re.sub(r'[^;]*цена[х]?[^;]{,7}[;\.]', r'руб;', units_var, flags=re.IGNORECASE)
# units_var = re.sub(r'[^;]*\b(\w*)км\b[^;]{,7}[;\.]', r'\1км;', units_var, flags=re.IGNORECASE)
# units_var = re.sub(r'[^;]*\bбалл[а]?[х]?\b[^;]{,40}[;\.]', r'балл;', units_var, flags=re.IGNORECASE)  # по прецеденту 12
# units_var = re.sub(r'[^;]*\b(\w*)семей[^;]{,7}[;\.]', r'\1семей;', units_var, flags=re.IGNORECASE)
#
# # ориентирующие по вхождению в текст
# units_var = re.sub(r'[^;]*числен[^;]*', r'человек', units_var, flags=re.IGNORECASE)
# units_var = re.sub(r'[^;]*количество[^;]*граждан[^;]*', r'человек', units_var, flags=re.IGNORECASE)
# units_var = re.sub(r'[^;]*число посещений[^;]*', r'единиц', units_var, flags=re.IGNORECASE)
# units_var = re.sub(r'[^;]*число[^;]*ших[^;]*', r'человек', units_var, flags=re.IGNORECASE)
# units_var = re.sub(r'[^;]*доля[^;]*', r'процент', units_var, flags=re.IGNORECASE)
# units_var = re.sub(r'[^;]*процент[^;]*', r'процент', units_var, flags=re.IGNORECASE)
# units_var = re.sub(r'[^;]*уровень[^;]*', r'процент', units_var, flags=re.IGNORECASE)
# units_var = re.sub(r'[^;]*часть[^;]*', r'процент', units_var, flags=re.IGNORECASE)
# units_var = re.sub(r'[^;]*коэффициент[^;]*', r'процент', units_var, flags=re.IGNORECASE)
# units_var = re.sub(r'[^;]*количество[^;]*месяц[^;]*', r'месяцев', units_var, flags=re.IGNORECASE)
# units_var = re.sub(r'[^;]*протяженность[^;]*', r'км', units_var, flags=re.IGNORECASE)
# units_var = re.sub(r'[^;]*количество[^;]*?[лд]ей[^;]*', r'человек', units_var, flags=re.IGNORECASE)
# units_var = re.sub(r'[^;]*количество[^;]*?щиков[^;]*', r'человек', units_var, flags=re.IGNORECASE)
# units_var = re.sub(r'[^;]*индекс[^;]*', r'процент', units_var, flags=re.IGNORECASE)
# units_var = re.sub(r'[^;]*(?!за )отчетный период[^;]*', r'№ года', units_var, flags=re.IGNORECASE)
#
# # финишный разделитель
# units_var = re.sub(r'ъъ', r' ', units_var)
# # затирка не найденых
# units_var = re.sub(r'[^;]*- ', r'', units_var)
#
#
# units_var = re.sub(r';\r\n;', r'\r\n', units_var)
# pyperclip.copy(units_var)


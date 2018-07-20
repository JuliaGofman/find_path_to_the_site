# Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
# Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.

import requests, re
# one, two = input(), input()
one, two = 'https://stepic.org/media/attachments/lesson/24472/sample1.html', 'https://stepic.org/media/attachments/lesson/24472/sample2.html'
url_2 = []
if requests.get(one).status_code == 200:
    url_ = re.findall(r'https?.*html', requests.get(one).text)
    for i in url_:
        url_2 += re.findall(r'https?.*html', requests.get(i).text)
if two in url_2:
    print('Yes')
else:
    print('No')
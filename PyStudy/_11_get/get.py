import os
#
# import requests
#
# # URL файла, который нужно скачать
# url = 'https://mshina.su/ftp/Price%20XLS.xls'
#
# # Имя файла, под которым он будет сохранён
# filename = url.split('/')[-1]
#
# # Выполнение GET-запроса для скачивания файла
# response = requests.get(url)
#
# # Проверка успешности запроса
# if response.status_code == 200:
#     # Сохранение файла
#     with open(filename, 'wb') as file:
#         file.write(response.content)
#     print(f"Файл '{filename}' успешно сохранён.")
# else:
#     print(f"Ошибка при скачивании файла: {response.status_code}")

#
print(os.listdir(path='.'))

#    os.rename('{filename}.xls', 'newfile.xls')
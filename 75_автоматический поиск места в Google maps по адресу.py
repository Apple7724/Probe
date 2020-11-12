# эта программа дает возможность поиска в Google maps
# по адресу, при этом сама открывает браузер и т.д.
import webbrowser, sys, pyperclip
if len(sys.argv)>1: # ф-ция sys.argv
    # -список аргументов командной строки, передаваемых сценарию Python:
    # Получение адреса из строки
    address = ''.join(sys.argv[1:])
else:
    # Получение адреса из буфера обмена. ф-ция pyperclip.paste
    # дает данные из буфера обмена
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/'+address)

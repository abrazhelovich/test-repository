# Написать скрипт, который будет получать на входе:
# обязательный параметр: адрес изображения в
# интернете;
# необязательный параметр: флаг, указывающий на
# поведение в случае, если изображение уже есть в
# папке: 1. перезаписать файл; 2. оставить оба файла(в
# этом случае к имени нового файла добавить случайно
# сгенерированную строку); 3. не сохранять файл. По
# умолчанию: перезаписать файл.
# Скрипт должен скачать указанный файл и сохранить
# его в папку images. Покрыть тестами все значимые
# функции(использовать unittest и doctest).
# Важно:
# - если папка images не существует - она должна быть
# создана скриптом автоматически.
# 1
# среда, 24 февраля 2021 г.
# - имя сохраняемого файла должно соответствовать
# имени файла в адресе запроса, например:
# файл в интернете https://cdn.pixabay.com/photo/
# 2015/03/26/09/40/forest-690058_960_720.jpg должен
# быть сохранен с именем forest-690058_960_720.jpg.
# - предусмотреть проверку на существование
# введенного адреса.
# - предусмотреть проверку на то, что скачиваемый
# файл является изображением(допустимые форматы
# изображения - .jpg, .jpeg, .png, .tiff).
# - если размер изображения менее 100кб - скачивать
# его в один заход, если больше - скачивать порционно.
# Подсказка: чтобы определить тип и размер файла
# обратите внимание на словарь headers вашего
# объекта запроса, чтобы определить, существует ли
# запрашиваемая страница - обратите внимание на
# статус вашего запроса.

from modules.get_image import get_image
from modules.img_types import img_form
from modules.is_folder_exist import check_folder
import argparse


def main():
    local_folder = 'images'
    check_folder(local_folder)
    avail_img_format = img_form()

    parser = argparse.ArgumentParser()
    parser.add_argument('-url', '--url', required=True)
    parser.add_argument('-mode', '--mode', required=False)
    args = parser.parse_args()

    get_image(args.url, args.mode, avail_img_format, local_folder)


if __name__ == '__main__':
    main()
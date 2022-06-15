from PIL import Image
import sys
import os

def rendering(picture_file, plashka_file, render_file):
    # Открываем файлы
    picture_image = Image.open(picture_file)
    plashka_image = Image.open(plashka_file)

    # Получаем размер файлов
    picture_width, picture_hight = picture_image.size
    plashka_width, plashka_hight = plashka_image.size

    # Берем больший размер по ширине и вычисляем высоту
    if plashka_width > picture_width:
        render_width = plashka_width
    else:
        render_width = picture_width
    render_hight = plashka_hight + picture_hight

    # Создаем новое изображение, по умолчанию полностью черное
    render_image = Image.new("RGB", (render_width, render_hight))

    # Заполняем белым цветом по координатам
    render_image.paste((255, 255, 255), [0, 0, render_width, render_hight])

    # Вставляем картинку в плашку
    render_image.paste(plashka_image)
    render_image.paste(picture_image, ((render_width - picture_width), plashka_hight))

    # Сохраняем картинку
    render_image.save(render_file, quality=100)


def valid_file(picture_file, plashka_file):
    for file in [picture_file, plashka_file]:
        if not os.path.isfile(file):
            return False
    return True

if __name__ == "__main__":
#picture_file, plashka_file, render_file = input(), input(), input()
    if not len(sys.argv) == 4:
    #if len(picture_file) == 0 or len(plashka_file) == 0 or len(render_file) == 0:
            print("Колличество передаваемых аргументов должно равняться 3 (трем)")
            print("В консоли введите (например): python main.py picture.jpg plashka.png render.png ")
            raise SystemExit
    picture_file, plashka_file, render_file = sys.argv[1], sys.argv[2], sys.argv[3]
    if valid_file(picture_file, plashka_file):
             rendering(picture_file, plashka_file, render_file)
             print(f"Обработка картинки успешно завершена: {render_file}")
    else:
        print("Один из файлов не существует в папке")
        print("В консоли введите (например): python main.py picture.jpg plashka.png render.png")
        raise SystemExit

import pygame
import game
from tkinter import *
from tkinter import messagebox
from game import get_score
from tkinter.ttk import Combobox


# выход из игры
def on_closing():
    if messagebox.askokcancel('Выход из игры',
                              'Хотите выйти из игры?'):
        window.destroy()


# нажимаем на кнопку
def clicked():
    game.start(fon.get(), speed.get(), music.get())
    if pygame.quit:
        score.config(text=str(get_score()))


# создание окна меню
window = Tk()
window.title('DinoGame')
window.resizable(0, 0)
window.geometry('500x500')
window.protocol("WM_DELETE_WINDOW", on_closing)

# кнопочка для начала игры
button = Button(window, text="Начать игру!", command=clicked)
button.grid(column=1, row=0)
button.place(relx=.5, rely=.35, anchor="center", height=30, width=130, bordermode=OUTSIDE)

# добавим текст для счета
text_score = Label(window, text='Количество очков:', font=('Aerial', 10))
text_score.place(relx=.5, rely=.45, anchor="center", height=30, width=150, bordermode=OUTSIDE)
score = Label(window, text=0, font=('Aerial', 10))
score.place(relx=.5, rely=.5, anchor="center", height=30, width=150, bordermode=OUTSIDE)

# динозаврик
img = PhotoImage(file='dino.png').subsample(10, 10)
lbl = Label(window, image=img)
lbl.place(rely=.2, relx=.5, anchor="center")

# просто текст
label = Label(window, text='Динозаврик', font=('Aerial', 18))
label.place(relx=.5, rely=.05, anchor="center")

# ползунок громкости музыки
label_music = Label(window, text='Громкость музыки:', font=('Aerial', 10))
label_music.place(relx=.15, rely=.7, anchor="center")
music = Scale(window, from_=0, to=100, orient=HORIZONTAL)
music.place(relx=.5, rely=.68, anchor="center")

# выбор скорости (уровня)
label_speed = Label(window, text='Выберите уровень игры:', font=('Aerial', 10))
label_speed.place(relx=.15, rely=.8, anchor="center")
speed = Combobox(window, state='readonly')
speed['values'] = ('Легкий',
                   'Средний',
                   'Тяжелый',
                   'Хардкор',
                   )
speed.current(1)
speed.grid(column=1, row=0)
speed.place(relx=.5, rely=.8, anchor="center", height=30, width=150, bordermode=OUTSIDE)

# список фона
label_fon = Label(window, text='Выберите фон игры:', font=('Aerial', 10))
label_fon.place(relx=.15, rely=.9, anchor="center")
fon = Combobox(window, state='readonly')
fon['values'] = ('Белый',
                 'Жёлтый',
                 'Красный',
                 'Зеленый',
                 'Синий',
                 'По умолчанию'
                 )
fon.current(5)
fon.grid(column=1, row=0)
fon.place(relx=.5, rely=.9, anchor="center", height=30, width=150, bordermode=OUTSIDE)

# запускаем окно
window.mainloop()

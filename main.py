#импортирую библиотеки
import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

data_file = "books.json"
books = []

#функция загрузки
def load_data():
    pass

#функция сохранения данных
def save_data():
    pass

#функция отображения книг
def display_books(data_to_show=None):
    pass

#функция добавления книг
def add_book():
    pass

#функция фильтрации книг
def filter_books():
    pass

#функция сброса фильтров
def reset_filter():
    pass

#главное окно приложения
window = tk.Tk()
window.title("Book Tracker (Трекер прочитанных книг)")
window.geometry("700x550")

load_data()

#форма ввода
frame_form = ttk.LabelFrame(window, text="Новая книга")
frame_form.pack(pady=10, padx=10, fill="x")
#форма ввода названия
ttk.Label(frame_form, text="Название:").grid(row=0, column=0, padx=5, pady=5)
ent_title = ttk.Entry(frame_form)
ent_title.grid(row=0, column=1, padx=5, pady=5)
#форма ввода автора
ttk.Label(frame_form, text="Автор:").grid(row=0, column=2, padx=5, pady=5)
ent_author = ttk.Entry(frame_form)
ent_author.grid(row=0, column=3, padx=5, pady=5)
#форма ввода жанра
ttk.Label(frame_form, text="Жанр:").grid(row=1, column=0, padx=5, pady=5)
ent_genre = ttk.Entry(frame_form)
ent_genre.grid(row=1, column=1, padx=5, pady=5)
#форма ввода кол-ва страниц
ttk.Label(frame_form, text="Количество страниц:").grid(row=1, column=2, padx=5, pady=5)
ent_pages = ttk.Entry(frame_form)
ent_pages.grid(row=1, column=3, padx=5, pady=5)

#кнопка добавления новой книги
btn_add = ttk.Button(frame_form, text="Добавить книгу", command=add_book)
btn_add.grid(row=2, column=0, columnspan=4, pady=10)

#интерфейс фильтров
frame_filter = ttk.LabelFrame(window, text="Фильтрация")
frame_filter.pack(pady=5, padx=10, fill="x")
#фильтр по жанру
ttk.Label(frame_filter, text="Жанр:").pack(side="left", padx=5)
ent_f_genre = ttk.Entry(frame_filter, width=15)
ent_f_genre.pack(side="left", padx=5)
#фильтр по количеству страниц
ttk.Label(frame_filter, text="Мин. кол-во страниц:").pack(side="left", padx=5)
ent_f_pages = ttk.Entry(frame_filter, width=10)
ent_f_pages.pack(side="left", padx=5)

ttk.Button(frame_filter, text="Применить", command=filter_books).pack(side="left", padx=5)
ttk.Button(frame_filter, text="Сбросить", command=reset_filter).pack(side="left", padx=5)

#таблица
table = ttk.Treeview(window, columns=("Title", "Author", "Genre", "Pages"), show="headings")
table.heading("Title", text="Название")
table.heading("Author", text="Автор")
table.heading("Genre", text="Жанр")
table.heading("Pages", text="Страниц")
table.pack(pady=10, padx=10, fill="both", expand=True)

# Инициализация таблицы при запуске
display_books()

window.mainloop() #запуск непрервного цикла окна

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from tkinter import *
from tkinter import ttk
from random import choice


films = pd.read_csv('imdb_top_250.csv')
film_genres_list = list(films['Genre'])


complex_genres = [] # будем хранить составные жанры, чтобы потом их удалить
for film_genre in film_genres_list:
    genres = film_genre.split(' | ') # разберем каждый составной жанр на составляющие
    if len(genres) > 1: # если попался составной жанр
        for genre in genres: # то пройдемся по всем элементарным жанрам фильма
            film_genres_list.append(genre) # и добавим их
        complex_genres.append(film_genre) 
# обратите внимание, что мы не можем в процессе итерации через for удалять элементы, поскольку это собьет итератор. Можете посмотреть, к чему это приведет, написав вместо complex_genres.append(film_genre) сразу film_genres_list.remove(film_genre)
        
for genre in complex_genres:
    film_genres_list.remove(genre)
    
genres_set = set(film_genres_list) 
FilmsAndGenres = {}
for i in range(len(films)):
    FilmsAndGenres[films['Title'][i]] = films['Genre'][i].split(' | ')


def find_film(*args):
    choose_genre = cur_genre.get()
    if choose_genre in genres_set:
        randomgenre = ""
        while choose_genre not in randomgenre:
            randomfilm = choice(list(films['Title']))
            randomgenre = FilmsAndGenres[randomfilm]
        film.set(f'Попробуйте "{randomfilm}" ')
    elif choose_genre == "":
        film.set("Ждем ваш выбор")
    else:
        film.set("Такого жанра не существует")

root = Tk()
root.geometry("350x100")
root.title("Фильмотека")

mainframe = ttk.Frame(root, padding="10 10 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

cur_genre = StringVar()
cg_entry = ttk.Entry(mainframe, width=20, textvariable=cur_genre)
cg_entry.grid(column=1, row=1, sticky=(E))

film = StringVar()
ttk.Label(mainframe, textvariable=film).grid(column=1, row=3, sticky=(W, E))
ttk.Button(mainframe, text="Подобрать", command=find_film).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="Введите жанр").grid(column=3, row=1, sticky=W)

# этот цикл позволяет "разбросать" элементы подальше друг от друга
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.bind("<Return>", find_film)
root.mainloop()

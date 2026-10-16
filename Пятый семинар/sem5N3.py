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
#print(film_genres_list)
#print(genres_set)
FilmsAndGenres = {}
for i in range(len(films)):
    FilmsAndGenres[films['Title'][i]] = films['Genre'][i].split(' | ')
print(FilmsAndGenres)

choose_genre = input()
if choose_genre in genres_set:
    randomgenre = ""
    while choose_genre not in randomgenre:
        randomfilm = choice(list(films['Title']))
        randomgenre = FilmsAndGenres[randomfilm]
        print(randomgenre)
    print("Итог: ", randomfilm)
else:
    print("Такого жанра не существует")


#! /bin/python

# Ce script contiendra les classes
import os
import json
import logging
CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR,'data','movies.json')

def get_movies():
    # Récuperer la liste de tous les films contenu dans le fichier
    with open(DATA_FILE,'r') as file:
         movies_title = json.load(file)
    movies = [Movie(movie) for movie in movies_title ]
    # afin d'obtenir des instances
    return movies
    
class Movie:
    def __init__(self, titre):
        self.titre = titre.title()
        
    def __str__(self):
        return self.titre
        # def title(self,name: str=''):
        #     print(name.upper())
    
    def _get_movies(self):
        # Récupérer la liste des films avec le module json.load 
        with open(DATA_FILE,'r') as file:
            file_data = json.load(file)
            return file_data
    
    def _write_movies(self, movies):
        # Ecrire une liste de film dans la liste avec json.dump
        # with open(DATA_FILE,'r') as file:
            # file_data = json.load(file)
        # file_data.append(movies)
        # with open(DATA_FILE,'w') as file:
            # json.dump(file_data, file, indent=3)
        with open(DATA_FILE,'w') as file:
            json.dump(movies, file, indent=3)
            
    def add_to_movies(self):
        # def add_to_movies(self, movie):
        # Récuperer la liste de film
        # movies = self._get_movies()
        
        # Vérifier que le film n'existe pas dans la liste
        # for item in movies:
            # Si il existe, on affiche un message disant que ce dernier existe
            # if item == movie:
                # print("Ce film est déja présent dans la liste")
            
            # Sinon on l'ajoute
            # else:
                # self._write_movies(movie)
        movies = self._get_movies()
        
        if self.titre not in movies:
            movies.append(self.titre)
            self._write_movies(movies)
            return True
        
        else:
            logging.INFO(f"Le Titre {self.titre} est déja présent dans la liste")
            return False

    def remove_from_movies(self):
        # Récupérer la liste des films
        movies = self._get_movies()
        # Vérifier si le film est bien dans la liste
        
        if self.titre in movies:
            # Si c'est le cas, enlever le film de la liste
            movies.remove(self.titre)
            # et écrire le nouveau film dans 
            # le fichier json
            self._write_movies(movies)


if __name__ == "__main__":
    film = get_movies()
    print(film)
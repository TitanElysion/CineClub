#! /bin/python

# Ce script contient l'interface graphique de notre application

from movie import Movie, get_movies

from PySide2 import QtWidgets, QtCore

class App(QtWidgets.QWidget):
    def __init__(self): # Initialisation des différents modules
        super().__init__()
        self.setWindowTitle('Ciné Club')
        self.setup_ui()
        self.populate_movies()
        self.setup_connections()
        
    def setup_ui(self):
        """Interface graphique de l'application
        """
        self.main_layout = QtWidgets.QVBoxLayout(self) # Fenêtre principale
        self.line_edit_movieTitle = QtWidgets.QLineEdit() # Barre d'édition de texte
        self.line_edit_movieTitle.setPlaceholderText("Ajouter un Film")
        self.button_addMovie = QtWidgets.QPushButton("Ajouter un Film")# Bouton pour ajouter un film
        self.list_all_movies = QtWidgets.QListWidget() # Zone d'affichage des films
        self.list_all_movies.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)
        self.button_removeMovie = QtWidgets.QPushButton("Supprimer le(s) film(s)") # Bouton de suppression des films
        
        
        """Connexion des modules de l'application aux éléments
        de l'interface graphique
        """
        self.main_layout.addWidget(self.line_edit_movieTitle)
        self.main_layout.addWidget(self.button_addMovie)
        self.main_layout.addWidget(self.list_all_movies)
        self.main_layout.addWidget(self.button_removeMovie)
        
    def setup_connections(self):
        self.button_addMovie.clicked.connect(self.add_movie)
        self.button_removeMovie.clicked.connect(self.remove_movie)
        self.line_edit_movieTitle.returnPressed.connect(self.add_movie)
    
    def populate_movies(self): 
        """Récupère et affiche la liste de tous les films
        """
        movies = get_movies()
        
        for movie in movies:
            list_all_movies_item = QtWidgets.QListWidgetItem(movie.titre)
            list_all_movies_item.setData(QtCore.Qt.UserRole, movie)
            self.list_all_movies.addItem(list_all_movies_item)
            # self.list_all_movies.addItem(movie.titre)
            
    def add_movie(self):
        # Récupérer le texte qui est dans le line_edit
        movie_title = self.line_edit_movieTitle.text()
        if not movie_title:
            return False
        # Créer une instance 'Movie'
        movie = Movie(titre = movie_title)
        
        # Ajouter le film dans le fichier json
        result = movie.add_to_movies()
        
        # Ajouter le titre du film dans le list Widget
        if result:
            #self.list_all_movies.addItem(movie.titre)
            list_all_movies_item = QtWidgets.QListWidgetItem(movie.titre)
            list_all_movies_item.setData(QtCore.Qt.UserRole, movie)
            self.list_all_movies.addItem(list_all_movies_item)
            # self.line_edit_movieTitle.setText("Ajouter un Film")
            self.line_edit_movieTitle.setPlaceholderText("Ajouter un film")
        #print("On ajoute un film")
        self.line_edit_movieTitle.setText("")
        
    def remove_movie(self):
        for selected_item in self.list_all_movies.selectedItems():
            movie =selected_item.data(QtCore.Qt.UserRole)
            movie.remove_from_movies()
            self.list_all_movies.takeItem(self.list_all_movies.row(selected_item))
        # print("On supprime le film")
        
app = QtWidgets.QApplication([])

win = App()

win.show()

app.exec_()

# film = Movie("harry potter")
# film.add_to_movies()

# print(film)
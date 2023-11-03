# Exercice
# Coder une classe Durée possédant trois attributs :
# ·   Le nombre d’heures de la durée ;
# ·   Le nombre de minutes de la durée ;
# ·   Le nombre de secondes de la durée.
# Et les méthodes publiques suivantes :
# ·   Un constructeur par défaut (tous les attributs auront zéro comme valeur) et un constructeur initialisant toutes les valeurs. On vérifiera que les nombres d’heures, minutes, secondes sont bien positifs, dans le cas contraire on considèrera leurs opposés. On fera également les conversions nécessaires pour que les nombres de minutes et de secondes soient strictement inférieurs à 60.
# ·   Une méthode réalisant l’affichage de la durée (sous la forme 3h10m00s) ;
# ·   Une méthode convertissant la durée en un nombre de secondes ;
# ·   Une méthode rajoutant à la durée un nombre de secondes.

#Pensez à tester toute votre classe dans un main.
#Dépôt par personne avec une branche main puis une branche dev qui dérive de main, vous codez sur la branche dev et une fois le code fini, vous merguez dev sur main. ATTENTION commencer par protéger votre branche main en imposant un pull request pour merger dessus.

# définition de la classe duree

class Duree:
	def __init__(self, heure=0,minute=0,seconde=0):
		self.heure = heure
		self.minute = minute
		self.seconde = seconde
		

	def __str__(self):
		return str(self.heure).zfill(2)+'h'+str(self.minute)+'m'+str(self.seconde).zfill(2)+'s'
	
	def afficher(self):
		print(str(self.heure).zfill(2)+'h'+str(self.minute)+'m'+str(self.seconde).zfill(2)+'s')
		
	def conversion(self):
		converti=self.heure * 3600 + self.minute * 60 + self.seconde
		print("La durée en temps HH:MM:SS vaut : ", str(self.heure).zfill(2)+'h'+str(self.minute).zfill(2)+'m'+str(self.seconde).zfill(2)+'s')
		print("La durée en seconde vaut : ", self.heure * 3600 + self.minute * 60 + self.seconde,' seconde')
		return converti
	
	def ajouter(self, secondes_ajouter=0):
		total = self.conversion()
		total += secondes_ajouter
		self.heure = total // 3600  # Quotient pour les heures
		total %= 3600  # Reste après avoir ajouté les heures
		self.minute = total // 60  # Quotient pour les minutes
		self.seconde = total % 60  # Reste pour les secondes
		return print('la durée nouvelle vaut : ',str(self.heure).zfill(2)+'h'+str(self.minute).zfill(2)+'m'+str(self.seconde).zfill(2)+'s')
        
        

	







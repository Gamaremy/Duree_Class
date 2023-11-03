import Duree_Classe as DC



def main():
	MonTempsTest=DC.Duree(5,20,30)
	# Fonction afficher()
	MonTempsTest.afficher()
	#Ou marche avec juste le nom de la variable grace à la méthode __str_
	print(MonTempsTest)
	MonTempsTest.conversion()
	MonTempsTest.ajouter(3600)
	


    
	
if __name__ == '__main__':
	main()
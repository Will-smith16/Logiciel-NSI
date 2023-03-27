#Ce fichier est le dictionnaire de tous les cours:

#Ces 3 fonctions ne marchent pas (pour le moment X) )
def ajouter_chapitre(nom: str) -> None:
    """Ajoute le chapitre <nom> à la liste des chapitres"""
    global dict_cours,dict_exos
    dict_cours[nom] = {}
    dict_exos[nom] = {}

def ajouter_cours(nom_chapitre:str ,nom: str, path: str)-> None:
    """Ajoute le cours <nom> aux cours du chapitre"""
    global dict_cours
    dict_cours[nom_chapitre][nom] = path

def ajouter_exo(nom_chapitre: str, nom: str,path: str)-> None:
    """Ajoute l'exercice <nom> aux exercices du chapitre"""
    global dict_exos
    dict_exos[nom_chapitre][nom] = path

dict_cours : dict = {"chapitre1":{"leçon1":"PDF/ouverture.pdf"}}

dict_exos : dict = {"leçon1":{"exercice1":"PDF/ouverture.pdf"}}

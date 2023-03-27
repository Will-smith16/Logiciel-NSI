import csv

def nouvelle_sauvegarde(pseudo:str, mdp:str, table:str, admin = False) -> None:
    """creer une nouvelle sauvegarde"""
    f = open(table,'a')
    w = csv.DictWriter(f, ["pseudo", "mdp", "admin"])
    w.writerow({"pseudo": pseudo, "mdp": mdp, "admin": admin})
    f.close()

def verif_sauvegarde(pseudo:str, mdp:str, table:str) -> bool:
    """verifie une sauvegarde déjà existante"""
    f = open(table, 'r')
    table = list(csv.DictReader(f))
    for e in table:
        if pseudo == e['pseudo'] and mdp == e['mdp'] :
            return False
    f.close()
    return True

def verifpseudo(pseudo:str, table:str) -> bool:
    """verifie que le pseudo choisi est original"""
    f = open(table, 'r')
    table =list(csv.DictReader(f))
    for e in table:
        if e ['pseudo'] == pseudo:
            return True
    f.close()
    return False

def user_is_admin(pseudo:str ,table:str) -> bool:
    """verifie si l'utilisateur est un admin"""
    f = open(table, 'r')
    table = list(csv.DictReader(f))
    for e in table:
        if e ['pseudo'] == pseudo and e["admin"] == "True":
            return True
        elif e ['pseudo'] == pseudo and e["admin"] == "False":
            return False
    f.close()



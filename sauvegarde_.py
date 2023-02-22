import csv

def nouvelle_sauvegarde(pseudo:str, mdp:str, table:str) -> None:
    """creer une nouvelle sauvegarde"""
    f = open(table,'a')
    w = csv.DictWriter(f, ["pseudo", "mdp"])
    w.writerow({"pseudo": pseudo, "mdp": mdp})
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

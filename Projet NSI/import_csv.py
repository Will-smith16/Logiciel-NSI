import csv

def get_all_chapters() -> list: 
    """Permet de récupérer la liste de tous les chapitres"""
    f = open("chapitres.csv", "r")
    table = list(csv.DictReader(f,delimiter=";")) #Preciser que le delimiter est ; et non ,
    val = []
    for e in table:
        val.append(e["chapitres"])
    return val 

def get_lessons(chapitre: str) -> list:
    """Renvoie une liste composée de couples (path,nom_leçon)"""
    f = open("chapitres.csv", "r")
    table = list(csv.DictReader(f,delimiter=";")) #Preciser que le delimiter est ; et non ,
    val = []
    for e in table:
        if e["chapitres"] == chapitre:
            val =e["lst_leçons"]
    return transform_to_list(val) 

def get_enonce_exercices(chapitre: str, lesson: str, nom: str) -> list:
    """Renvoie une liste composée de couples (path,nom_leçon)"""
    f = open("exercices.csv", "r")
    table = list(csv.DictReader(f,)) #Preciser que le delimiter est ; et non ,
    val = ""
    for e in table:
        if e["chapitre"] == chapitre and e["leçon"] == lesson and e["nom_exo"] == nom:
            val = e["enonce"]
    return val 

def get_name_lessons(chapitre: str):
    """Renvoie la liste des noms de leçons du chapitre"""
    lst = get_lessons(chapitre)
    res = []
    for chap in range(len(lst)):
        res.append(lst[chap][1])
    return res

def get_name_exercices(chapitre: str, lesson: str) -> list:
    """Permet de récupérer la liste de tous les exercices d'un chapitre et d'une leçon données"""
    f = open("exercices.csv", "r")
    table = list(csv.DictReader(f)) #Preciser que le delimiter est ; et non ,
    val = []
    for e in table:
        if e["chapitre"] == chapitre and e["leçon"] == lesson:
            val.append(e["nom_exo"])
    return val 

def add_chapter(chapitre: str) -> bool:
    """Ajoute le chapitre dans le csv et renvoie true si l'opération a eu lieu, False sinon"""
    if not chapitre in get_all_chapters():
        f = open("chapitres.csv", "a")
        table = csv.DictWriter(f, ["chapitres", "lst_leçons"], delimiter=";")
        table.writerow({"chapitres":chapitre, "lst_leçons":[]})
        f.close()
        return True #L'action a été faite
    return False

def delete_user(user: str) -> bool:
    """Supprime l'utilisateur dont le pseudo est donné en argument. Renvoie True si tout c'est bien passé, False sinon"""
    with open('csvfile.csv', 'r') as fr:
        # reading line by line
        lines = fr.readlines()
        line_to_delete = find_line(user, "pseudo", 'csvfile.csv')
        acc = 0
        # opening in writing mode
        with open('csvfile.csv', 'w') as fw:
            for line in lines:
                if acc != line_to_delete:
                    fw.write(line)
                acc += 1

        if line_to_delete == 1:
            return False
        return True
    
def find_line(value: str, key: str, file: str ,delimiter: str= ",") -> int or None:
    """Renvoie la ligne correspondant à la valeur de l'élément 'value' de clé 'key' dans le fichier 'file' ayant pour séparation 'delimiter'"""
    with open(file, 'r') as f:
        test = list(csv.DictReader(f,delimiter= delimiter))
        line_to_delete = 0
        for e in test:
            line_to_delete += 1
            if e[key] == value:
                f.close()
                return line_to_delete
        f.close()

def add_lesson(chapitre: str ,path_lecon: str ,nom_lecon: str) -> bool:
    """Ajoute la leçon dans le csv et renvoie True si l'opération a eu lieu, False sinon\n
    ATTENTION: Doit suivre la syntaxe suivante : "'path'" et " 'nom'" (l'espace est important)"""
    if chapitre in get_all_chapters():
        with open("chapitres.csv",'r') as fr:
            lines = fr.readlines()
            line_to_modifiy = find_line(chapitre,"chapitres","chapitres.csv",";") 
            line_to_update = add_lesson_bis(chapitre,path_lecon,nom_lecon)
            acc = 0
            a_marché = False
            with open("chapitres.csv", 'w') as fw:
                for line in lines:
                    if acc != line_to_modifiy:
                        fw.write(line)
                    else:
                        if line_to_update is None:
                            fw.write(line) 
                        elif line_to_update is not None:
                            fw.write(line_to_update+"\n")
                            a_marché = True
                    acc += 1
            if line_to_modifiy == 0 or not a_marché:
                return False
            return True
    return False

def add_lesson_bis(chapitre: str ,path: str ,nom_lecon: str) -> None or str :
    """Renvoie la ligne changée ou None si le changement n'a pas pu avoir lieu"""
    with open("chapitres.csv", 'r') as f:
        test = list(csv.DictReader(f, delimiter=";"))
        for e in test:
            if e["chapitres"] == chapitre and not nom_lecon in e["lst_leçons"]:
                lecon_lst = str(e["lst_leçons"])
                res = change_txt(lecon_lst, "(" + path + "," + nom_lecon + ")")
                return str(chapitre) + ";" + res

def change_txt(base_txt: str, what_to_add: str) -> str:
    "renvoie une nouvelle chaine de caractères à partir de celles envoyées"
    res = ""
    for ch in base_txt:
        if ch == "]":
            if base_txt == "[]":
                ch = what_to_add + "]"
            else:
                ch = ", " + what_to_add + "]"
        res += ch
    return res

def transform_to_list(value: str) -> list:
    coma_in_couple = False
    res = []
    path, name = "",""
    characters = ["[","]","'","(",")",","," "]
    for ch in value:
        if ch == "," and not coma_in_couple:
            coma_in_couple = True
        elif ch == "," :
            coma_in_couple = False
        if not coma_in_couple and ch not in characters :
            path +=ch
        elif coma_in_couple and ch not in characters:
            name += ch
        if ch == ")":
            res.append((path,name))
            path,name = "",""
    return res

def add_exercice(chapitre:str ,lesson: str, nom: str, enonce: str)-> bool:
    """Ajoute l'exercice dans le csv suivant les paramètres donnés. Renvoie True si l'action a eu lieu, false sinon."""
    if chapitre in get_all_chapters() and lesson in get_name_lessons(chapitre):
        with open("exercices.csv", "r") as fr:
            r = list(csv.DictReader(fr))
            for e in r:
                if e["chapitre"] == chapitre and e["leçon"] == lesson and e["nom_exo"] == nom:
                    return False
                else:
                    with open("exercices.csv","a") as f:
                        w = csv.DictWriter(f, ["chapitre", "leçon", "nom_exo", "enonce"])
                        w.writerow({"chapitre": chapitre, "leçon": lesson, "nom_exo": nom, "enonce": enonce})
                        return True
    return False
    
def delete_exo(chapitre: str, lesson: str = None, nom: str = None)-> bool:
    """Supprime l'exercice avec les infos données en argument. Renvoie True si tout c'est bien passé, False sinon"""
    with open('exercices.csv', 'r') as fr:
        # reading line by line
        lines = fr.readlines()
        lines_to_delete = find_line_exo(chapitre, lesson, nom)
        acc = 0
        # opening in writing mode
        with open('exercices.csv', 'w') as fw:
            for line in lines:
                if lines_to_delete is None or acc not in lines_to_delete:
                    fw.write(line)
                acc += 1
        if lines_to_delete is None:
            return False
        return True

def find_line_exo(chapitre: str, lesson: str, nom: str)-> int or None:
    with open("exercices.csv", 'r') as f:
        test = list(csv.DictReader(f))
        line_to_delete = 0
        res = []
        for e in test:
            line_to_delete += 1
            if e["chapitre"] == chapitre and lesson is None and nom is None:
                res.append(line_to_delete)
            elif e["chapitre"] == chapitre and lesson == e["leçon"] and nom is None:
                res.append(line_to_delete)
            elif e["chapitre"] == chapitre and e["leçon"] == lesson and e["nom_exo"] == nom:
                res.append(line_to_delete)
        f.close()
        return res
       
def delete_chapter(chapitre: str) -> bool: 
    """Supprime le chapitre donné en argument (et donc les leçons et exos qu'il y'avait). Renvoie True si tout c'est bien passé, False sinon"""
    with open('chapitres.csv', 'r') as fr:
        # reading line by line
        lines = fr.readlines()
        line_to_delete = find_line(chapitre, "chapitres", 'chapitres.csv',";")
        acc = 0
        # opening in writing mode
        with open('chapitres.csv', 'w') as fw:
            for line in lines:
                if acc != line_to_delete:
                    fw.write(line)
                acc += 1
        if line_to_delete is None:
            return False
        else:
            delete_exo(chapitre)
            return True

def delete_lesson(chapitre: str,lesson_name: str) -> bool:
    """Supprime la lecon du chapitre dans le csv et renvoie True si tout a marché False sinon """
    lst = get_lessons(chapitre)
    res = []
    for chap in lst:
        if chap[1] != lesson_name:
            res.append(chap)
    if res == lst:
        return False
    else:
        delete_exo(chapitre, lesson_name)
        return modif_line(str(res), str(lst), "lst_leçons", "chapitres.csv", ";")

def modif_line(new_val: str, previous_val: str, key: str, file: str, delimiter: str = ","):
    """Permet de remplacer la valeur 'previous_val' par 'new_val' de clé 'key' dans le fichier 'file' ayant pour séparateur 'delimiter'
    Renvoie True si tout c'est bien passé, False sinon
    """
    with open(file,'r') as fr:
        lines = fr.readlines()
        line_to_modifiy = find_line(previous_val,key,file,delimiter) 
        acc = 0
        with open(file, 'w') as fw:
            for line in lines:
                if acc != line_to_modifiy:
                    fw.write(line)
                else:
                    string = line.replace(previous_val,new_val)
                    fw.writelines(string)
                acc += 1
        if line_to_modifiy is None:
            return False
        return True
    
def get_path_lesson(chapitre, lesson):
    lst = get_lessons(chapitre)
    for l in lst:
        if l[1] == lesson:
            return l[0]
        
print("Ici c'est pour les tests donc tu mets ce que tu veux pour essayer une fonction. Mais attention à la syntaxe exigée si tu fais ça sinon tout ne va pas bien marcher")

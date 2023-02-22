import platform
import os
from tkinter import filedialog
from tkinter import *

"""os.path.abspath(__file__) permet d'obtenir le path du script"""

def open_pdf() -> None:
    """Ouvre la fenetre pour choisir un fichier PDF et l'ouvre dans le lecteur par defaut de l'OS
    """
    file_path = filedialog.askopenfilename(filetypes=[("Fichiers PDF", "*.pdf")])
    if "macOS" in platform.platform():
        os.system(f"open {file_path}")

    elif "Windows" in platform.platform():
        os.startfile(f"{file_path}")

def open_given_pdf(file_path)-> None:
    """Ouvre un fichier PDF donné dans le lecteur par defaut de l'OS
    """
    if "macOS" in platform.platform():
        os.system(f"open {file_path}")

    elif "Windows" in platform.platform():
        os.startfile(f"{file_path}")



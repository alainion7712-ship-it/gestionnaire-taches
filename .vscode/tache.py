import json
from pathlib import Path

FICHIER = Path("taches.json")

def charger():
    if FICHIER.exists():
        try:
            return json.loads(FICHIER.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            print("Fichier abîmé, on repart de zéro.")
    return []

def sauvegarder(taches):
    texte = json.dumps(taches, indent=2, ensure_ascii=False)
    FICHIER.write_text(texte, encoding="utf-8")

def afficher(taches):
    if not taches:
        print("Aucune tâche.")
    for i, t in enumerate(taches, start=1):
        case = "x" if t["faite"] else " "
        print(f"{i}. [{case}] {t['titre']}")

def main():
    taches = charger()
    while True:
        print("\n1) Voir  2) Ajouter  3) Terminer  4) Quitter  5) Supprimer")
        choix = input("Choix : ").strip()
        if choix == "1":
            afficher(taches)
        elif choix == "2":
            titre = input("Titre : ").strip()
            if titre:
                taches.append({"titre": titre, "faite": False})
                sauvegarder(taches)
        elif choix == "3":
            afficher(taches)
            try:
                n = int(input("Numéro : "))
                if n < 1:
                    raise IndexError
                taches[n - 1]["faite"] = True
                sauvegarder(taches)
            except (ValueError, IndexError):
                print("Numéro invalide.")
        elif choix == "5":
            afficher(taches)
            try:
                n = int(input("Numéro à supprimer : "))
                if n < 1:
                    raise IndexError
                supprimee = taches.pop(n - 1)
                sauvegarder(taches)
                print(f"Supprimé : {supprimee['titre']}")
            except (ValueError, IndexError):
                print("Numéro invalide.")
        elif choix == "4":
            break

if __name__ == "__main__":
    main()
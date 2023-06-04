from fonction import ajouter_eleves,supprimer_eleves,info_eleves,ajouter_une_notes,moyenne_general, info_classe, supprimer_une_note


menu_option = [{
    'indice': '1',
    'description': 'Ajouter un élève',
    'fonction': ajouter_eleves
},{
    'indice': '2',
    'description': 'supprimer un élève',
    'fonction': supprimer_eleves
},{
    'indice': '3',
    'description': 'carte informations d\'un élève',
    'fonction': info_eleves
},{
    'indice': '4',
    'description': 'ajouter une note a un élève',
    'fonction': ajouter_une_notes
},{
    'indice': '5',
    'description': 'affiche la moyenne général d\'un élève',
    'fonction': moyenne_general
},{
    'indice': '6',
    'description': 'liste élève par classe',
    'fonction': info_classe
},{
    'indice': '7',
    'description': 'supprimer une note a un élève',
    'fonction': supprimer_une_note
}]

def menu():
    g=True
    while g:
        print("******")
        print("*MENU*")
        print("******")
        print()
        for element in menu_option:
            print(f"[{element['indice']}] : {element['description']}")
        print("[quit] : quittez")
        x=input("\nQue veut tu faire ? ")
        if x == 'quit':
            g=False
        for element in menu_option:
            if x == element['indice']:
                z=element['fonction']()
                if z == False:
                    g=False
menu()
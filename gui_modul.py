import tkinter as tk
from tkinter import simpledialog, messagebox
from main import HouseManager

class HouseManagerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Házkezelő Alkalmazás")

        self.house_manager = HouseManager()
        self.house_manager.load_data_from_file(self.house_manager.flats_database, self.house_manager.residents_database)

        self.create_widgets()

    def create_widgets(self):
        # TODO: Készítsd el a Tkinter elemeket (label, entry, button stb.) a GUI-hoz.
        # Példakód:
        self.label = tk.Label(self.master, text="Üdvözöljük a Házkezelő Alkalmazásban!")
        self.label.pack()

        self.button_add_resident = tk.Button(self.master, text="Lakó hozzáadása", command=self.add_resident)
        self.button_add_resident.pack()

        self.button_add_flat = tk.Button(self.master, text="Lakás hozzáadása", command=self.add_flat)
        self.button_add_flat.pack()

        self.button_save_data = tk.Button(self.master, text="Adatok mentése", command=self.save_data)
        self.button_save_data.pack()

    def add_resident(self):
        name = simpledialog.askstring("Lakó hozzáadása", "Lakó neve:")
        flat = simpledialog.askstring("Lakó hozzáadása", "Lakóhoz rendelt lakás:")
        if not flat:
            flat = None
        self.house_manager.add_resident(name, flat)
        messagebox.showinfo("Siker", "Lakó sikeresen hozzáadva!")

    def add_flat(self):
        floor = simpledialog.askinteger("Lakás hozzáadása", "Emelet:")
        flat = simpledialog.askinteger("Lakás hozzáadása", "Ajtó:")
        self.house_manager.add_flat(floor, flat)
        messagebox.showinfo("Siker", "Lakás sikeresen hozzáadva!")

    def save_data(self):
        self.house_manager.save_data_to_file(self.house_manager.flats_database, self.house_manager.residents_database)
        messagebox.showinfo("Siker", "Adatok sikeresen mentve!")

# Main függvény Tkinter alkalmazás indításához
def run_tkinter_app():
    root = tk.Tk()
    app = HouseManagerGUI(root)
    root.mainloop()




'''class Menu():
    def __init__(self):
        self.house_manager = HouseManager()
        self.house_manager.load_data_from_file(self.house_manager.flats_database,self.house_manager.residents_database)

    def display_menu(self):
        print()
        print('##########'*5)
        print('             Házkezelő Alkalmazás')
        print()
        print('Menü')
        print()
        print('1. Lakó hozzáadása. ')
        print('2. Lakás hozzáadása')
        print('3. Lakó hozzárendelése lakáshoz. ')
        print('4. Lakó eltávolítása lakásból. ')
        print('5. Adatok mentése fájlba. ')
        print('6. Adatok betöltése fájlból. ')
        print('7. Jelentés készítése. ')
        print('0. Kilépés. ')

        return input()

    def display_report_submenu(self):
        print('1. Összes lakó megjelenítése.')
        print('2. Összes lakás megjelenítése. ')
        print('3. Adott lakás információinak megjelenítése. ')
        print('4. Adott emeleten lévő lakások megjelenítése. ')
        print('5. Hasonló lakások összesítése. ')
        return input()
        


    def run_menu(self):
        choice = ' '
        while choice != '0':
            choice = self.display_menu()

            match  choice:
                case '1':
                    name = input('Lakó neve: ')
                    flat = input('Lakóhoz rendelt lakás. ')
                    if not flat:
                        flat = None
                    self.house_manager.add_resident(name, flat)

                case '2':
                    floor = int(input('Emelet. '))
                    flat = int(input('Ajtó. '))
                    #rooms = int(input('Szombák száma. '))
                    self.house_manager.add_flat(floor,flat)

                case '3':
                    print('Melyik lakót rendeljük lakáshoz?.')
                    self.report('1')
                    resident = input()
                    print('Meliyk lakáshoz rendeljük? ')
                    self.report('2')
                    flat = input()
                    self.house_manager.add_resident_to_flat(resident,flat)

                case '4':
                    print('Melyik lakóttávolítsuk el a lakásból?.')
                    self.report('1')
                    resident = input()
                    self.house_manager.remove_resident_from_flat(resident)

                case '5':
                    self.house_manager.save_data_to_file(self.house_manager.flats_database,self.house_manager.residents_database)

                case '6':
                    self.house_manager.load_data_from_file()

                case '7':
                    self.house_manager.report(self.display_report_submenu())

        self.house_manager.save_data_to_file(self.house_manager.flats_database,self.house_manager.residents_database)
    
'''
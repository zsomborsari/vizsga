import sys,time,json
#from gui_modul import run_tkinter_app
        
class Floor():
    def __init__(self, floor_number):
        self.floor_number = floor_number

class Flat(Floor):
    def __init__(self, floor_number, flat_number):
        super().__init__(floor_number)
        self.flat_number = flat_number


class Resident():
    def __init__(self, name,flat=None):
        self.name = name
        self.flat = flat


class HouseManager():
    def __init__(self):
        self.flats_dict = {}
        self.residents_dict = {}
        self.flats_database = 'lakasok.json'
        self.residents_database = 'lakok.json'

    def add_resident(self, name, flat=None):
        resident = Resident(name, flat)
        self.residents_dict[len(self.residents_dict)] = resident.__dict__ 


    def add_flat(self, floor,flat):
        flat = Flat(floor,flat)
        self.flats_dict[len(self.flats_dict)] = flat.__dict__
    
    def add_resident_to_flat(self,resident,flat):
        self.residents_dict[resident]['flat'] = flat 

    def remove_resident_from_flat(self,resident):
        self.residents_dict[resident]['flat'] = None

    def save_data_to_file(self,flats_file, residents_file):
        try:
            with open(flats_file, 'w') as flatfile:
                json.dump(self.flats_dict,flatfile)

            with open(residents_file, 'w') as residentfile:
                json.dump(self.residents_dict,residentfile)

        except FileNotFoundError:
            print('A fájlok nem találhatók')

    def load_data_from_file(self,flats_file, residents_file):
        try:
            with open(flats_file) as flatfile:
                self.flats_dict = json.load(flatfile)

            with open(residents_file) as residentfile:
                self.residents_dict = json.load(residentfile)

        except FileNotFoundError:
            print('A fájlok nem találhatók.')

    def report(self, sub):
        match sub:
            case '1':
                for r in self.residents_dict.items():
                    print(f'{r[0]}: Név: {r[1]['name']} Ajtó: {r[1]['flat']}')
            case '2':
                for f in self.flats_dict.items():
                    print(f'{f[0]}: Emelet: {f[1]['floor_number']}, Ajtó: {f[1]['flat_number']}')
            case '3':
                pass #print info about specifik flat
            case '4':
                pass #print info about flats on same floor
            case '5':
                pass #print info about same type flats


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


#def main():
#    run_tkinter_app()
            
# __name__ == '__main__':
#    sys.exit(main())


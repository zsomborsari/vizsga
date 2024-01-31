import sys,time,json

        
class Floor:
    def __init__(self, floor_number):
        self.floor_number = floor_number

class Flat(Floor):
    def __init__(self, floor_number, flat_number,room_number,resident_number = 0):
        super().__init__(floor_number)
        self.flat_number = flat_number
        self.room_number = room_number
        self.resident_number = resident_number

    def change_residents_number(self, operation):
        if operation == '+':
            self.resident_number += 1
        elif operation == '-':
            self.resident_number -= 1


    def __str__(self):
        return f'Emelet: {self.floor_number}, Ajtó: {self.flat_number}, Szobák: {self.room_number}, Lakók: {self.resident_number}'


class Resident:
    def __init__(self, name,flat=None):
        self.name = name
        self.flat = flat

    def change_flat(self,flat):
        self.flat = flat

    def __str__(self):
        return f'Név: {self.name}, Lakás: {self.flat}'
        


class HouseManager:
    def __init__(self):
        self.flats = []
        self.residents = []
        self.flats_database = 'lakasok.json'
        self.residents_database = 'lakok.json'

    def add_resident(self, name, flat=None):
        '''add resident to dictionary'''
        resident = Resident(name, flat)
        self.residents.append(resident)
        #self.residents_dict[len(self.residents_dict)+1] = resident.__dict__ 


    def add_flat(self, floor,flat,rooms):
        '''add flat to dictionary'''
        flat = Flat(floor,flat,rooms)
        self.flats.append(flat)
        #self.flats_dict[len(self.flats_dict)+1] = flat.__dict__
    
    def add_resident_to_flat(self,resident,flat):
        ''''''
        #self.residents_dict[resident]['flat'] = flat
        residentmod = self.residents[resident-1]
        if residentmod.flat:
            self.remove_resident_from_flat(resident)
        residentmod.change_flat(self.flats[flat-1].flat_number)
        self.flats[flat-1].change_residents_number('+')

        

    def remove_resident_from_flat(self,resident):
        residentmod = self.residents[resident-1]
        flatmod = residentmod.flat
        print(flatmod)
        for f in self.flats:
            if f.flat_number == flatmod:
                f.change_residents_number('-')
        residentmod.change_flat(None)
        #self.flats_dict[self.residents_dict[resident]['flat']] -= 1
        #self.residents_dict[resident]['flat'] = None


    def delete_resident(self,resident):
        resident = self.residents[resident-1]
        for f in self.flats:
            if resident.flat == f.flat_number:
                f.change_residents_number('-')
                break
        del(resident)
        #self.residents_dict.pop(resident)

    def delete_flat(self,flat):
        flat = self.flats[flat-1]
        if flat.resident_number == 0:
            del(flat)
        else:
            print('A lakás nem törölhető, mert lakók vannak hozzárendelve.')
        #self.flats_dict.pop(flat)


    
class Menu:
    def __init__(self):
        self.house_manager = HouseManager()
        self.load_data_from_file(self.house_manager.flats_database,self.house_manager.residents_database)

    def display_menu(self):
        print('##########'*5)
        print('             Házkezelő Alkalmazás')
        print('                     Menü')
        print()
        print('1. Lakó hozzáadása. ')
        print('2. Lakás hozzáadása')
        print('3. Lakó hozzárendelése lakáshoz. ')
        print('4. Lakó eltávolítása lakásból. ')
        print('5. Lakó törlése. ')
        print('6. Lakás törlése.')
        print('7. Adatok mentése fájlba. ')
        print('8. Adatok betöltése fájlból. ')
        print('9. Jelentés készítése. ')
        print('0. Kilépés. ')

        return input()

    def display_report_submenu(self):
        print('1. Összes lakó megjelenítése.')
        print('2. Összes lakás megjelenítése. ')
        print('3. Adott lakás információinak megjelenítése. ')
        print('4. Adott emeleten lévő lakások megjelenítése. ')
        print('5. Hasonló lakások összesítése. ')
        return input()
        
    def report(self, sub):
        match sub:
            case '1':
                #for r in self.residents_dict.items():
                #    print(f'{r[0]}: Név: {r[1]['name']} Ajtó: {r[1]['flat']}')
                count = 1
                for r in self.house_manager.residents:
                    print(count,end='. ')
                    print(r)
                    count += 1
            case '2':
                #for f in self.flats_dict.items():
                #    print(f'{f[0]}: Emelet: {f[1]['floor_number']}, Ajtó: {f[1]['flat_number']},  Szobák: {f[1]['room_number']}, Lakók száma: {f[1]['resident_number']}')
                count = 1
                for f in self.house_manager.flats:
                    print(count,end='. ')
                    print(f)
                    count += 1
            case '3':
                print('')
                print('Mi alapján szeretnél jelentést készíteni a lakásokról?')
                print('1. Szobák száma')
                print('2. Lakók száma')
                reporttype = input()
                print('Add meg a mennyiséget. ')
                reportvalue = int(input())
                for f in self.house_manager.flats:
                    if reporttype == '1':
                        if f.floor_number == reportvalue:
                            print(f)
                    elif reporttype == '2':
                        if f.resident_number == reportvalue:
                            print(f)
                      #print info about specific flat
            case '4':
                floors = []
                for f in self.house_manager.flats:
                    if not f.floor_number in floors:
                        floors.append(f.floor_number)
                for l in floors:
                    print(f'{l}. emelet.')
                print('Válassz emeletet. ')
                pass #print info about flats on same floor
            case '5':
                pass #print info about same type flats

    def loading_animation(self,sec):
        print("Loading:")
        #animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
        animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
        for i in range(len(animation)):
            time.sleep(sec)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()
        print("\n")

    def save_data_to_file(self,flats_file, residents_file):
        self.residents_dict = {}
        for r in self.residents:
            self.residents_dict[len(self.residents_dict)+1] = r.__dict__ 

        self.flats_dict = {}
        for f in self.flats:
            self.flats_dict[len(self.flats_dict)+1] = f.__dict__ 
        try:
            with open(flats_file, 'w') as flatfile:
                json.dump(self.flats_dict,flatfile)

            with open(residents_file, 'w') as residentfile:
                json.dump(self.residents_dict,residentfile)

            self.loading_animation(0.1)

        except FileNotFoundError:
            print('A fájlok nem találhatók')

    def load_data_from_file(self,flats_file, residents_file):
        try:
            with open(flats_file) as flatfile:
                self.flats_dict = json.load(flatfile)
                for f in self.flats_dict.items():
                    flat = Flat(f[1]['floor_number'], f[1]['flat_number'], f[1]['room_number'], f[1]['resident_number'])
                    self.house_manager.flats.append(flat)

            with open(residents_file) as residentfile:
                self.residents_dict = json.load(residentfile)
                for r in self.residents_dict.items():
                    resident = Resident(r[1]['name'], r[1]['flat'])
                    self.house_manager.residents.append(resident)


            self.loading_animation(0.1)

        except FileNotFoundError:
                
            print('A fájlok nem találhatók.')


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
                    self.loading_animation(0.01)
                    self.house_manager.add_resident(name, flat)

                case '2':
                    floor = int(input('Emelet. '))
                    flat = int(input('Ajtó. '))
                    rooms = int(input('Szombák száma. '))
                    self.loading_animation(0.01)
                    self.house_manager.add_flat(floor,flat,rooms)

                case '3':
                    print('Melyik lakót rendeljük lakáshoz?.')
                    self.report('1')
                    resident = int(input())
                    print('Meliyk lakáshoz rendeljük? ')
                    self.report('2')
                    flat = int(input())
                    self.loading_animation(0.01)
                    for i in self.house_manager.flats:
                        print(i)
                    self.house_manager.add_resident_to_flat(resident,flat)

                case '4':
                    print('Melyik lakót távolítsuk el a lakásból? ')
                    self.report('1')
                    try:
                        resident = int(input())
                    except ValueError:
                        print('Nem számot adtál meg.')
                    self.loading_animation(0.01)
                    self.house_manager.remove_resident_from_flat(resident)

                case '5':
                    print('Melyik lakót szeretnéd törölni?' )
                    self.report('1')
                    resident = int(input())
                    self.loading_animation(0.01)
                    self.house_manager.delete_resident(resident)

                case '6':
                    print('Melyik lakást szeretnéd törölni?' )
                    self.report('2')
                    try:
                        flat = int(input())
                    except ValueError:
                        print('Nem számot adtál meg.')
                        self.loading_animation(0.01)
                    try:
                        self.house_manager.delete_flat(flat)

                    except:
                        print('A megadott szám nem szerepel a litán.')

                case '7':
                    self.loading_animation(0.005)
                    self.house_manager.save_data_to_file(self.house_manager.flats_database,self.house_manager.residents_database)
                case '8':
                    self.loading_animation(0.005)
                    self.house_manager.load_data_from_file(self.house_manager.flats_database,self.house_manager.residents_database)

                case '9':
                    submenu_choice = self.display_report_submenu()
                    self.report(submenu_choice)
                    input('Nyomj enter a folytatáshoz.')


        self.house_manager.save_data_to_file(self.house_manager.flats_database,self.house_manager.residents_database)
    


def main():
   menu = Menu()
   menu.run_menu()

        
if __name__ == '__main__':
    sys.exit(main())


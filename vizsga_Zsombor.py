import sys,time

class Flat():
    def __init__(self,flat_id, address, number_of_rooms, floor, doorbell):
        self.flat_id = flat_id
        self.address = address
        self.number_of_rooms = number_of_rooms
        self.floor = floor
        self.doorbell = doorbell


class Resident():
    def __init__(self,name):
        self.name = name
        self.flat = None

class HouseManager():
    def __init__(self):
        self.flats = {}
        self.residents = {}

    def add_resident(self,name,flat_id):
        flat = next((f for f in self.flats if f.flat_id == flat_id), None)
        if not flat:
            print("Hiba: A megadott lakás nem létezik.")
            return
        resident = Resident(name)
        resident.flat = flat
        print(resident)

    def delete_resident(self,name):
        self.residents = [resident for resident in self.residents if resident.name != name]

    def add_flat(self, flat_id, address, number_of_rooms, floor, doorbell):
        flat_data = []
        flat = Flat(flat_id, address,number_of_rooms,floor, doorbell)
        flat_data = [flat.flat_id,flat.address,flat.number_of_rooms,flat.floor,flat.doorbell]
        self.flats.setdefault(flat_data[0], []).append(flat_data[1:]) # type: ignore
        

        print(self.flats)


    def delete_flat(self,flat_id):
        self.flats = [flat for flat in self.flats if flat.id != flat_id]
        self.residents = [resident for resident in self.residents if resident.flat.id != flat_id]

    def add_resident_to_flat(self, name,flat_id):
        resident = next((t for t in self.residents if t.name == name), None)
        if not resident:
            print("Hiba: A megadott lakó nem létezik. ")
            return
        resident.flat = next((f for f in self.flats if f.id == flat_id), None)


    def remove_resident_from_flat(self,name):
        resident = next((t for t in self.residents if t.name == name), None)
        if not resident:
            print("Hiba: A megadott lakó nem létezik. ")
            return
        resident.flat = None

    def save_data_to_file(self,filename):
        with open(filename, 'w') as file:
            file.write(str(self.__dict__))
        self.loading_animation()

    def load_data_from_file(self, filename):
        with open(filename, 'r') as file:
            data = eval(file.read())
            self.__dict__.update(data)
        self.loading_animation()

    def residents_report(self):
        for resident in self.residents:
            print(f'Név: {resident.name}, \nLakás: {resident.flat.id if resident.flat else 'Nincs hozzárendelve lakás'}, ')

    def flats_report(self):
        for flat in self.flats:
            print(f'Ajtó száma: {flat.flat_id} \nCím: {flat.address} \nSzobák száma: {flat.number_of_rooms} \nEmelet: {flat.floor} \nKapucsengő: {flat.doorbell}')

    def loading_animation(self):
        print("Loading:")
        #animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
        animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
        for i in range(len(animation)):
            time.sleep(0.2)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()
        print("\n")

class Menu():
    def __init__(self):
        self.housemanager = HouseManager()
        self.filename = 'database.txt'

    def display_menu(self):
        print('\nHázkezelő alkalmazás')
        print('1. Lakó hozzáadása')
        print('2. Lakó eltávolítása')
        print('3. Lakás hozzáadása')
        print('4. Lakás eltávolítása')
        print('5. Lakó hozzárendelése lakáshoz')
        print('6. Lakó eltávolítása lakásból')
        print('7. Információk mentése fájlba')
        print('8. Információk betöltése fájlból')
        print('9. Jelentések')
        print('0. Kilépés')


    def run_menu(self):
        while True:
            self.display_menu()
            try:
                choice = int(input('Válassz egy menüpontot(0-9): '))
                match choice:
                    case 1:
                        name = input('Lakó neve: ')
                        flat_id = input('Ajtó száma: ')
                        self.housemanager.add_resident(name, flat_id)

                    case 2:
                        name = input('Lakó neve: ')
                        self.housemanager.delete_resident(name)

                    case 3:
                        flat_id = input('Ajtó száma: ')
                        if flat_id in self.housemanager.flats:
                            print(f'Ilyen számú ajtó ({flat_id}) már létezik.')
                            continue
                        else:
                            address = input('Cím: ')
                            number_of_rooms = input('Szobák száma: ')
                            floor = input('Emelet: ')
                            doorbell = input('Kapucsengő: ')

                            self.housemanager.add_flat(flat_id,address,number_of_rooms,floor,doorbell)

                    case 4:
                        flat_id = input('Ajtó száma: ')
                        self.housemanager.delete_flat(flat_id)

                    case 5:
                        name = input('Lakó neve: ')
                        flat_id = input('Ajtó száma: ')
                        self.housemanager.add_resident_to_flat(name,flat_id)

                    case 6:
                        name = input('Lakó neve: ')
                        self.housemanager.remove_resident_from_flat(name)

                    case 7:
                        self.housemanager.save_data_to_file(self.filename)

                    case 8:
                        self.housemanager.load_data_from_file(self.filename)

                    case 9:
                        report = input('1. Lakók jelentése. \n2. Lakások jelentése. ')
                        if report == '1':
                            self.housemanager.residents_report()
                        elif report == '2':
                            self.housemanager.flats_report()
                        else:
                            print('Nincs ilyen választási lehetőség.')

                    case 0:
                        print('Adatok mentése.')
                        self.housemanager.save_data_to_file(self.filename)
                        print('Kilépés. ')
                        break
                        

            except ValueError as e:
                print(e)
def main():
    menu = Menu()
    menu.run_menu()


if __name__ == '__main__':
    sys.exit(main())


term = int(input("Írj be egy számot:"))
match term:
    case 1:
         print("1-es ág")
    case 2:
          print("2-es ág")
    case 3:
          print("3-as ág")
    case _:
         print("Ide jön, ha nem talál megfelelő ágat")
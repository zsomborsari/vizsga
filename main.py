import sys,time,json
from gui_modul import run_tkinter_app
        
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





def main():
    run_tkinter_app()


if __name__ == '__main__':
    sys.exit(main())


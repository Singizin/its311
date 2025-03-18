import pandas as pd

df = pd.DataFrame

df = pd.read_excel('files/inv.xlsx', header=0)

print(df.head())

class Invetroty:
    def __init__(self):
        self.df = pd.DataFrame
        self.df = pd.read_excel('files/inv.xlsx', header=0)
        self.convert_to_str()
        print(df.head())
        self.rooms = []
        self.buildings = set()

    def convert_to_str(self):
        self.df = self.df.astype(str)

    def define_rooms(self):
        self.rooms = self.df['room'].unique()
        print(self.rooms)

    def define_buildings(self):
        rooms = self.df['full_room'].unique()

        for room in rooms:
            self.buildings.add(room.split('-')[0])
        print(self.buildings)


    def shrink_table(self):
        pass


if __name__ == "__main__":
    inv = Invetroty()
    inv.define_rooms()
    inv.define_buildings()
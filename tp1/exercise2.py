import os
from random import randint, choice
from time import sleep

tiles = randint(5, 15)
random_movement = randint(1, 2)


class Floor:
    def __init__(self, size, stage_list, stains_floor, position, move):
        self.size = size
        self.stage = stage_list
        self.stains_floor = stains_floor
        self.position = position
        self.move = move

    def get_size(self):
        return self.size

    def set_size(self, size):
        self.size = size

    def get_stage_list(self):
        return self.stage

    def set_stage_list(self, stage_list):
        self.stage = stage_list

    def get_stains_floor(self):
        return self.stains_floor

    def set_stains_floor(self, stains_floor):
        self.stains_floor = stains_floor

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    def move_left(self):
        self.position -= 1

    def move_right(self):
        self.position += 1

    def get_move(self):
        return self.move

    def set_move(self, move):
        self.move = move


class Funcion:
    @staticmethod
    def clean_up():
        print('Floor cleaned')

    @staticmethod
    def clean_floor():
        print('The floor is already clean')


    @staticmethod
    def stage(tiles):
        return [x for x in range(tiles)]

    @staticmethod
    def position_initial(tiles):
        return choice(tiles)

    @staticmethod
    def generate_floor(tiles):
        floor = []
        state = [' ', '+', 'x', '#']

        for i in range(tiles):
            floor.append(choice(state))
        return floor

    @staticmethod
    def show_main_information(size_floor, stage_list, stains_floor, position):
        print(f'Map size: {size_floor}')
        print(f'Floor tiles: {stage_list}')
        print(f'Dirt: {stains_floor}')
        print(f'Initial position: {position}')
        input('Press any key to start the vacuum cleaner work...')
        print()

    @staticmethod
    def check_the_floor(stains_floor, position):
        print(Funcion.clean_up())
        if stains_floor[position] == 'x' or stains_floor[position] == '+':
            stains_floor[position] = ' '
        return stains_floor


ambient = Floor(
    tiles,
    Funcion.stage(tiles),
    Funcion.generate_floor(tiles),
    Funcion.position_initial(Funcion.stage(tiles)),
    random_movement
)


def main():
    movement_counter = 0
    final_position = 0
    aspirated = 0

    Funcion.show_main_information(
        ambient.get_size(),
        ambient.get_stage_list(),
        ambient.get_stains_floor(),
        ambient.get_position()
    )

    clean_history = [False for _ in range(ambient.get_size())]

    while True:

        os.system('clear')

        vacuum_cleaner_position = [' ' for _ in range(ambient.get_size())]
        vacuum_cleaner_position[ambient.get_position()] = "@"

        print(clean_history)
        print(f'The vacuum cleaner is on the tile: {ambient.get_position()}')
        print(f'Current state of the floor: \n{vacuum_cleaner_position}\n{ambient.get_stains_floor()}')

        if not clean_history[ambient.get_position()]:
            ambient.set_stains_floor(Funcion.check_the_floor(ambient.get_stains_floor(), ambient.get_position()))
        else:
            print(Funcion.clean_floor())

        if ambient.get_stains_floor()[ambient.get_position()] == 'x' or '+' or '#':
            clean_history[ambient.get_position()] = True
            aspirated += 2

        if ambient.get_position() == ambient.get_stage_list()[0]:
            ambient.set_move(2)
        elif ambient.get_position() >= ambient.get_stage_list()[-1]:
            ambient.set_move(1)

        ambient.move_left() if ambient.get_move() == 1 else ambient.move_right()

        sleep(1)
        movement_counter += 1

        if False not in clean_history:
            os.system('clear')
            break

    for i in vacuum_cleaner_position:
        if i == '@':
            break
        final_position += 1

    print(f'Final position: {final_position} | I do: {movement_counter} movements.')
    print(f'Final condition of the floor: \n{vacuum_cleaner_position}\n{ambient.get_stains_floor()}')

    print(f'Number of vacuums: {str(aspirated)}')


if __name__ == '__main__':
    main()

import os
from random import randint, choice
from time import sleep

from model_floor import Floor

tiles = randint(5, 15)
random_movement = randint(1, 2)


class Funcion:
    @staticmethod
    def clean_up():
        print('Floor cleaned')

    @staticmethod
    def clean_floor():
        print('The floor is already clean')

    @staticmethod
    def floor_not_cleanable():
        print('The floor cannot be cleaned here')

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

        if stains_floor[position] == ' ':
            Funcion.clean_floor()

        elif stains_floor[position] == '+':
            stains_floor[position] = ' '
            Funcion.clean_up()

        elif stains_floor[position] == 'x':
            stains_floor[position] = '+'
            Funcion.clean_up()

        else:
            Funcion.floor_not_cleanable()

        return stains_floor

    @staticmethod
    def actual_position_aspirated(actual_position):
        if actual_position == 'x' or actual_position == '+' or actual_position == '#':
            return True


ambient = Floor(
    tiles,
    Funcion.stage(tiles),
    Funcion.generate_floor(tiles),
    Funcion.position_initial(Funcion.stage(tiles)),
    random_movement
)


def main():
    movement_counter = 0
    aspirated = 0

    Funcion.show_main_information(
        ambient.get_size(),
        ambient.get_stage_list(),
        ambient.get_stains_floor(),
        ambient.get_position()
    )

    while True:

        os.system('clear')

        vacuum_cleaner_position = [' ' for _ in range(ambient.get_size())]
        vacuum_cleaner_position[ambient.get_position()] = "@"

        actual_position = ambient.get_stains_floor()[ambient.get_position()]

        if Funcion.actual_position_aspirated(actual_position):
            aspirated += 1

        print(f'The vacuum cleaner is on the tile: {ambient.get_position()}')
        print(f'Current state of the floor: \n{vacuum_cleaner_position}\n{ambient.get_stains_floor()}')
        ambient.set_stains_floor(Funcion.check_the_floor(ambient.get_stains_floor(), ambient.get_position()))

        if ambient.get_position() <= 0:
            ambient.set_move(2)
        elif ambient.get_position() >= ambient.get_size() - 1:
            ambient.set_move(1)

        print(f'Total number of aspirated: {str(aspirated)}')

        ambient.move_left() if ambient.get_move() == 1 else ambient.move_right()

        sleep(1)
        movement_counter += 1


if __name__ == '__main__':
    main()

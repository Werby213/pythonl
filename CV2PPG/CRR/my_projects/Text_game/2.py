class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        if direction in self.paths:
            return self.paths[direction]()
        else:
            print("Вы не можете туда пойти.")

class Game:
    def __init__(self, start_room):
        self.start_room = start_room

    def play(self):
        current_room = self.start_room

        while True:
            print("\n" + current_room.name)
            print(current_room.description)

            command = input("> ").lower().split()
            if command[0] == "go":
                next_room = current_room.go(command[1])
                if next_room:
                    current_room = next_room
                else:
                    print("Неверное направление.")
            elif command[0] == "quit":
                print("До свидания!")
                return
            else:
                print("Неверная команда.")


class DarkRoom(Room):
    def __init__(self):
        super().__init__("Темная комната",
                         "Вы проснулись в темной комнате. Вы не знаете, где вы находитесь. Вы видите дверь справа, окно слева, шкаф напротив и кровать под вами.")

        self.paths = {
            "кровать": StartBed,
            "Стул": StartChair
        }

class StartChair(Room):
    def __init__(self):
        super().__init__("Стул в стартовой комнате", "Обычный деревянный стул. Видимо еще советский.")

        self.paths = {
            "Отойти": DarkRoom
        }

class StartBed(Room):
    def __init__(self):
        super().__init__("Кровать в стартовой комнате", "Кровать")

        self.paths = {
            "Отойти": DarkRoom
        }

start_room = DarkRoom()
game = Game(start_room)
game.play()

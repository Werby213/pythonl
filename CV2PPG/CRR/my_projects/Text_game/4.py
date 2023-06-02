class Room:
    def __init__(self, name, description, items=None, paths=None):
        self.name = name
        self.description = description
        self.items = items or []
        self.paths = paths or {}

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def add_path(self, direction, room):
        self.paths[direction] = room


class Player:
    def __init__(self, current_room):
        self.current_room = current_room
        self.inventory = []

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def remove_from_inventory(self, item):
        self.inventory.remove(item)

    def show_inventory(self):
        if not self.inventory:
            print("Your inventory is empty.")
        else:
            print("Your inventory contains:")
            for item in self.inventory:
                print(item)


class Game:
    def __init__(self, starting_room):
        self.player = Player(starting_room)
        self.health = 100

    def run(self):
        print("Welcome to the game!")
        while self.health > 0:
            current_room = self.player.current_room
            print("You are in the", current_room.name)
            print(current_room.description)

            if current_room.items:
                print("\033[1;33mItems in the room:")
                for item in current_room.items:
                    print(item)
                print("\033[0;0m")

            if current_room.paths:
                print("You can go:")
                for direction, room in current_room.paths.items():
                    print(direction, "to", room.name)

            command = input("> ").strip().lower()

            if command.startswith("/"):
                if command == "/path":
                    print("You are on the path:", self.get_path())
                elif command == "/inv":
                    self.player.show_inventory()
                else:
                    print("Unknown command.")
            else: с
                new_room = current_room.paths.get(command)
                if new_room:
                    self.player.current_room = new_room
                else:
                    print("You can't go that way.")

    def get_path(self):
        path = []
        current_room = self.player.current_room
        while current_room:
            path.append(current_room.name)
            current_room = self.get_previous_room(current_room)
        path.reverse()
        return " -> ".join(path)

    def get_previous_room(self, room):
        for previous_room in self.player.current_room.paths.values():
            if previous_room == room:
                return previous_room
        return None

start_room = Room()
game = Game()
game.play()
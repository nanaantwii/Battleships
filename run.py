import random

class BattleshipsGame:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.player_grid = [['O' for _ in range(grid_size)] for _ in range(grid_size)]
        self.computer_grid = [['O' for _ in range(grid_size)] for _ in range(grid_size)]
        self.player_ships = self.place_ships()
        self.computer_ships = self.place_ships()

    def place_ships(self):
        ships = []
        for _ in range(3):  # Place 3 ships
            ship = (random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1))
            while ship in ships:  # Ensure ships don't overlap
                ship = (random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1))
            ships.append(ship)
        return ships

    def print_grids(self):
        print("\nYour Grid:")
        for row in self.player_grid:
            print(" ".join(row))
        print("\nComputer's Grid:")
        for row in self.computer_grid:
            print(" ".join(row))

    def check_guess(self, guess):
        x, y = guess
        if not (0 <= x < self.grid_size and 0 <= y < self.grid_size):
            print("Warning: Your guess is off-grid!")
            return False
        return True

    def player_turn(self):
        print("\nPlayer's Turn:")
        while True:
            try:
                x = int(input("Enter the row number (0 to {}): ".format(self.grid_size - 1)))
                y = int(input("Enter the column number (0 to {}): ".format(self.grid_size - 1)))
                if not self.check_guess((x, y)):
                    continue
                return x, y
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    def computer_turn(self):
        print("\nComputer's Turn:")
        x = random.randint(0, self.grid_size - 1)
        y = random.randint(0, self.grid_size - 1)
        print("Computer guesses: ({}, {})".format(x, y))
        return x, y

    def play(self):
        print("Welcome to Battleships!")
        self.print_grids()
        while True:
            # Player's turn
            player_guess = self.player_turn()
            if player_guess in self.computer_ships:
                print("Hit! You sank a computer's ship!")
                self.computer_grid[player_guess[0]][player_guess[1]] = 'X'
                self.computer_ships.remove(player_guess)
            else:
                print("Miss!")
                self.computer_grid[player_guess[0]][player_guess[1]] = '-'
            if not self.computer_ships:
                print("Congratulations! You destroyed all computer's ships!")
                break
            self.print_grids()

            # Computer's turn
            computer_guess = self.computer_turn()
            if computer_guess in self.player_ships:
                print("Computer hit your ship at ({}, {})!".format(computer_guess[0], computer_guess[1]))
                self.player_grid[computer_guess[0]][computer_guess[1]] = 'X'
                self.player_ships.remove(computer_guess)
            else:
                print("Computer missed at ({}, {})!".format(computer_guess[0], computer_guess[1]))
                self.player_grid[computer_guess[0]][computer_guess[1]] = '-'
            if not self.player_ships:
                print("Game Over! All your ships are destroyed.")
                break
            self.print_grids()

if __name__ == "__main__":
    grid_size = int(input("Enter the grid size (minimum size is 5): "))
    if grid_size < 5:
        print("Grid size must be at least 5")
    else:
        game = BattleshipsGame(grid_size)
        game.play()

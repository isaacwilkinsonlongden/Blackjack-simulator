from player import Player
from games.blackjack import play_blackjack
from games.slots import play_slots
from utils import clear_screen


def main():
    clear_screen()
    name = input("Enter your name: ")
    player = Player(name)

    while True:
        clear_screen()
        print(f"Welcome to the Casino, {player.name}!")
        print(f"Balance: ${player.balance}")
        print("\n1. Play Blackjack")
        print("2. Play Slots")
        print("3. Quit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            play_blackjack(player)
        elif choice == "2":
            play_slots(player)
        elif choice == "3":
            print("Thank you for playing! Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()

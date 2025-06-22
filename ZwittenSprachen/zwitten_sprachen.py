from ZwittenSprachen.deck_loader import load_deck
import getpass

def study(deck: dict, deck_name: str = None) -> None:
    words = list(deck[deck_name].items())
    transposed = False
    print(f"\nStarting session: {deck_name} ({len(words)} cards)")
    print("Commands: [f]lip  [Enter] next  [b]ack  [q]uit [t]ranspose\n")

    i = 0
    while 0 <= i < len(words):
        prompt, definition = words[i]
        user_input = getpass.getpass(f"{prompt}\n").strip().lower()

        if user_input == "q":
            print("Ending session.")
            break
        elif user_input == "f":
            print(f"\t-> {definition}\n")
            i += 1
            continue
        elif user_input == "b":
            if i > 0:
                i -= 1
            else:
                print("Already at the first card.\n")
        elif user_input == "t":
            transposed = not transposed
            if transposed:
                words = [(v, k) for k, v in deck[deck_name].items()]
            else:
                words = list(deck[deck_name].items())
            print("\nTransposed.\n")
        else:
            i += 1

if __name__ == "__main__":
    deck = load_deck("examples/example_data/german_nouns.yaml")
    study(deck, "German Nouns")
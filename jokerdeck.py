from carddeck import CardDeck
from card import Card

class CardGame:
    def start_game(self):
        print("starting game")

class JokerDeck(CardDeck, CardGame):
    def _make_deck(self):
        super()._make_deck()
        for joker_number in 1, 2:
            joker = Card(f"JOKER{joker_number}", "JOKER")
            self._cards.append(joker)

if __name__ == "__main__":
    j = JokerDeck()
    j.shuffle()
    print(j)
    print(j.cards)
    for i in range(5):
        print(j.draw())
    j.start_game()
    print(JokerDeck.mro())
import unittest

from cards import CardGame


class TestCards(unittest.TestCase):
    """
    Test cases
    """
    def test_all_three_cards_same(self):
        player_cards = {'A': ['2', '2', '2'], 'B': ['Q', 'A', '9'], 'C': ['J', '4', '9'], 'D': ['A', 'J', 'Q']}
        winner = ["A"]
        self.assertEqual(CardGame().start_game(player_cards), winner)

    def test_series_cards_same(self):
        player_cards = {'A': ['A', '2', '2'], 'B': ['Q', 'J', '9'], 'C': ['J', '4', '9'], 'D': ['A', 'J', 'Q']}
        winner = ["B"]
        self.assertEqual(CardGame().start_game(player_cards), winner)

    def test_two_cards_same(self):
        player_cards = {'A': ['A', '2', '2'], 'B': ['Q', 'J', '2'], 'C': ['J', '9', '9'], 'D': ['A', 'J', 'Q']}
        winner = ["C"]
        self.assertEqual(CardGame().start_game(player_cards), winner)

    def test_all_cards_diff(self):
        player_cards = {'A': ['A', 'K', '2'], 'B': ['Q', 'J', '2'], 'C': ['J', '7', '9'], 'D': ['A', 'J', 'Q']}
        winner = ["A"]
        self.assertEqual(CardGame().start_game(player_cards), winner)


if __name__ == '__main__':
    unittest.main()

import random
from functools import cmp_to_key


def sort_data(arr, arr1):
    for i in range(len(arr)-1, -1, -1):
        if arr[1][i] > arr1[1][i]:
            return 1
        elif arr[1][i] < arr1[1][i]:
            return -1
    return 0


class CardGame:
    cards_value = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    cards = {"A": 1, "K": 12, "Q": 11, "J": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}
    cards_order = ["2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K", "A"]

    def __init__(self, num_of_players=4):
        self.num_of_players = num_of_players

    def check_series(self, player_cards):
        """
        Function to check the series of the card
        :param player_cards:
        :return:
        """
        order = []
        for i in player_cards:
            order.append(self.cards_order.index(i))
        # print(order, player_cards)
        order.sort()
        for p in range(0, len(order)-1):
            if order[p] != order[p+1]-1:
                # print("false")
                return False
        # print("true")
        return True

    def check_order(self, player_cards):
        """
        Function to check the order of the order
        :param player_cards:
        :return:
        """
        if len(player_cards) == 3:
            if player_cards[0] == player_cards[1] == player_cards[2]:
                return 1
            elif self.check_series(player_cards):
                return 2
            elif player_cards[0] == player_cards[1] or player_cards[1] == player_cards[2] or \
                    player_cards[0] == player_cards[2]:
                return 3
            else:
                return 4
        return -1

    def get_winner(self, player_cards):
        """
        Function to deciced winner
        :param player_cards:
        :return:
        """
        pld = {}
        player_data = []
        i = 0
        for pl in player_cards:
            player_data.append(sorted([self.cards_order.index(p) for p in player_cards[pl]]))
            pld[pl] = sorted([self.cards_order.index(p) for p in player_cards[pl]])
            i += 1
        result = sorted(pld.items(), key=cmp_to_key(sort_data))
        winner = []
        max_arr = result[len(result)-1]
        winner.append(max_arr[0])
        for i in range(len(result)-2, -1, -1):
            if result[i][1] == max_arr[1]:
                winner.append(result[i][0])
        return winner

    def start_game(self, player_cards=None):
        """
        Function to start game and return winner
        :return:
        """
        num_of_players = self.num_of_players
        total_cards = list(self.cards.keys()) * 4
        if self.num_of_players * 3 > len(total_cards):
            return "Game is not possible"
        if not player_cards:
            player_cards = {}
            for i in range(0, num_of_players):
                player_cards[chr(65+i)] = []

            for pl in player_cards:
                for i in range(0, 3):
                    player_cards[pl].append(total_cards.pop())
                    random.shuffle(total_cards)
        print(player_cards)
        player_rank = {}
        for pl, crs in player_cards.items():
            player_rank[pl] = self.check_order(crs)
        print(player_rank)
        max_order = min(player_rank.values())
        top_players = {}
        for pl, order in player_rank.items():
            if order == max_order:
                top_players[pl] = player_cards[pl]
        winner = self.get_winner(top_players)
        print(winner)
        while len(winner) != 1 and total_cards:
            top_players = {}
            for pl in winner:
                top_players.update({pl: [total_cards.pop()]})
                random.shuffle(total_cards)
            winner = self.get_winner(top_players)
        return winner


if __name__ == "__main__":
    num_of_player = 4
    print(CardGame(num_of_player).start_game())

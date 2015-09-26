__author__ = 'krimeano'


class PokerCard:
    Ranks = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
             '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    # Suits = {'c', 'd', 'h', 's'}

    def __init__(self, txt_value):
        self.txtValue = txt_value
        self.rank = txt_value[0].upper()
        self.suit = txt_value[1].lower()

    def rank_weight(self, alt=False):
        if alt and self.rank == 'A':
            return 1
        if self.rank in self.Ranks:
            return self.Ranks[self.rank]
        return 0

    def __str__(self):
        return self.rank + self.suit


class PokerHand:
    """
High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
    """
    Rankings = ['1', '2', '22', '3', 'S', 'F', '32', '4', 'SF', 'R']

    def __init__(self, cards=''):
        cc = [PokerCard(x) for x in cards.split(' ')]
        self.cards = sorted(cc, key=lambda y: y.rank_weight(), reverse=True)
        self.kinds = []
        self.suits = []
        self.sequences = []
        self.ranking = -1
        self.sub_rankings = []
        self.define_ranking()

    def __str__(self):
        return '[' + ' '.join([str(x) for x in self.cards]) + ']'

    def define_ranking(self):
        self.ranking = 0
        for x in self.cards:
            self.match_kinds(x).match_suits(x).match_sequences(x)

        for x in self.cards:
            if x.rank == 'A':
                self.match_sequences(x, True)

        tf = self.test_flush()
        ts = self.test_straight()

        if len(tf) and len(ts):  # straight flush or royal flush
            if ts[0].rank_weight() == 14:  # royal flush
                self.ranking = 9
                self.sub_rankings = []
            else:
                self.ranking = 8
                self.sub_rankings = [PokerCard.Ranks[ts[0].rank]]
        else:
            tk = self.test_kinds()
            print(tk)
            self.sub_rankings = [PokerCard.Ranks[x[0].rank] for x in tk]

            if len(tk) and len(tk[0]) >= 4:  # four of a kind
                self.ranking = 7
            elif len(tk) > 1 and len(tk[0]) == 3:  # full house
                self.ranking = 6
            elif len(tf):  # flush
                self.ranking = 5
                self.sub_rankings = [PokerCard.Ranks[x.rank] for x in tf]
            elif len(ts):  # straight
                self.ranking = 4
                self.sub_rankings = [PokerCard.Ranks[ts[0].rank]]
            elif len(tk) and len(tk[0]) == 3:  # three of a kind
                self.ranking = 3
            elif len(tk) > 1:  # two pairs
                self.ranking = 2
            elif len(tk):  # pair
                self.ranking = 1
            else:
                self.ranking = 0

        return self

    def match_card_property(self, card, property_name, arr):
        m = False
        for x in arr:
            # print(card, '-'.join(str(c) for c in x))
            for i in range(len(x)):
                if getattr(x[i], property_name) == getattr(card, property_name):
                    m = True
                    x.append(card)
                    break
        if not m:
            arr.append([card])
        return self

    def match_kinds(self, card):
        return self.match_card_property(card=card, property_name='rank', arr=self.kinds)

    def match_suits(self, card):
        return self.match_card_property(card=card, property_name='suit', arr=self.suits)

    def match_sequences(self, card, alt=False):
        arr = self.sequences
        m = False

        def compare_weights(cw, ww):
            return (cw + 1 == min(ww)) or (cw - 1 == max(ww))

        for x in arr:
            if compare_weights(card.rank_weight(alt), [y.rank_weight(alt) for y in x]):
                m = True
                x.append(card)
        if not m:
            arr.append([card])
        return self

    def test_flush(self):
        for x in self.suits:
            if len(x) == 5:
                # self.sub_rankings = [y.rank_weight() for y in x]
                return x
        return []

    def test_straight(self):
        for x in self.sequences:
            if len(x) == 5:
                # self.sub_rankings = [y.rank_weight() for y in x]
                return x
        return []

    def test_kinds_by_number(self, n):
        arr = []
        for x in self.kinds:
            if len(x) == n:
                arr.append(x)
        return arr

    def test_kinds(self):
        return self.test_kinds_by_number(4) + self.test_kinds_by_number(3) + self.test_kinds_by_number(2)


def solve():
    result = 0
    h = PokerHand('5H 5C 6S 7S KD')
    print(h, h.Rankings[h.ranking], h.sub_rankings)
    # print(['-'.join(str(c) for c in x) for x in h.kinds])
    # print(['-'.join(str(c) for c in x) for x in h.suits])
    # print(['-'.join(str(c) for c in x) for x in h.sequences])
    return result


if __name__ == '__main__':
    r = solve()
    print('\n' + '-' * 79)
    print(r)

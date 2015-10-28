class Hand:
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
    Ranks = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
             '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    def __init__(self, cards=list()):
        if len(cards) != 5:
            return
        self.cards = cards
        self.ranks = sorted([Hand.Ranks[x[0].upper()] for x in cards])
        self.suits = set(x[1].lower() for x in cards)
        self.matched_ranks = []
        self.sequence = []
        self.process_ranks()

        self.isFlush = len(self.suits) == 1
        self.isStraight = len(self.sequence) == 5
        self.ranking = self.get_ranking()
        # self.ranking_full = self.calculate_ranking_full()

    def get_ranking(self):
        if self.isFlush and self.isStraight:
            return 8  # straight flush or royal flush
        if len(self.matched_ranks[0]) == 4:
            return 7  # four of a kind
        if len(self.matched_ranks[0]) == 3 and len(self.matched_ranks[1]) == 2:
            return 6  # full house
        if self.isFlush:
            return 5
        if self.isStraight:
            return 4
        if len(self.matched_ranks[0]) == 3:
            return 3
        if len(self.matched_ranks[0]) == 2:
            if len(self.matched_ranks[1]) == 2:
                return 2
            return 1
        return 0

    def process_ranks(self):
        is_sequence = True
        for x in self.ranks:
            is_matching = False
            for yy in self.matched_ranks:
                if x in yy:
                    yy.append(x)
                    is_matching = True
                    break
            if not is_matching:
                self.matched_ranks.append([x])
            if len(self.sequence):
                if x - self.sequence[len(self.sequence) - 1] == 1:
                    self.sequence.append(x)
                elif x == 14 and self.sequence[0] == 2:
                    self.sequence.insert(0, 1)
            else:
                self.sequence.append(x)

        self.matched_ranks = sorted(self.matched_ranks, key=lambda x: len(x))[::-1]
        self.sequence = self.sequence[::-1]

    def calculate_ranking_full(self):
        r = self.ranking * (16 ** 5)
        for i in range(len(self.matched_ranks)):
            r += self.matched_ranks[i][0] * (16 ** (4 - i))
        return r


def solve():
    r = 0
    # # hand = Hand('2C 3D 4H 5S 7C'.split(' '))
    # hand = Hand('AC KC JC QC TC'.split(' '))
    #
    # print(hand.ranks, hand.suits, hand.matched_ranks, hand.sequence, hand.ranking, hand.calculate_ranking_full(),
    #       hex(hand.calculate_ranking_full()))
    with open('p054_poker.txt') as f:
        lines = f.read().splitlines()
    for x in lines:
        cc = x.split(' ')
        hh = [Hand(cc[:5]), Hand(cc[5:])]

        r0, r1 = 0, 0
        if hh[0].ranking > hh[1].ranking:
            r += 1
        elif hh[0].ranking == hh[1].ranking:
            r0, r1 = hh[0].calculate_ranking_full(), hh[1].calculate_ranking_full()
            if r0 > r1:
                r += 1
        print(hh[0].cards, hh[1].cards, r, hh[0].ranking, hh[1].ranking, hex(r0), hex(r1))
    return r


if __name__ == '__main__':
    print(solve())

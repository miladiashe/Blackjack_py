import random


class Player:
    def __init__(self, money):
        self.hand = []
        self.my_money = money
        self.hand_value = 0
        self.status = 0
        # 0일시 살아있음, 1이면 게임오버 등

    def give_card(self, deck):
        if not deck.FullDeck:
            print('temp')
            # 여기다 카드 다 써서 게임을 중단하는 경우를 작성
        else:
            self.hand.append(deck.FullDeck[0])
            del deck.FullDeck[0]

    def display_card(self):
        for i in range(0, len(self.hand)):
            print(self.hand[i].print_card(), end=' ')
        print('\n')

    def count_value(self):
        ace_status = 0
        for i in range(0, len(self.hand)):
            self.hand_value = self.hand_value + self.hand[i].value
            if self.hand[i].isAce:
                ace_status = ace_status + 1
        while ace_status > 0 and self.hand_value > 21:
            self.hand_value = self.hand_value - 10
            ace_status = ace_status - 1

    def declare(self):
        if self.hand_value >= 17:
            return 0
            # stop
        else:
            return 1
            # go

    def win_or_not(self):
        if self.hand_value == 21:
            return 21
        elif self.hand_value > 21:
            return 0
        elif self.hand_value < 21:
            return 1


class Dealer(Player):
    def __init__(self):
        self.hand = []
        self.hand_value = 0
        # 딜러는 판돈과 상태를 갖지 않는다.

    def display_one_card(self):
        print('unknown', end=' ')
        for i in range(1, len(self.hand)):
            print(self.hand[i].print_card(), end=' ')
        print('\n')

    def display_card(self):
        for i in range(0, len(self.hand)):
            print(self.hand[i].print_card(), end=' ')
        print('\n')


class User(Player):
    def declare(self):
        while True:
            go_stop = input('카드를 더 받으시겠습니까? Yes = 1 No = 0')
            if go_stop in [0, 1]:
                return int(go_stop)
            else:
                input('잘못된 입력입니다.')


class Deck:
    def __init__(self, decknum):
        self.FullDeck = []
        for i in range(0, decknum):
            # 사용하는 카드 벌 수에 맞춰 반복
            # 카드 한 벌 생성
            for suit in ['spade', 'diamond', 'heart', 'club']:
                for num in range(1, 14):
                    # print(type(num))
                    self.FullDeck.append(Card(num, suit))
        random.shuffle(self.FullDeck)

    # def shuffle(self):
    # def return_deck(self):
    #     for i in self.FullDeck:
    #         print(i.number, i.suit)


class Card:
    def __init__(self, num, suit):
        if isinstance(num, int):
            self.number = num
        else:
            self.number = 0
        # 카드에 들어갈 숫자가 정수인지 판별
        if self.number == 1:
            self.isAce = True
        else:
            self.isAce = False
        # 에이스인지 여부 저장
        if self.number >= 11:
            self.value = 10
        elif self.isAce:
            self.value = 11
        else:
            self.value = self.number
        # 카드의 가치를 저장하는 변수
        if suit in ['spade', 'diamond', 'heart', 'club']:
            self.suit = suit
        # 카드 무늬 저장

    def print_card(self):
        visual_suit = '무늬 없음'

        if self.suit == 'spade':
            visual_suit = '♠'
        elif self.suit == 'diamond':
            visual_suit = '◇'
        elif self.suit == 'heart':
            visual_suit = '♥'
        elif self.suit == 'club':
            visual_suit = '♧'

        if self.number == 1:
            visual_num = 'A'
        elif self.number == 11:
            visual_num = 'J'
        elif self.number == 12:
            visual_num = 'Q'
        elif self.number == 13:
            visual_num = 'K'
        else:
            visual_num = str(self.number)
        return visual_suit + ' ' + visual_num
        # 카드를 출력하는 함수

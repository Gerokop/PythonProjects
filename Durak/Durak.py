import random
import operator
        
class Deck:

    decks = []


    def __init__(self):

        self.lastturn = None
        self.cards_in_deck = []
        self.decks.append(self)       
        for i in range(0,4):           
            for j in range(0,9):                
               self.cards_in_deck.append(Card(j,i))                
        random.shuffle(self.cards_in_deck)
        k1 = self.cards_in_deck[-1].suit
        self.K = k1
   
class Hand:

    hands = []

    def __init__(self,name):

        self.turn = False
        self.name = name
        self.hand_list = [] #Что в руке
        self.go = False

    def __repr__(self):

        self.name = str(self.name)

        return self.name

        
class Card:
    
    suits = ['♠Пики♠','♥Черви♥','♦Буби♦','♣Крести♣']
    
    values = ['6','7','8','9','10','Валет','Дама','Король','Туз']


    
    def __init__(self,v,s):
        
        self.value = v        
        self.suit = s

    def __lt__(self,c2):
        
        k = Deck.decks[0].K
        if self.suit == k and c2.suit != k:
            return False
        if self.suit == k and c2.suit == k:
            if self.value < c2.value:
                return True
            else:
                return False
        if self.suit != k and c2.suit == k:
            return True
        if self.suit != k and c2.suit != k:
            if self.value < c2.value:
                return True
            else:
                return False
        
    def __gt__(self,c2):
        
        k = Deck.decks[0].K
        if self.suit == k and c2.suit != k:
            return True
        elif self.suit == k and c2.suit == k:
            if self.value > c2.value:
                return True
            else:
                return False
        elif self.suit != k and c2.suit == k:
            return False
        elif self.suit != k and c2.suit != k:
            if self.suit > c2.suit:
                return True
            else:
                return False
    def __repr__(self):
        
        self.name = self.values[self.value] + ' ' + self.suits[self.suit]
        return self.name
    
class Game:
    
    def __init__(self):
        
        self.table = []
        self.players_count = input('Сколько Игроков?(пока доступно только 2): ')
        self.players_count = int(self.players_count)
        for i in range(0,self.players_count):
            name = input('Введите имя {}-ого игрока: '.format(i+1))
            Hand.hands.append(Hand(name))
        self.notError = False

    def startgame(self):
        
        for h in Hand.hands:
            for i in range(0,6):
                self.draw(h,'-')        
        self.what_player_starts()

        print('Козырь: {}'.format(Card.suits[Deck.decks[0].K]))

        self.flist()

        self.this_turn()
                
    def draw(self,h,turn):
        if turn == '+':
            for h in Hand.hands:
                if h.turn == True:                    
                    while h.hand_list.index(h.hand_list[-1])< 5:
                        self.draw(h,'-')
                else:
                    while h.hand_list.index(h.hand_list[-1])< 5:
                        self.draw(h,'-')
        else:
            if Deck.decks[0].cards_in_deck != []:
                h.hand_list.append(Deck.decks[0].cards_in_deck[0])        
                del Deck.decks[0].cards_in_deck[0]
            else:
                pass
        
    def what_player_starts(self):
        
        kosiri = []
        for h in Hand.hands:
            for c in h.hand_list:
                if c.suit == Deck.decks[0].K:
                    kosiri.append(c)
        kosiri = sorted(kosiri)
        if kosiri != []:           
            for h in Hand.hands:
                for card in h.hand_list:
                    if card == kosiri[0]:
                        h.turn = True
        else:
            i = random.randrange(0,self.players_count)
            Hand.hands[i].turn = True
        del kosiri

    def this_turn(self):
        self.checkwin()
        for h in Hand.hands:
            if h.turn == True:
                z = Hand.hands.index(h)
                self.space(4)
                print(input('Нажмите Enter чтобы передать управление\
 игроку под именем {}'.format(h.name)))
                self.space(20)
                self.info(h)
                answer = input('Напишите какую карту по списку бросить: ')
                answer = int(answer)
                self.table.append(h.hand_list[answer-1])
                del h.hand_list[answer-1]
            else:
                j = Hand.hands.index(h)
        Hand.hands[z].turn = False
        Hand.hands[j].turn = True
        self.checkwin
        do_not_turn = False
        self.space(3)
        print(input('Нажмите Enter чтобы передать управление другому игроку '))
        self.space(20)
        for h in Hand.hands:
            if h.turn == True:
                self.info(h)
                answer = input('Введите номер карты по списку или "Беру"\
 если берете карты: ')
                answer = answer.strip()
                answer = answer.upper()
                print(answer)
                if answer != 'БЕРУ' and answer != 'БЕРУ!':
                    answer = int(answer)
                    answer -= 1
                    if self.table[-1] < h.hand_list[answer]:
                        self.table.append(h.hand_list[answer])
                        del h.hand_list[answer]
                    else:
                        print('Извините, но вы должны кинуть большую карту\
 или козырь')
                else:
                    for c in self.table:
                        i = self.table.index(c)
                        h.hand_list.append(self.table[i])
                        del self.table[i]
                    do_not_turn = True
        portal = False
        Hand.hands[z].turn = True
        Hand.hands[j].turn = False
        if do_not_turn != True:
            for h in Hand.hands:
                if h.turn == True:
                    print(input('Нажмите Enter передать управление д\
ругому игроку'))
                    self.info(h)
                    answer2 = input('Введите номер карты по списку \
которую хотите доложить или напишите "Бито!": ')
                    if answer2 != 'Бито!' and answer2 != 'Бито':
                        answer2 = int(answer2)
                        for c in self.table:
                            if h.hand_list[answer2].value == c.value:
                                self.table.append(h.hand_list[answer2])
                                del h.hand_list[answer2]
                                portal = True
                            else:
                                print(input('Введите действительную карту или\
 напишите Бито'))
                    else:
                        self.table = []
                        self.draw(h,'+')
                        Hand.hands[z].turn = False
                        Hand.hands[j].turn = True
                        self.this_turn()
        else:
            
            print('kak')
            self.draw(h,'+')
            self.this_turn()
        if portal == True:
            self.this_turn()
                    
                                                    
    def flist(self):

        print(Hand.hands)
        print(Hand.hands[0].hand_list)
        print(Hand.hands[1].hand_list)
        print(Deck.decks[0].cards_in_deck)

    def space(self,count):

        for i in range(0,count):
            print('\n')

    def checkwin(self):
        for h in Hand.hands:
            if h.hand_list == [] and self.table == []:
                print(input('{} Победил! У него не осталось карт в руке,\
 поздравляем!'.format(h.name)))
        else:
            pass

    def info(self,hand):
        
        self.space(3)
        print('Ходит игрок под именем: ', hand.name)
        self.space(3)
        print('Последняя карта в колоде: ', Deck.decks[0].cards_in_deck[-1])
        self.space(3)
        print('Козырь: ', Card.suits[Deck.decks[0].K])
        self.space(3)
        show = ['Стол: ']
        for card in self.table:
            show.append(card.name)
        show = ' , '.join(show)
        print(show)
        show = []
        self.space(3)
        show = ['Ваша рука: ']
        for card in hand.hand_list:
            show.append(card.name)
        show = ' , '.join(show)
        print(show)
        show = []

        self.space(3)

deck1 = Deck()
game1 = Game()
game1.startgame()






        

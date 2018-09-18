def proverka(x):
    print(x)
    input('')
def probel(i=5):
    for i in range(0,i):
        print('\n')
def igra():
    Chelik = ('',
              '______    ',
              '      |   ',
              '      O   ',
              '     /|\  ',
              '    / | \ ',
              '     / \  ',
              '    /   \ '
              )
    ChelikWin = ('     Ураа!',
                '      /   ',
                '  \  O  / ',
                '   \ | /  ',
                '     |    ',
                '    / \   ',
                '   /   \  ',
               )
    for c in Chelik[1:8]:
        print(c)
    print('''Приветствуем вас в игре виселица!\n
Особенности игры таковы:
    1)Игрок1 загадывает слово и пишет его в строке а Игрок2
должен его отгадать.
    2)У Игрока2 есть 5 попыток чтобы отгадать слово.
    3)Как только Игрок1 напишет загаданное слово оно пропадет и Игрок2
не сможет подглядеть его.
    4)Игрок2 может писать только по 1 букве''')
    word = input('Введите слово: ')
    word = word.upper()
    word = '+'.join(word)
    word = word.split('+')
    for i in range(0,21):
        print('\n')
    win = 0 
    lose = 3 #Сколько будет челика
    otg = 0 #за каждую отг букву увеличить на 1
    kol = [' ___ '] * len(word)
    listF = []


    while True:
        otg1 = otg + 1
        for c in Chelik[1:lose]:
            print(c)
        probel()
        print(kol)
        probel()
        if ' ___ ' not in kol:
            print ("Поздравляем! Победа!")
            probel()
            for c in ChelikWin[0:8]:
                print(c)
            probel(4)
            input('Нажмите Enter чтобы выйти: ')
            break
        elif lose == 8:
            print ('Вы проиграли :(')
            probel()
            for c in Chelik[1:8]:
                print(c)
            probel(4)
            input('Нажмите Enter чтобы выйти: ')
            break
        slov = input('Буква: ') #Буква сказанная игроком
        slov = slov.upper()
        probel(4)
        if slov in word and slov not in listF:
            listF.append(slov)
            while slov in word:
                x = word.index(slov)
                kol[x] = slov
                word[x] = '^'
            otg += 1
            print('Правильно!')
            probel(2)
        elif slov in listF:
            print('Вы уже отгадали эту букву. Попробуйте еще')
            continue
        else:
            lose += 1
            print('Неправильно!')
            probel(2)

igra()

#imports
import random
from time import sleep
import os
from colorama import Fore as f
from colorama import Style as s
#update
#vars
money = 100
playerHand = {"cards":[], "count":0}
dealerHand = {"cards":[], "count":0}
glitchy = "\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff\u0100\u0101\u0102\u0103\u0104\u0105\u0106\u0107\u0108\u0109\u010a\u010b\u010c\u010d\u010e\u010f\u0110\u0111\u0112\u0113\u0114\u0115\u0116\u0117\u0118\u0119\u011a\u011b\u011c\u011d\u011e\u011f\u0120\u0121\u0122\u0123\u0124\u0125\u0126\u0127\u0128\u0129\u012a\u012b\u012c\u012d\u012e\u012f\u0130\u0131\u0132\u0133\u0134\u0135\u0136\u0137\u0138\u0139\u013a\u013b\u013c\u013d\u013e\u013f\u0140\u0141\u0142\u0143\u0144\u0145\u0146\u0147\u0148\u0149\u014a\u014b\u014c\u014d\u014e\u014f\u0150\u0151\u0152\u0153\u0154\u0155\u0156\u0157\u0158\u0159\u015a\u015b\u015c\u015d\u015e\u015f\u0160\u0161\u0162\u0163\u0164\u0165\u0166\u0167\u0168\u0169\u016a\u016b\u016c\u016d\u016e\u016f\u0170\u0171\u0172\u0173\u0174\u0175\u0176\u0177\u0178\u0179\u017a\u017b\u017c\u017d\u017e"
class Card:
    def __init__(self, value, color):
        self.value = value
        self.suit = color
suits = ['hearts', 'diamonds', 'spades', 'clubs']
digits = ['ace', "2", '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
deck = [Card(value, color) for value in digits for color in suits]

# functions 
def dealerreveal(hand=dealerHand, st=1.5):
  firstcard = hand['cards'][0]
  secondcard = hand['cards'][1]
  clear()
  print("Dealer: " + glitchtext(10) + ' , ' + glitchtext(10))
  print('Dealer Total: 0\n')
  print(f'You: {showCards(playerHand)}')
  print(f'Total: {playerHand["count"]}\n')
  sleep(st)
  clear()
  print("Dealer: " + showCard(firstcard) + ' , ' + glitchtext(10))
  print(f'Dealer Total: {getValue(firstcard, dealerHand)}\n')
  print(f'You: {showCards(playerHand)}')
  print(f'Total: {playerHand["count"]}\n')
  sleep(st)
  clear()
  print(f"Dealer: {showCards(dealerHand)}")
  print(f'Dealer Total: {getValue(firstcard, dealerHand)+getValue(secondcard, dealerHand)}\n')
  print(f'You: {showCards(playerHand)}')
  print(f'Total: {playerHand["count"]}\n')
  
def glitchtext(length): # Thanks daniel macarthur ( http://dmacarthur.uk/python-glitch-text/ )
    output = ""
    for x in range(length):
        output += random.choice(glitchy)
    return output
def clear():
   if os.name == 'nt':
      os.system('cls')
   else:
     os.system('clear')
def gameloop():
  global money
  clear()
  print("Dealer: " + glitchtext(10) + ' , ' + glitchtext(10))
  print(f'Dealer Total: {glitchtext(5)}\n')
  print(f'You: {showCards(playerHand)}')
  print(f'Total: {playerHand["count"]}\n')
  print("What do you want to do?")
  print(f.GREEN+'1. Hit'+f.WHITE)
  print(f.RED+'2. Stand'+f.WHITE)
  while True:
    choice = input("|>")
    try: int(choice)
    except Exception: print(f.RED+"That's not a valid choice"+f.WHITE); continue
    if int(choice) == 1: break
    elif int(choice) == 2: break
    else: print(f.RED+"That's not a valid choice"+f.WHITE); continue
  if int(choice) == 1:
    newcard = hit()
    playerHand['cards'].append(newcard)
    playerHand['count'] += getValue(newcard)
    if playerHand['count'] > 21:
      clear()
      print("Dealer: " + glitchtext(10) + ' , ' + glitchtext(10))
      print(f'Dealer Total: {glitchtext(5)}\n')
      print(f'You: {showCard(playerHand["cards"][0])}, {showCard(playerHand["cards"][1])}')
      print(f'Total: {playerHand["count"]}\n')
      print(s.DIM+'BUST!'+s.RESET_ALL)
      print("Press enter to restart.")
      input('|>')
      clear()
      return False
  else:
    print("stand")
    dealerreveal()
    while True:
      choice = dealersTurn(dealerHand)
      sleep(1.5)
      clear()
      print(f"Dealer: {showCards(dealerHand)}")
      print(f'Dealer Total: {dealerHand["count"]}\n')
      print(f'You: {showCards(playerHand)}')
      print(f'Total: {playerHand["count"]}\n')
      if choice == 'hit':
        newcard = hit()
        dealerHand['cards'].append(newcard)
        dealerHand['count'] += getValue(newcard)
        if dealerHand['count'] > 21:
          clear()
          print(f"Dealer: {showCards(dealerHand)}")
          print(f'Dealer Total: {dealerHand["count"]}\n')
          print(f'You: {showCards(playerHand)}')
          print(f'Total: {playerHand["count"]}\n')
          print(f.GREEN+"Dealer Bust!"+f.WHITE)
          money += bet*2
          print("You win " + str(bet*2) + " dollars!")
          print("Your updated money: " + str(money))
          print('Press enter to restart')
          input('|>')
          clear()
          break
      elif choice == "stand":
        if dealerHand['count'] > playerHand['count']:
          clear()
          print(f"Dealer: {showCards(dealerHand)}")
          print(f'Dealer Total: {dealerHand["count"]}\n')
          print(f'You: {showCards(playerHand)}')
          print(f'Total: {playerHand["count"]}\n')
          print(f.RED+"Dealer wins!"+f.WHITE)
          print('Press enter to restart')
          input('|>')
          clear()
          break
        elif dealerHand['count'] == playerHand['count']:
          clear()
          print(f"Dealer: {showCards(dealerHand)}")
          print(f'Dealer Total: {dealerHand["count"]}\n')
          print(f'You: {showCards(playerHand)}')
          print(f'Total: {playerHand["count"]}\n')
          print(s.DIM+"Tie!"+s.RESET_ALL)
          print("You get " + str(bet) + 'back.')
          money += bet
          print("Your updated total: " + str(money))
          print('Press enter to restart')
          input('|>')
          clear()
          break
        else:
          clear()
          print(f"Dealer: {showCards(dealerHand)}")
          print(f'Dealer Total: {dealerHand["count"]}\n')
          print(f'You: {showCards(playerHand)}')
          print(f'Total: {playerHand["count"]}\n')
          print(f.GREEN+"You Win!"+f.WHITE)
          money += bet*2
          print("You win " + str(bet*2) + " dollars!")
          print("Your updated money: " + str(money))
          print('Press enter to restart')
          input('|>')
          clear()
          break
    return "break"
def split():
  global money
  global playerHand
  global bet
  global dealerHand
  print("Dealer: " + glitchtext(10) + ' , ' + glitchtext(10))
  print(f'Dealer Total: {glitchtext(5)}\n')
  print(f'You: {showCard(playerHand["cards"][0])}, {showCard(playerHand["cards"][1])}')
  print(f'Total: {playerHand["count"]}\n')
  print("What do you want to do?")
  print(f.GREEN+'1. Hit'+f.WHITE)
  print(f.BLUE+'2. Double'+f.WHITE)
  print(f.YELLOW+'3. Split'+f.WHITE)
  print(f.RED+'4. Stand'+f.WHITE)
  while True:
    choice = input('|>')
    try: int(choice)
    except Exception: print(f.RED+'Thats not an option!'+f.WHITE); continue
    if int(choice) == 1: break
    elif int(choice) == 2: 
      if bet > money: 
        print(f.RED+"You can't bet more than you have!"+f.WHITE); continue
      else: break
    elif int(choice) == 3: break
    elif int(choice) == 4: break
    else: print(f.RED+"That's not a valid choice"+f.WHITE); continue
  if int(choice) == 2:
    money -= bet
    bet += bet
  if int(choice) == 1 or int(choice) == 2:
    newcard = hit()
    playerHand['cards'].append(newcard)
    playerHand['count'] += getValue(newcard)
    if playerHand['count'] > 21:
      clear()
      print("Dealer: " + glitchtext(10) + ' , ' + glitchtext(10))
      print(f'Dealer Total: {glitchtext(5)}\n')
      print(f'You: {showCards(playerHand)}')
      print(f'Total: {playerHand["count"]}\n')
      print(s.DIM+'BUST!'+s.RESET_ALL)
      print("Press enter to restart.")
      input('|>')
      clear()
    else: 
      while True:
        t = gameloop()
        if t == False:
          break
        elif t == 'break':
          break
        elif t == "blackjack":
          print(f.GREEN+"Blackjack!"+f.WHITE)
          money += bet*2
          print("You win " + str(bet*2) + " dollars!")
          print("Your updated money: " + str(money))
          print('Press enter to restart')
          input('|>')
          clear()
          break
        else: 
          continue
  elif int(choice) == 3: 
    playerHand = {
      "count1":getValue(playerHand['cards'][0]),
      "count2":getValue(playerHand['cards'][1]),
      "cards1":[playerHand['cards'][0]],
      "cards2":[playerHand['cards'][1]]
    }
    print("Dealer: " + glitchtext(10) + ' , ' + glitchtext(10))
    print(f'Dealer Total: {glitchtext(5)}\n')
    print("Your hands:")
    showHand1 = showCards(playerHand['cards1'])
    print(f'Hand 1: {showHand1}')
    print(f'Total: {playerHand["count1"]}')
    print(s.DIM+f"Hand 2: {showCards(playerHand['cards2'])}"+s.RESET_ALL)
    print(f'Total: {playerHand["count2"]}')
  elif int(choice) == 4:
    print("stand")
    dealerreveal()
    while True:
      choice = dealersTurn(dealerHand)
      sleep(1.5)
      clear()
      print(f"Dealer: {showCards(dealerHand)}")
      print(f'Dealer Total: {dealerHand["count"]}\n')
      print(f'You: {showCards(playerHand)}')
      print(f'Total: {playerHand["count"]}\n')
      if choice == 'hit':
        newcard = hit()
        dealerHand['cards'].append(newcard)
        dealerHand['count'] += getValue(newcard)
        if dealerHand['count'] > 21:
          clear()
          print(f"Dealer: {showCards(dealerHand)}")
          print(f'Dealer Total: {dealerHand["count"]}\n')
          print(f'You: {showCards(playerHand)}')
          print(f'Total: {playerHand["count"]}\n')
          print(f.GREEN+"Dealer Bust!"+f.WHITE)
          money += bet*2
          print("You win " + str(bet*2) + " dollars!")
          print("Your updated money: " + str(money))
          print('Press enter to restart')
          input('|>')
          clear()
          break
      elif choice == "stand":
        if dealerHand['count'] > playerHand['count']:
          clear()
          print(f"Dealer: {showCards(dealerHand)}")
          print(f'Dealer Total: {dealerHand["count"]}\n')
          print(f'You: {showCards(playerHand)}')
          print(f'Total: {playerHand["count"]}\n')
          print(f.RED+"Dealer wins!"+f.WHITE)
          print('Press enter to restart')
          input('|>')
          clear()
          break
        elif dealerHand['count'] == playerHand['count']:
          clear()
          print(f"Dealer: {showCards(dealerHand)}")
          print(f'Dealer Total: {dealerHand["count"]}\n')
          print(f'You: {showCards(playerHand)}')
          print(f'Total: {playerHand["count"]}\n')
          print(s.DIM+"Tie!"+s.RESET_ALL)
          print("You get " + str(bet) + 'back.')
          money += bet
          print("Your updated total: " + str(money))
          print('Press enter to restart')
          input('|>')
          clear()
          break
        else:
          clear()
          print(f"Dealer: {showCards(dealerHand)}")
          print(f'Dealer Total: {dealerHand["count"]}\n')
          print(f'You: {showCards(playerHand)}')
          print(f'Total: {playerHand["count"]}\n')
          print(f.GREEN+"You Win!"+f.WHITE)
          money += bet*2
          print("You win " + str(bet*2) + " dollars!")
          print("Your updated money: " + str(money))
          print('Press enter to restart')
          input('|>')
          clear()
          break
    
def showCards(hand):
  string = ""
  for item in hand['cards']:
    string = string + showCard(item) + ', '
  return string[:-2]
def showCard(card):
  return card.value + ' of ' + card.suit
def getValue(card, hand=playerHand):
  if card.value == 'ace': 
    if hand["count"] < 11:
      return 11
    else:
      return 1
  elif card.value == 'jack' or card.value == "queen" or card.value == "king": return 10
  else: return int(card.value)

def hit():
  return deck[random.randint(0, len(deck)-1)]
  
def dealersTurn(hand):
  if hand["count"] <= 16:
    return 'hit'
  if hand["count"] >= 17:
    return 'stand'

while True:
  
  #Create starting hands
  pcard1, pcard2 = hit(), hit()
  playerHand["cards"] = [pcard1, pcard2]
  playerHand["count"] = getValue(pcard1)
  playerHand["count"] += getValue(pcard2)
  dcard1, dcard2 = hit(), hit()
  dealerHand['cards'] = [dcard1, dcard2]
  dealerHand['count'] = getValue(dcard1, dealerHand)
  dealerHand['count'] += getValue(dcard2, dealerHand)
  #bet 
  while True:
    print(f"How much would you like to bet? Current Money: {money}")
    bet = input('|>')
    try: float(bet)
    except Exception: clear(); continue 
    if float(bet) > money: clear(); continue
    if float(bet) < 0: continue
    print("Successfully bet " + bet); bet = float(bet); money -= bet;
    print("Your updated total: " + str(money) + "\n"); break
  
      
  #choose ai
  while True:
    print('How would you like to play:\n   -1. Human VS Dealer\n   -2. AI VS Dealer')
    #playas = input("|>")
    playas = 1
    try: int(playas)
    except Exception: clear(); continue
    if int(playas) != 1 and int(playas) != 2: clear()
    else: break
  
  #Human VS AI
  if int(playas) == 1:
    clear()
    if playerHand['count'] == 21:
      print("Dealer: " + glitchtext(10) + ' , ' + glitchtext(10))
      print(f'Dealer Total: {glitchtext(5)}\n')
      print(f'You: {showCards(playerHand)}')
      print(f'Total: {playerHand["count"]}\n')
      print(f.GREEN+"Blackjack!"+f.WHITE)
      money += bet*2.50
      print("You win " + str(bet*2.50) + " dollars!")
      print("Your updated money: " + str(money))
      print('Press enter to restart')
      input('|>')
      clear()
      continue
    elif getValue(playerHand['cards'][0]) == getValue(playerHand['cards'][1]):
      split()
    else: 
      print("Dealer: " + glitchtext(10) + ' , ' + glitchtext(10))
      print(f'Dealer Total: {glitchtext(5)}\n')
      print(f'You: {showCards(playerHand)}')
      print(f'Total: {playerHand["count"]}\n')
      print("What do you want to do?")
      print(f.GREEN+'1. Hit'+f.WHITE)
      print(f.BLUE+'2. Double'+f.WHITE)
      print(f.RED+'3. Stand'+f.WHITE)
      while True:
        choice = input("|>")
        try: int(choice)
        except Exception: print(f.RED+"That's not a valid choice"+f.WHITE); continue
        if int(choice) == 1: break
        elif int(choice) == 2: 
          if bet > money: 
            print(f.RED+"You can't bet more than you have!"+f.WHITE); continue
          else: break
        elif int(choice) == 3: break
        else: print(f.RED+"That's not a valid choice"+f.WHITE); continue
      if int(choice) == 2:
        bet = bet*2
        money -= bet
      if int(choice) == 1 or int(choice) == 2:
        newcard = hit()
        playerHand['cards'].append(newcard)
        playerHand['count'] += getValue(newcard)
        if playerHand['count'] > 21:
          clear()
          print("Dealer: " + glitchtext(10) + ' , ' + glitchtext(10))
          print(f'Dealer Total: {glitchtext(5)}\n')
          print(f'You: {showCards(playerHand)}')
          print(f'Total: {playerHand["count"]}\n')
          print(s.DIM+'BUST!'+s.RESET_ALL)
          print("Press enter to restart.")
          input('|>')
          clear()
          continue
        else: 
          while True:
            t = gameloop()
            if t == False:
              break
            elif t == 'break':
              break
            elif t == "blackjack":
              print(f.GREEN+"Blackjack!"+f.WHITE)
              money += bet*2
              print("You win " + str(bet*2) + " dollars!")
              print("Your updated money: " + str(money))
              print('Press enter to restart')
              input('|>')
              clear()
              break
            else: 
              continue
      elif int(choice) == 3:
        print("stand")
        dealerreveal()
        while True:
          choice = dealersTurn(dealerHand)
          sleep(1.5)
          clear()
          print(f"Dealer: {showCards(dealerHand)}")
          print(f'Dealer Total: {dealerHand["count"]}\n')
          print(f'You: {showCards(playerHand)}')
          print(f'Total: {playerHand["count"]}\n')
          if choice == 'hit':
            newcard = hit()
            dealerHand['cards'].append(newcard)
            dealerHand['count'] += getValue(newcard)
            if dealerHand['count'] > 21:
              clear()
              print(f"Dealer: {showCards(dealerHand)}")
              print(f'Dealer Total: {dealerHand["count"]}\n')
              print(f'You: {showCards(playerHand)}')
              print(f'Total: {playerHand["count"]}\n')
              print(f.GREEN+"Dealer Bust!"+f.WHITE)
              money += bet*2
              print("You win " + str(bet*2) + " dollars!")
              print("Your updated money: " + str(money))
              print('Press enter to restart')
              input('|>')
              clear()
              break
          elif choice == "stand":
            if dealerHand['count'] > playerHand['count']:
              clear()
              print(f"Dealer: {showCards(dealerHand)}")
              print(f'Dealer Total: {dealerHand["count"]}\n')
              print(f'You: {showCards(playerHand)}')
              print(f'Total: {playerHand["count"]}\n')
              print(f.RED+"Dealer wins!"+f.WHITE)
              print('Press enter to restart')
              input('|>')
              clear()
              break
            elif dealerHand['count'] == playerHand['count']:
              clear()
              print(f"Dealer: {showCards(dealerHand)}")
              print(f'Dealer Total: {dealerHand["count"]}\n')
              print(f'You: {showCards(playerHand)}')
              print(f'Total: {playerHand["count"]}\n')
              print(s.DIM+"Tie!"+s.RESET_ALL)
              print("You get " + str(bet) + ' back.')
              money += bet
              print("Your updated total: " + str(money))
              print('Press enter to restart')
              input('|>')
              clear()
              break
            else:
              clear()
              print(f"Dealer: {showCards(dealerHand)}")
              print(f'Dealer Total: {dealerHand["count"]}\n')
              print(f'You: {showCards(playerHand)}')
              print(f'Total: {playerHand["count"]}\n')
              print(f.GREEN+"You Win!"+f.WHITE)
              money += bet*2
              print("You win " + str(bet*2) + " dollars!")
              print("Your updated money: " + str(money))
              print('Press enter to restart')
              input('|>')
              clear()
              break
  

  # AI VS AI
  elif int(playas) == 2:
    print('No')
import random
import itertools

deck = list(itertools.product(['Ace','King','Queen','Joker','Ten','Nine','Eight','Seven','Six','Five','Four','Three','Two'],
							  ['Spades','Hearts','Diamonds','Clubs']))

player1 = []
player2 = []
random.shuffle(deck)

card_rank_lookup = {
	"Ace": 14,
	"King": 13,
	"Queen": 12,
	"Joker": 11,
	"Ten": 10,
	"Nine": 9,
	"Eight": 8,
	"Seven": 7,
	"Six": 6,
	"Five": 5,
	"Four": 4,
	"Three": 3,
	"Two": 2
	
}
card_color_lookup = {
	"Spades": 4,
	"Hearts": 3,
	"Diamonds": 2,
	"Clubs": 1
}

class Card:
	def __init__(self):
		color = ""
		number = ""
		rank = 0
	def __str__(self):
		return self.color + " " + self.number + " " + str(self.rank)

	
def generate_deck_player1():
	print("player 1 deck is below")
#	global player1
	for i in range(26):
		obj_card = Card()
		obj_card.color = deck[i][1]
		obj_card.number = deck[i][0]
		obj_card.rank = card_rank_lookup[deck[i][0]]
		player1.append(obj_card)
		deck.remove(deck[i])
		print(str(obj_card))
		
def generate_deck_player2():
	print("Player 2 deck is below")
#	global player2
	for j in range(26):
		obj_card = Card()
		obj_card.color = deck[j][1]
		obj_card.number = deck[j][0]
		obj_card.rank = card_rank_lookup[deck[j][0]]
		player2.append(obj_card)
		print(str(obj_card))
	

def card_compare(card1, card2):
	if card1.rank > card2.rank:
		return 1
	elif card2.rank > card1.rank:
		return -1
	else:
		if card_color_lookup[card1.color] > card_color_lookup[card2.color]:
			return 1
		elif card_color_lookup[card1.color] < card_color_lookup[card2.color]:
			return -1
		else:
			return 0
def kachuful():
	count1 = 0
	count2 = 0
	generate_deck_player1()
	generate_deck_player2()
	for i in range(26):
		obj_player1 = player1[i]
		obj_player2 = player2[i]
		result = card_compare(obj_player1,obj_player2)
		if result == 1:
			count1 += 1
		elif result == -1:
			count2 += 1
	if 	count1 > count2:
		print("player 1 won")
	elif count2 > count1:
		print("player 2 won")
	else:
		print("TIE")
	

if __name__ == '__main__':
	kachuful()


#!/usr/bin/env python3

# Ax + Bx + C + Dx = E + Fx + G
# Rules A-H must be 1-9 each number used at most 1 time

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# print helper function
def pf(x):
	print(x, flush=True)
	return

# returns remaning cards after excluding passed in card
def remainingCards(exclude_card, cl):
	cardList = range(0,len(cl))
	remaingCards = []

	for a in cardList:
		if (exclude_card != a):
			remaingCards.append(cl[a])

	return remaingCards

# count how many loops were run
count = 0

# start loop with all cards
aCards = cards
aCardsR = range(0, len(aCards))

for a in aCardsR:
	# remove card A from deck
	bCards = remainingCards(a, aCards)
	bCardsR = range(0, len(bCards))
   
	for b in bCardsR:
		# remove card B from deck
		cCards = remainingCards(b, bCards)
		cCardsR = range(0, len(cCards))
	
		for c in cCardsR:
			dCards = remainingCards(c, cCards)
			dCardsR = range(0, len(dCards))
		
			for d in dCardsR:
				eCards = remainingCards(d, dCards)
				eCardsR = range(0, len(eCards))
			
				for e in eCardsR:
					fCards = remainingCards(e, eCards)
					fCardsR = range(0, len(fCards))
				
					for f in fCardsR:
						gCards = remainingCards(f, fCards)
						gCardsR = range(0, len(gCards))
					
						for g in gCardsR:
							# convert card value to strings to match equation
							answerString = str(aCards[a]) + "x + " + str(bCards[b]) + "x + " + str(cCards[c]) + " + " + str(dCards[d]) + "x = " + str(eCards[e]) + " + " + str(fCards[f]) + "x + " + str(gCards[g])
							count = count + 1

							# EQ: # Ax + Bx + C + Dx = E + Fx + G
							# LeftX = Ax+Bx + Dx
							# LeftConst = C
							# RightX = Fx
							# RightConst = E+G

							# assign valus to like terms for each side of the equation
							leftX = aCards[a]+bCards[b]+dCards[d]
							leftConst = cCards[c]
							rightX = fCards[f]
							rightConst = eCards[e]+gCards[g]

							# prints if the all the like terms are equal
							if ((leftX == rightX) and (leftConst == rightConst)):
								pf(answerString)

pf(str(count)+ " loops were run.")


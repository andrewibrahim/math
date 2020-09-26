#!/usr/bin/env python3

# Ax + Bx + C + Dx = E + Fx + G
# Rules A-H must be 1-9 each number used at most 1 time

#cards = [1, 2, 3, 4, 5, 6, 7, 8, 9]
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def pf(x):
	print(x, flush=True)
	return

def remainingCards(c, cl):
	cardList = range(0,len(cl))
	remaingCards = []

	for a in cardList:
		if (c != a):
			remaingCards.append(cl[a])

	return remaingCards


aCards = cards
aCardsR = range(0, len(aCards))

for a in aCardsR:
	bCards = remainingCards(a, aCards)
	bCardsR = range(0, len(bCards))
   
	for b in bCardsR:
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

							answerString = str(aCards[a]) + "x + " + str(bCards[b]) + "x + " + str(cCards[c]) + " + " + str(dCards[d]) + "x = " + str(eCards[e]) + " + " + str(fCards[f]) + "x + " + str(gCards[g])
							# pf(answerString)

							# EQ: # Ax + Bx + C + Dx = E + Fx + G
							# LeftX = Ax+Bx + Dx
							# LeftConst = C
							# RightX = Fx
							# RightConst = E+G

							leftX = aCards[a]+bCards[b]+dCards[d]
							leftConst = cCards[c]
							rightX = fCards[f]
							rightConst = eCards[e]+gCards[g]

							if ((leftX == rightX) and (leftConst == rightConst)):
								pf(answerString)




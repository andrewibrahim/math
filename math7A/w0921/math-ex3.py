#!/usr/bin/env python3

# A/B (Cx + D) + Ex + F = Gx + H
# A*Cx/B + A*D/B + Ex + F = Gx + H 
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
							hCards = remainingCards(g, gCards)
							hCardsR = range(0, len(hCards))
						
							for h in hCardsR:
								# convert card value to strings to match equation
								answerString = str(aCards[a]) + "/" + str(bCards[b]) + "(" + str(cCards[c]) + "x + " + str(dCards[d]) + ") + " + str(eCards[e]) + "x + " + str(fCards[f]) + " = " + str(gCards[g]) + "x + " + str(hCards[h])
								count = count + 1

								# EQ: A*Cx/B + A*D/B + Ex + F = Gx + H
								# LeftX = A*Cx/B + Ex
								# LeftConst = A*D/B + F
								# RightX = Gx
								# RightConst = H

								# assign valus to like terms for each side of the equation
								leftX = aCards[a]*cCards[c]/bCards[b] + eCards[e]
								leftConst = aCards[a]*dCards[d]/bCards[b] + fCards[f]
								rightX = gCards[g]
								rightConst =hCards[h]

								# prints if the all the like terms are equal
								if ((leftX == rightX) and (leftConst == rightConst)):
									pf(answerString)


pf(str(count)+ " loops were run.")

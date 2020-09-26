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

# start loop with all cards and remove current card from remaining subloops
aCards = cards

# loop through all cards in deck
for a in range(0, len(aCards)):
	# remove card A from deck
	bCards = remainingCards(a, aCards)
	for b in range(0, len(bCards)):
		# remove card B from deck
		cCards = remainingCards(b, bCards)
		for c in range(0, len(cCards)):
			dCards = remainingCards(c, cCards)		
			for d in range(0, len(dCards)):
				eCards = remainingCards(d, dCards)
				for e in range(0, len(eCards)):
					fCards = remainingCards(e, eCards)				
					for f in range(0, len(fCards)):
						gCards = remainingCards(f, fCards)
						for g in range(0, len(gCards)):
							hCards = remainingCards(g, gCards)
							for h in range(0, len(hCards)):
								# convert card value to strings to match equation
								answerString = str(aCards[a]) + "/" + str(bCards[b]) + "(" + str(cCards[c]) + "x + " + str(dCards[d]) + ") + " + str(eCards[e]) + "x + " + str(fCards[f]) + " = " + str(gCards[g]) + "x + " + str(hCards[h])
								count = count + 1

								# EQ: A*Cx/B + A*D/B + Ex + F = Gx + H
								# LeftX = A*Cx/B + Ex
								# LeftConst = A*D/B + F
								# RightX = Gx
								# RightConst = H

								# assign valus to like terms for each side of the equation
								leftX = aCards[a] * cCards[c] / bCards[b] + eCards[e]
								leftConst = aCards[a] * dCards[d] / bCards[b] + fCards[f]
								rightX = gCards[g]
								rightConst = hCards[h]

								# prints if the all the like terms are equal
								if ((leftX == rightX) and (leftConst == rightConst)):
									pf(answerString)

pf(str(count)+ " loops were run.")

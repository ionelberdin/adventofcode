# Ideas for improvement
For the 2nd part, since the recursion goes always towards higher card numbers, it would be worth to process the cards from last to first and keep the computed result of the total number of cards they end up spawning.
That way every card would be processed completely just once, and then the result cached and used later if the card is required again.

# -*- coding: utf-8 -*-
"""
Solution to Euler Problem 54 - Poker Hands.

Given a text file of two player poker hands, determines the number of times
each player would win.

I went a little crazy on this solution and built it out for any number of 5 card
hands, also allowing for potentially other methods of "dealing" than from a 
text file. Certainly there is a solution to this problem that is more concise,
but less flexible.

Created on Fri Jun  8 08:08:34 2018

@author: Jake Wickstrom
"""
import unittest
import itertools
from collections import Counter

class Card():
    """A standard playing card
    Args:
        code - a two character card identifier code. The first value in the
        code represents the value of the card and will be either an integer
        between 2 and 10 inclusive or one of the following characters 'T','J',
        'Q','K','A'. The second character represents the suit an will be one of
        'C','D','H','S'. Codes can be given either as a string with two characters
        or a two element list."""
        
    values = {'2':0x2,
              '3':0x3,
              '4':0x4,
              '5':0x5,
              '6':0x6,
              '7':0x7,
              '8':0x8,
              '9':0x9,
              'T':0xA,
              'J':0xB,
              'Q':0xC,
              'K':0xD,
              'A':0xE}
    
    inv_values = {v: k for k, v in values.items()}
    
    suits = {'C':0x00,
             'D':0x10,
             'H':0x20,
             'S':0x30}
    
    inv_suits = {v: k for k, v in suits.items()}
    
    def __init__(self,code):
        if not hasattr(code,"__len__"):
            raise ValueError("Provided code {} is not indexable".format(code))
        
        if len(code) != 2:
            raise ValueError("A card code must have exactly two characters!")
        
        if not code[0] in self.values.keys():
            if not code[0] in self.values.values():
                raise ValueError("Invalid value, must be one of {}".format(self.values.values()))
        
        if not code[1] in self.suits.keys():
            raise ValueError("Invalid suit, must be one of {}".format(self.suits.keys()))
            
        self.value_code = code[0]
        self.suit_code = code[1]
        
    @property
    def suit(self):
        return self.suits[self.suit_code]
    
    @property
    def value(self):
        if self.value_code in self.values.keys():
            return self.values[self.value_code]
        else:
            return int(self.value_code)
        
    def __str__(self):
        return self.inv_values[self.values[self.value_code]] \
                + self.inv_suits[self.suits[self.suit_code]]
    
    def __eq__(self,other):
        """Overrides delault == opperation"""
        if not isinstance(other,Card):
            return False
        
        return (self.value == other.value and self.suit == other.suit)
        
    def __ne__(self,other):
        """Overrides delault != opperation"""
        return not self.__eq__(other)
    
    def __hash__(self):
        return self.suits[self.suit_code] + self.values[self.value_code]
    
class Player():
    """The :class:'Player' represents a poker player
    Args:
        player_id - a unique identifier for this player"""
    def __init__(self,player_id):
        pass
    
    
class Hand():
    """The :class:'Hand' represents 5 card poker hand
    Args:
        cards - a list of 5 card objects belonging to this hand. All cards must
        be unique."""
    def __init__(self,cards):
        #check that every card in the list is unique
        if not len(list(set(cards))) == len(cards):
            raise ValueError("All cards in a hand must be unique")
            
        if not len(cards) == 5:
            raise ValueError("A hand must consist of 5 cards")
            
        self.cards = cards
        self.values = [card.value for card in self.cards]
        self.suits = [card.suit for card in self.cards]
        
    def score(self):
        """Get a score for this hand. Loses to every hand with higher score
        according to poker rules."""
        
        
        #check for flush
        
            #check for straight flush
    
    def checkForFlush(self):
        """Returns true if all cards in this hand have the same suit"""
        return len(set(self.suits)) == 1
    
    def checkForStraight(self):
        """Returns true if cards in this hand all occur sequentially"""
        low = min(self.values)
        
        #return false if the 4 next values greater than the lowest are not
        #present in the list
        for i in range(5):
            if not low + i in self.values:
                return False
        return True
    
    def getHighCard(self):
        """Returns the value of the highest card in the hand"""
        return max([card.value for card in self.cards])
    
    def _getDuplicity(self):
       """HELPER: Returns an semi - ordered list of tuples, where each tuple 
          contains a value and the number of cards in the hand that have that 
          value.Ordered by the number of occurences, highest first. Order of
          values with the same number of occurences is undefined."""
       return Counter(self.values).most_common()
   
    def checkForPair(self):
        """Returns the value of the highest pair, if it exists. Will return 0
        if no pair is found. Checks explicitly for pairs, will not return the
        value of 3 of a kind for example, even though there is a pair inside
        it."""
        
        for potential_pair in self._getDuplicity():
            if(potential_pair[1] == 2):
                return potential_pair[0]
            
    def checkForTwoPair(self):
        """Returns the value of the highest two pairs, if they exists. Will return 
        0 if no pairs are found. Checks explicitly for pairs, will not return the
        value of 3 of a kind for example, even though there is a pair inside
        it."""
        pairlist = []
        for potential_pair in self._getDuplicity():
            if(potential_pair[1] == 2):
                pairlist.append(potential_pair[0]) 
        
        #sort highest to lowest        
        pairlist.sort(reverse=True)
                
        return pairlist if len(pairlist) == 2 else 0
    
        
    
class Match():
    """The :class:'Match' represents the matchup of one or more :class:'hand' 
    objects. All instances of :class:'Hand' must belong to a different :class:
    'Player'.
    Args:
        hands - an ordered list of :class:'Hand' objects. No two hands in the same match
        are permitted to have the same :class:'Card'
        """
    def __init__(self,hands):
        pass
    
    def showdown(self):
        """Returns player number of player with best hand in match."""
        pass

class dealer():
    """The :class:'Dealer' provides a method of distributing cards to players"""
    
class tournament():
    """Represents a series of poker matches between two hands"""
    def __init__(self,players,dealer):
        pass
    
class TestHelpers():
    
    suits = ["C","D","H","S"]
    string_values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    int_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    
    all_values = []
    all_values.extend(string_values)
    all_values.extend(int_values)
    
    deck = [Card(code) for code in itertools.product(string_values,suits)]
    
    @classmethod
    def setUpCards(self,parent):
        """Load useful card values as parameters into parent class"""
        parent.string_values = list(self.string_values)
        parent.int_values = list(self.int_values)
        parent.all_values = list(self.all_values)
        parent.suits = list(self.suits)
        
        
class CardTest(unittest.TestCase):
    def setUp(self):
        TestHelpers.setUpCards(self)
        
    def test_cards_are_equal(self):
        """Check that all cards in the deck are equal to themselves"""
        for value in self.string_values:
            for suit in self.suits:
                with self.subTest(msg="Checking {}{} stringlike".format(value,suit)):
                    self.assertEqual(Card(value + suit),Card(value + suit))
                    
        for value in self.all_values:
            for suit in self.suits:
                with self.subTest(msg="Checking {}{} listlike".format(value,suit)):
                    self.assertEqual(Card([value,suit]),Card([value,suit]))
        
        #test that cards initialized in different ways are equal
        for value in self.all_values:
            for string_value in self.string_values:
                for suit in self.suits:
                    if(value == string_value or Card.values[string_value]==value):
                        with self.subTest(msg="Checking {}{}".format(value,suit)):
                            self.assertEqual(Card(string_value + suit),Card([value,suit]))
                    
        
    def test_hash(self):
            """Check that all cards in the deck have a unique hash"""
            hashes = [card.__hash__() for card in TestHelpers.deck]
            
            #it is sufficient to say that the set has the same length as the
            #list it was created from to confirm every element in the list is
            #unique
            self.assertCountEqual(list(set(hashes)),hashes)
                        
    def test_cards_are_not_equal(self):
        """Check that cards can be not equal to each other"""
        cards = ['AH','2H','6D','TC','4C','2D',[8,"C"],[13,"D"]]
        
        for card1 in cards:
            for card2 in cards:
                if cards.index(card1) != cards.index(card2):
                    with self.subTest(msg="Checking {} != {}".format(card1,card2)):
                        self.assertNotEqual(Card(card1),Card(card2))
                        
                        
    
    def test_valid_string_inputs(self):
        for value in self.string_values:
            for suit in self.suits:
                with self.subTest(msg="Checking {}{}".format(value,suit)):
                    try:
                        Card(value + suit)
                    except ValueError:
                        self.fail("Card {} is not valid".format(value + suit))
                        
    def test_valid_list_inputs(self):
        #test all cards in a deck given as lists
        for value in self.all_values:
            for suit in self.suits:
                with self.subTest(msg="Checking {}{}".format(value,suit)):
                    try:
                        Card([value,suit])
                    except ValueError:
                        self.fail("Card {} is not valid".format(str(value) + suit))
    
    def test_card_is_invalid(self):
        bad_cards = ["HC","19","AA", "5CA","",2,"1C","8A","8h"]
        
        for bad_card_code in bad_cards:
                    with self.subTest(msg="Checking {} is invalid".format(bad_card_code)):
                        self.assertRaises(ValueError,Card,bad_card_code)
                    
                    
class TestHand(unittest.TestCase):
    def test_valid_hand(self):
        self.skipTest("Takes a long time to execute as it tests every valid hand possible")
        for cards in itertools.combinations(TestHelpers.deck,5):
            with self.subTest():
                try:
                    Hand(cards)
                except ValueError:
                    self.fail("Hand {} is not valid".format(cards))
        
    def test_is_a_flush(self):
        royal_flush = Hand([Card("AD"),Card("KD"),Card("QD"),Card("JD"),Card("TD")])
        straight_flush = Hand([Card("TC"),Card("9C"),Card("8C"),Card("7C"),Card("6C")])
        random_flush = Hand([Card("6S"),Card("9S"),Card("QS"),Card("2S"),Card("4S")])
        flushes = [royal_flush,straight_flush,random_flush]
        
        for flush in flushes:
            with self.subTest():
                self.assertTrue(flush.checkForFlush())
            
    def test_not_a_flush(self):
        not_flush_1 = Hand([Card("AH"),Card("KD"),Card("QD"),Card("JD"),Card("TD")])
        not_flush_2 = Hand([Card("AH"),Card("7C"),Card("4S"),Card("2D"),Card("3D")])
        not_flush_3 = Hand([Card("2H"),Card("3S"),Card("4D"),Card("5C"),Card("6C")])
        not_flushes = [not_flush_1,not_flush_2,not_flush_3]
        
        for hand in not_flushes:
            with self.subTest():
                self.assertFalse(hand.checkForFlush())
            
    def test_is_a_straight(self):
        low_straight = Hand([Card("2H"),Card("3S"),Card("4D"),Card("5C"),Card("6C")])
        royal_flush = Hand([Card("AD"),Card("KD"),Card("QD"),Card("JD"),Card("TD")])
        straight_flush = Hand([Card("TC"),Card("9C"),Card("8C"),Card("7C"),Card("6C")])
        unordered_straight = Hand([Card("7H"),Card("9S"),Card("6D"),Card("TC"),Card("8C")])
        straights =  [low_straight,royal_flush,straight_flush,unordered_straight]
        
        for straight in straights:
            with self.subTest():
                self.assertTrue(straight.checkForStraight())
                
    def test_not_a_straight(self):
        random_cards = Hand([Card("2H"),Card("3S"),Card("4D"),Card("TD"),Card("6C")])
        random_flush = Hand([Card("6S"),Card("9S"),Card("QS"),Card("2S"),Card("4S")])
        one_off = Hand([Card("AD"),Card("KD"),Card("QD"),Card("JD"),Card("9D")])
        not_straights = [random_cards,random_flush,one_off]
        
        for hand in not_straights:
            with self.subTest():
                self.assertFalse(hand.checkForStraight())
        
                
    def test_high_card(self):
        """Tests if Hand can identify it's highest card"""
        hand = Hand([Card("2H"),Card("3S"),Card("4D"),Card("TD"),Card("6C")])
        self.assertEqual(hand.getHighCard(),10)
        
    def test_multiple_high_card(self):
        """Tests if Hand can identify it's highest card if there are more than one"""
        hand = Hand([Card("2H"),Card("TC"),Card("4D"),Card("TD"),Card("6C")])
        self.assertEqual(hand.getHighCard(),10)
                
    def test_high_card_royal(self):
        """Tests if hand can identify a high card above 10"""
        hand = Hand([Card("AH"),Card("TC"),Card("4D"),Card("TD"),Card("6C")])
        self.assertEqual(hand.getHighCard(),14)
        
    def test_is_a_pair(self):
        hand = Hand([Card("2H"),Card("TC"),Card("4D"),Card("TD"),Card("6C")])
        self.assertEqual(hand.checkForPair(),10)
        
    def test_three_not_a_pair(self):
        """Tests that a three of a kind is not recognized as a pair"""
        hand = Hand([Card("TH"),Card("TC"),Card("4D"),Card("TD"),Card("6C")])
        self.assertFalse(hand.checkForPair())
        
    def test_pair_from_full_house(self):
        """Tests that checkForPair() can extract the pair from a full house"""
        full_house = Hand([Card("2H"),Card("TC"),Card("4D"),Card("TD"),Card("2C")])
        self.assertEqual(full_house.checkForPair(),2)
        
    def test_is_two_pair(self):
        hand = Hand([Card("6H"),Card("TC"),Card("4D"),Card("TD"),Card("6C")])
        self.assertEqual(hand.checkForTwoPair(),[10,6])
    
if __name__ == "__main__":
    unittest.main(exit=False,verbosity=2)
    
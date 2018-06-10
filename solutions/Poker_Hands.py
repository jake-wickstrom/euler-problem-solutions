# -*- coding: utf-8 -*-
"""
Solution to Euler Problem 54 - Poker Hands.

Given a text file of two player poker hands, determines the number of times
each player would win.

I went a little crazy on this solution and built it out for any number of 5 card
hands, also allowing for potentially other methods of "dealing" than from a 
text file. Certainly there is a solution to this problem that is more concise,
but less flexible.

This was also my first real experience with unit testing. Looking back, I
probably could have avoided the Hand class having so many methods to test, as 
all that is really important in that class is the score. My design might be a
little too modular and requires a ton of testing as a result. The pair, triple,
quad methods are also very similar, which was probably a bad design decision
looking back. I can see the benefits of test driven development, and from this point forward I would expect
to see unit testing in all of my solutions.

Created on Fri Jun  8 08:08:34 2018

@author: Jake Wickstrom
"""
import unittest
import unittest.mock as mock
import itertools
import abc
import re
import io
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
        
        #sorting high to low makes getting values easier
        #score depends on these values being sorted
        self.values.sort()
        self.suits.sort()
        
    def score(self):
        """Get a score for this hand. Loses to every hand with higher score
        according to poker rules.
        
        Codes:
        0x90000a - straight flush (a is value of highest card)
        0x80000a - four of a kind (a is value of quad)
        0x7000ab - full house (a is value of trip, b of pair)
        0x6abcde - flush (a b c d e are value of cards high to low)
        0x50000a - straight (a is value of highest card)
        0x400abc - three of a kind (a is value of trip, b,c others high to low)
        0x300abc - two pair (a is high pair, b low pair, c other card)
        0x20abcd - pair (a is pair, bcd is other cards in order)
        0x1abcde - high card (abcde is order of cards by value)
        """
        values_by_duplicity = [x[0] for x in self._getDuplicity(self.values)]
        duplicities = [x[1] for x in self._getDuplicity(self.values)]
        is_flush = len(set(self.suits)) == 1
        is_straight = set(range(min(values_by_duplicity),min(values_by_duplicity) + 5)) == set(self.values)
        
        if is_flush == 1:
            if is_straight:
                #straight flush
                return 0x900000 + max(self.values)
            else:
                #flush
                return 0x600000 \
                       + 0x10000*values_by_duplicity[0] \
                       + 0x1000*values_by_duplicity[1] \
                       + 0x100*values_by_duplicity[2] \
                       + 0x10*values_by_duplicity[3] \
                       + 0x1*values_by_duplicity[4]  
                       
        if 4 in duplicities:
            #quads
            return 0x800000 + self._getHexCode(values_by_duplicity)
        
        if 3 in duplicities:
            if 2 in duplicities:
                #full house
                return 0x700000 + self._getHexCode(values_by_duplicity)
            else:
                #three of a kind
                return 0x400000 + self._getHexCode(values_by_duplicity)
            
        if is_straight:
            #straight
            return 0x500000 + self._getHexCode(values_by_duplicity)
        
        if duplicities[0] == 2:
            if duplicities[1] == 2:
                #two pair
                return 0x300000 + self._getHexCode(values_by_duplicity)
            else:
                #pair
                return 0x200000 + self._getHexCode(values_by_duplicity)
        
        #high card
        return self._getHexCode(values_by_duplicity)
    
    @classmethod
    def _getHexCode(self,card_values):
        """Returns an integer code that represents the value of a hand, by order.
        Arguements - 
            card_values (list(int)) - a list of the values of the cards,
            ordered by priority. Must be at least one entry, and less than 5
            each entry must be an integer, at least 2 and no more than 14
            
        Returns:
            an integer number representing the value of this hand
        """
        if len(card_values) > 5 or len(card_values) < 1:
            raise ValueError("Number of card values must be between 1 and 5")
            
        if max(card_values) > 14 or min(card_values) < 2:
            raise ValueError("Card values must be between 2 and 14 (14->Ace)")
        
        exp = len(card_values) - 1
        card_code = 0
        for value in card_values:
            card_code += (0x10**exp)*value
            exp -= 1
            
        return card_code
            
    @classmethod
    def _getDuplicity(self,values):
       """Returns an ordered list of tuples, where each tuple 
          contains a value and the number of cards in the hand that have that 
          value.Ordered by the number of occurences, highest first. Order of
          values with the same number of occurences is from greatest to least."""
       return sorted(Counter(values).most_common(),key = lambda dupli: (dupli[1],dupli[0]),reverse=True)
    
class Tournament():
    """Represents a series of poker matches between two hands"""
    __metaclass__ = abc.ABCMeta
    def __init__(self):
        pass
    
    @abc.abstractmethod
    def run(self):
        """Run a tournament and return the winner"""
        pass
    
class TextFileTournamentCreator():
    def createTournament(self,players,matchups):
        pass
    
class ClassicTournamentFromTextFile(Tournament):
    """A classic poker style tournament from a formatted text file. Each line of
    the file contains a group of hands (between 2 and 10), with each hand
    consisting of 5 tokens which indicate the card in question. All hands are
    assumed to be valid, and it is assumed there are no ties."""
    def __init__(self,file):
        self.matchups = []
        self.handRegex = re.compile(r"(?:[\dTJQKA][CDHS] *?){5}")
        try:
            with open(file) as tournament_txt:
                for matchup in tournament_txt:
                    raw_hands = self.handRegex.findall(matchup)
                    #break up matchup into hands, then for each hand create
                    #individual cards and place them in a Hand object
                    self.matchups.append([Hand([Card(x) for x in raw_cards.split()]) for raw_cards in raw_hands])
        except FileNotFoundError:
            print("The provided file does not exist. Program terminating.")
            exit()
    
                
    def run(self):
        total_wins = {}
        for matchup in self.matchups:
            scores = []
            for hand in matchup:
                scores.append(hand.score())
            if scores.count(max(scores)) > 1:
                
                try:  
                    total_wins["Draws"] += 1
                except KeyError:
                    total_wins["Draws"] = 1
            else:
                try:
                    total_wins[scores.index(max(scores))] += 1
                except KeyError:
                    total_wins[scores.index(max(scores))] = 1
                
        return total_wins
            
                
    
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
                    
    def test_hex_no_cards(self):
        self.assertRaises(ValueError,Hand._getHexCode,[])
    
    def test_hex_one_card(self):
        self.assertEqual(Hand._getHexCode([5]),0x5)
    
    def test_hex_two_cards(self):
        self.assertEqual(Hand._getHexCode([5,2]),0x52)
        
    def test_hex_three_cards(self):
        self.assertEqual(Hand._getHexCode([5,2,7]),0x527)
        
    def test_hex_four_cards(self):
        self.assertEqual(Hand._getHexCode([5,2,7,3]),0x5273)
    
    def test_hex_five_cards(self):
        self.assertEqual(Hand._getHexCode([5,2,7,3,6]),0x52736)
        
    def test_hex_too_many_cards(self):
        self.assertRaises(ValueError,Hand._getHexCode,[5,2,7,3,6,4])
        
    def test_hex_value_to0_low(self):
        self.assertRaises(ValueError,Hand._getHexCode,[5,2,7,3,1,4])
        
    def test_hex_value_too_high(self):
        self.assertRaises(ValueError,Hand._getHexCode,[5,2,7,3,15,4])
        
    def test_duplicity_highest_occurence_is_first(self):
        self.assertEqual(Hand._getDuplicity([1,1,3]),[(1,2),(3,1)])
        
    def test_duplicity_same_dup_ordered_by_val(self):
        self.assertEqual(Hand._getDuplicity([1,1,3,3]),[(3,2),(1,2)])
        
    def test_duplicity_complex_test(self):
        self.assertEqual(Hand._getDuplicity([1,1,3,3,3,8,14,2,2]),[(3,3),(2,2),(1,2),(14,1),(8,1)])
        
    def test_royal_ties_royal(self):
        royal_flush = Hand([Card("AD"),Card("KD"),Card("QD"),Card("JD"),Card("TD")])
        royal_flush_2 = Hand([Card("AH"),Card("KH"),Card("QH"),Card("JH"),Card("TH")])
        self.assertEqual(royal_flush.score(),royal_flush_2.score())
        
    def test_royal_beats_straight_flush(self):
        royal_flush = Hand([Card("AD"),Card("KD"),Card("QD"),Card("JD"),Card("TD")])
        straight_flush = Hand([Card("TC"),Card("9C"),Card("8C"),Card("7C"),Card("6C")])
        self.assertGreater(royal_flush.score(),straight_flush.score())
        
    def test_straight_flush_ties_straight_flush(self):
        straight_flush_diamonds = Hand([Card("TD"),Card("9D"),Card("8D"),Card("7D"),Card("6D")])
        straight_flush_clubs = Hand([Card("TC"),Card("9C"),Card("8C"),Card("7C"),Card("6C")])
        self.assertEqual(straight_flush_diamonds.score(),straight_flush_clubs.score())
        
    def test_straight_flush_beats_lower_straight_flush(self):
        straight_flush = Hand([Card("TD"),Card("9D"),Card("8D"),Card("7D"),Card("6D")])
        straight_flush_lower = Hand([Card("5C"),Card("9C"),Card("8C"),Card("7C"),Card("6C")])
        self.assertGreater(straight_flush.score(),straight_flush_lower.score())
        
    def test_straight_flush_beats_quads(self):
        straight_flush = Hand([Card("TD"),Card("9D"),Card("8D"),Card("7D"),Card("6D")])
        quads = Hand([Card("2H"),Card("2C"),Card("2S"),Card("2D"),Card("JC")])
        self.assertGreater(straight_flush.score(),quads.score())
        
    def test_quads_beat_lower_quads(self):
        lower_quads = Hand([Card("2H"),Card("2C"),Card("2S"),Card("2D"),Card("JC")])
        quads = Hand([Card("AH"),Card("AC"),Card("AS"),Card("AD"),Card("JC")])
        self.assertGreater(quads.score(),lower_quads.score())
        
    def test_quads_beat_lower_quads_with_higher_kicker(self):
        lower_quads = Hand([Card("2H"),Card("2C"),Card("2S"),Card("2D"),Card("KC")])
        quads = Hand([Card("AH"),Card("AC"),Card("AS"),Card("AD"),Card("JC")])
        self.assertGreater(quads.score(),lower_quads.score())
        
    def test_quads_beat_full_house(self):
        quads = Hand([Card("2H"),Card("2C"),Card("2S"),Card("2D"),Card("KC")])
        full_house = Hand([Card("AH"),Card("AC"),Card("AD"),Card("KD"),Card("KH")])
        self.assertGreater(quads.score(),full_house.score())
        
    def test_full_house_beats_lower_full_house(self):
        full_house = Hand([Card("AH"),Card("AC"),Card("AD"),Card("KD"),Card("KH")])
        full_house_2 = Hand([Card("AH"),Card("AC"),Card("AD"),Card("9D"),Card("9H")])
        full_house_3 = Hand([Card("KH"),Card("KC"),Card("KD"),Card("TD"),Card("TH")])
        full_house_4 = Hand([Card("4H"),Card("4C"),Card("4D"),Card("KD"),Card("KH")])
        full_houses = [(full_house,full_house_2),(full_house_2,full_house_3),(full_house,full_house_4)]
        
        for houses in full_houses:
            with self.subTest():
                self.assertGreater(houses[0].score(),houses[1].score())
                
    def test_full_house_beats_flush(self):
        full_house = Hand([Card("4H"),Card("4C"),Card("4D"),Card("KD"),Card("KH")])
        flush = Hand([Card("6S"),Card("9S"),Card("QS"),Card("2S"),Card("4S")])
        self.assertGreater(full_house.score(),flush.score())
        
    def test_flush_beats_lower_flush(self):
        flush = Hand([Card("6S"),Card("9S"),Card("QS"),Card("2S"),Card("4S")])
        flush_lower = Hand([Card("6H"),Card("9H"),Card("JH"),Card("2H"),Card("4H")])
        self.assertGreater(flush.score(),flush_lower.score())
        
    def test_flush_beats_straight(self):
        flush = Hand([Card("6S"),Card("9S"),Card("QS"),Card("2S"),Card("4S")])
        straight = Hand([Card("7H"),Card("9S"),Card("6D"),Card("TC"),Card("8C")])
        self.assertGreater(flush.score(),straight.score())
        
    def test_straight_beats_lower_straight(self):
        straight = Hand([Card("7H"),Card("9S"),Card("6D"),Card("TC"),Card("8C")])
        straight_lower = Hand([Card("7H"),Card("9S"),Card("6D"),Card("5C"),Card("8C")])
        self.assertGreater(straight.score(),straight_lower.score())
        
    def test_straight_beats_trips(self):
        straight = Hand([Card("7H"),Card("9S"),Card("6D"),Card("TC"),Card("8C")])
        trips = Hand([Card("4H"),Card("4C"),Card("4D"),Card("KD"),Card("2H")])
        self.assertGreater(straight.score(),trips.score())
        
    def test_trips_beat_lower_trips(self):
        trips = Hand([Card("9H"),Card("9C"),Card("9D"),Card("KD"),Card("2H")])
        trips_lower = Hand([Card("4H"),Card("4C"),Card("4D"),Card("KD"),Card("2H")])
        self.assertGreater(trips.score(),trips_lower.score())
        
    def test_trips_beat_two_pair(self):
        trips = Hand([Card("9H"),Card("9C"),Card("9D"),Card("KD"),Card("2H")])
        two_pair = Hand([Card("9H"),Card("9C"),Card("8D"),Card("2D"),Card("2H")])
        self.assertGreater(trips.score(),two_pair.score())
        
    def test_two_pair_beats_lower_two_pair(self):
        two_pair = Hand([Card("9H"),Card("9C"),Card("8D"),Card("7D"),Card("7H")])
        two_pair_lower = Hand([Card("9H"),Card("9C"),Card("8D"),Card("2D"),Card("2H")])
        two_pair_even_lower = Hand([Card("6H"),Card("6C"),Card("8D"),Card("4D"),Card("4H")])
        two_pair_lowest = Hand([Card("5H"),Card("5C"),Card("8D"),Card("4D"),Card("4H")])
        hands = [(two_pair,two_pair_lower),(two_pair_lower,two_pair_even_lower),(two_pair_even_lower,two_pair_lowest)]
        
        for matchup in hands:
            self.assertGreater(matchup[0].score(),matchup[1].score())
            
    def test_two_pair_beats_pair(self):
        two_pair = Hand([Card("9H"),Card("9C"),Card("8D"),Card("7D"),Card("7H")])
        pair = Hand([Card("9H"),Card("9C"),Card("8D"),Card("7D"),Card("6H")])
        self.assertGreater(two_pair.score(),pair.score())
        
    def test_pair_beats_lower_pair(self):
        pair = Hand([Card("9H"),Card("9C"),Card("8D"),Card("7D"),Card("6H")])
        pair_lower = Hand([Card("8H"),Card("8C"),Card("AD"),Card("7D"),Card("6H")])
        self.assertGreater(pair.score(),pair_lower.score())
        
    def test_pair_beats_high_card(self):
        pair = Hand([Card("9H"),Card("9C"),Card("8D"),Card("7D"),Card("6H")])
        high_card = Hand([Card("9H"),Card("KC"),Card("8D"),Card("7D"),Card("6H")])
        self.assertGreater(pair.score(),high_card.score())
        
    def test_high_card_beats_lower_high_card(self):
        high_card = Hand([Card("9H"),Card("KC"),Card("8D"),Card("7D"),Card("6H")])
        high_card_lower = Hand([Card("9H"),Card("JC"),Card("8D"),Card("7D"),Card("6H")])
        self.assertGreater(high_card.score(),high_card_lower.score())

class TestClassicTournamentFromTextFile(unittest.TestCase):
    def system_test_gets_correct_value(self):
        """Value verified on projecteuler.net, verifies that further implimentation
        changes still get right answer"""
        tournament = ClassicTournamentFromTextFile("..\\Data\\Problem_54_Data.txt")
        self.assertEqual(tournament.run(),{0:376,1:624})
        
if __name__ == "__main__":
    unittest.main(exit=False)
    tournament = ClassicTournamentFromTextFile("..\\Data\\Problem_54_Data.txt")
    results = tournament.run()
    print("\nPlayer 1: {}\nPlayer 2: {}".format(results[0],results[1]))
from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['cookies', 'cream', 'love', 'vinegar']


def _get_random_word(list_of_words):
    if list_of_words == []:
        raise InvalidListOfWordsException
    else:
        return random.choice(list_of_words)


def _mask_word(word):
    if word == "":
        raise InvalidWordException
    else:
        return len(word)*"*"


def find_substring(string, substring):
    """ 
    Returns list of indices where substring begins in string
    >>> find_substring('r', "rmotr")
    [0, 4]
    """
    indices = []
    index = -1  # Begin at -1 so index + 1 is 0
    while True: 
        # Find next index of substring, by starting search from index + 1
        index = string.find(substring, index + 1)
        if index == -1:  
            break  # All occurrences have been found
        indices.append(index)
    return indices

def _uncover_word(answer_word, masked_word, character):
    if character == "" or len(character) > 1 :
        raise InvalidGuessedLetterException(Exception)
    if len(masked_word) != len(answer_word):
        raise InvalidWordException
    if answer_word =="" or masked_word =="" :
        raise InvalidWordException
    #convert answer_word and character to lower case    
    lower_character = str.lower(character)
    lower_answer = str.lower(answer_word)
    if lower_character not in lower_answer:
        return masked_word  
    #loop through list of indices of answer_word to replace characters
    if lower_character in lower_answer:
      indices=find_substring(lower_answer, lower_character)
      for index in indices:
        masked_word = masked_word[:index] + lower_character + masked_word[index + 1:]
    return masked_word



def guess_letter(game, letter):

    if game['remaining_misses']==0 or game['answer_word'] == game['masked_word']:
        raise GameFinishedException
    else:
        #make game case insensitive by converting all strings to lower case
        letter = str.lower(letter)
        game['answer_word'] = str.lower(game['answer_word'])
    
        game['masked_word'] = _uncover_word(game['answer_word'], game['masked_word'], letter)
    
        if game['answer_word'] != game['masked_word']: 
            game['previous_guesses'] += letter  
    
        if letter not in game ['answer_word']:
            game['remaining_misses'] -= 1
    
        if game['remaining_misses']==0:
            raise GameLostException 
    
        if game['answer_word'] == game['masked_word']:
            raise GameWonException
        
        return game 
    
    


def start_new_game(list_of_words=None, number_of_guesses=5):
    if list_of_words is None:
        list_of_words = LIST_OF_WORDS

    word_to_guess = _get_random_word(list_of_words)
    masked_word = _mask_word(word_to_guess)
    game = {
        'answer_word': word_to_guess,
        'masked_word': masked_word,
        'previous_guesses': [],
        'remaining_misses': number_of_guesses,
    }

    return game

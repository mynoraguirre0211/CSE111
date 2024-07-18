import random

def main():

    sentences = [make_sentence(1, "past"),
                make_sentence(1, "present"),
                make_sentence(1, "future"),
                make_sentence(2, "past"),
                make_sentence(2, "present"),
                make_sentence(2, "future")]

    for i in sentences:
        print(i)

def get_preposition():
  """Return a randomly chosen preposition
  from this list of prepositions:
      "about", "above", "across", "after", "along",
      "around", "at", "before", "behind", "below",
      "beyond", "by", "despite", "except", "for",
      "from", "in", "into", "near", "of",
      "off", "on", "onto", "out", "over",
      "past", "to", "under", "with", "without"
  Return: a randomly chosen preposition.
  """
  words = ["about", "above", "across", "after", "along",
      "around", "at", "before", "behind", "below",
      "beyond", "by", "despite", "except", "for",
      "from", "in", "into", "near", "of",
      "off", "on", "onto", "out", "over",
      "past", "to", "under", "with", "without"]
  word = random.choice(words)
  return word

def get_adjetive():
    words = ["good", "big", "small", "hot", "cold", 
             "expensive", "difficult", "easy", "free",
             "open", "closed", "sick", "nice", "hungry",
             "late", "right", "happy", "new", "old", "tall", 
             "ready", "far"]
    word = random.choice(words)
    return word

def get_adverb():
    words = ["now", "yesterday", "today", "tomorrow", "soon", 
             "already", "eventually", "just", "here", "there",
             "everywhere", "anywhere", "above", "below", "nearby",
             "faraway", "quickly", "happily", "carefully", "loudly",
             "softly", "truly", "perfectly", "bravely", "gently"]
    word = random.choice(words)
    return word

def get_determiner(quantity):

    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
            # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]
            
    word = random.choice(words)
    return word

def get_verb(quantity, tense):
    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        words = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity != 1:
        words = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    else:
        words = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
            
    word = random.choice(words)
    return word

def get_prepositional_phrase(quantity):
  """Build and return a prepositional phrase composed
  of three words: a preposition, a determiner, and a
  noun by calling the get_preposition, get_determiner,
  and get_noun functions.
  Parameter
      quantity: an integer that determines if the
          determiner and noun in the prepositional
          phrase returned from this function should
          be single or pluaral.
  Return: a prepositional phrase.
  """
  preposition = get_preposition()
  determiner = get_determiner(quantity)
  noun = get_noun(quantity)

  preposition_phrase = f"{determiner} {noun} {preposition}"
  return preposition_phrase

def get_prepositional_phrase2(quantity):
    """I added this other one to put in in the start of the sentence"""

    prep = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)

    prep_phrase = f"{determiner.capitalize()} {noun} {prep}"
    return prep_phrase

def make_sentence(quantity, tense):
  """Build and return a sentence with three words:
  a determiner, a noun, and a verb. The grammatical
  quantity of the determiner and noun will match the
  number in the quantity parameter. The grammatical
  quantity and tense of the verb will match the number
  and tense in the quantity and tense parameters.
  """
  prep_phrase2 = get_prepositional_phrase2(quantity)
  preposition_phrase = get_prepositional_phrase(quantity)
  determiner = get_determiner(quantity)
  noun = get_noun(quantity)
  verb = get_verb(quantity, tense)
  adverb = get_adverb()
  adjetive = get_adjetive()
    
  sentence = f"{determiner.capitalize()} {adjetive} {noun} {prep_phrase2} {adverb} {verb} {determiner} {adjetive} {noun} {preposition_phrase}"
  return sentence

main()
    
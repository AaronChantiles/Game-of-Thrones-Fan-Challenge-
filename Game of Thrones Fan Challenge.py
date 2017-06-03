### For all my Game of Thrones fans out there. Lets put your knowledge to the test! ###

### Q&A Variables ###
EASY_QUESTION = "I did not kill Joffrey but I wish that I had. Watching your vicious __1__ die gave me more relief than a thousand lying whores. I wish I was the monster you think I am. I wish I had enough __2__ for the whole pack of you. I would gladly give my life to watch you all swallow it. I will not give my life for Joffrey's murder. And I know I'll get no justice here, so I will let the __3__ decide my fate. I demand a trial by __4__! -Tyrion Lannister\n"

MEDIUM_QUESTION = "Chaos isn't a pit. Chaos is a __1__. Many who try to climb it __2__ and never get to try again. The fall breaks them. And some, are given a chance to climb. They refuse, they cling to the __3__ or the gods or love. Illusions. Only the ladder is real. The __4__ is all there is. -Little Finger\n"

HARD_QUESTION = "Night gathers, and now my watch begins. It shall not end until my death. I shall take no __1__, hold no lands, father no children. I shall wear no crowns and win no glory. I shall live and die at my post. I am the __2__ in the darkness. I am the watcher on the walls. I am the fire that burns against __3__, the light that brings the dawn, the horn that wakes the __4__, the shield that guards the realms of men. I pledge my life and honor to the Night’s Watch, for this night and all the nights to come.\n"

LEGENDARY_QUESTION = "Don’t fight for your king, don’t fight for his kingdoms, don’t fight for honor, don’t fight for glory, don’t fight for __1__ because you won’t get any. This is your city Stannis means to __2__, your gate he’s ramming. If he gets in, it will be your houses he burns, your __3__ he steals, your women he will rape. Those are __4__ men knocking at our door. Let’s go kill them! -Tyrion Lannister\n"


blanks_list = ["__1__", "__2__", "__3__", "__4__"]
  

name = raw_input("What is your name? ")

import random
correct = ["\nThat's correct "+ name +"! Hodor would be proud!\n", "\nThat's correct "+ name +"! You must know the Three-eyed Raven!\n", "\nThat's correct "+ name +"! You'll be on the Irone Throne in no time!\n", "\nThat's correct "+ name +"! The North remembers!\n"]
incorrect = ["\nShould've read the books! Try again.\n", "\nYou bring dishonor to your name. Try again.\n", "\nHodor is crying in heaven. Don't make Hodor cry. Try again.\n", "\nNed Stark would be disappointed. Try again.\n"]

#Spoiler Alert! Quiz answers
EASY_ANSWERS = ["BASTARD", "POISON", "GODS", "COMBAT"]
MEDIUM_ANSWERS = ["LADDER", "FAIL", "REALM", "CLIMB"]
HARD_ANSWERS = ["WIFE", "SWORD", "COLD", "SLEEPERS"] 
LEGENDARY_ANSWERS = ["RICHES", "SACK", "GOLD", "BRAVE"]

### Functions ###

def Welcome():
  """Behavior: Player Greeting. Gets their name and explains how the game works. Players name is inserted into the string
  Inputs: None
  Outputs: Welcome Prompt. Level Prompt"""
  print "\n=================== LEVEL SELECTION ==================="
  print "\nHello " + name + ". Welcome to the Game of Thrones fan challenge! The purpose of the game is to fill in all the blanks with the correct responses. If you answer correctly you can move foward, if not you'll be prompted to try again. You'll have 5 lives on each level. You will either win or die. Now please select your difficultty level!\n"
  print "A) Easy: I've seen an episode or two, so I pretty much know what's going on.\n"
  print "B) Medium: I LOVE Game of thrones. I've seen all the episodes!\n"
  print "C) Hard: Game of Thrones has changed my life! I'm ready to join the Nights Watch!\n"
  print "D) Legendary: I am the prince that was promised! I'm here to lead the realm through the long night!\n"


def Game_Setup():
  """Behavior: Game Setup function. Choose Easy, Medium, or Hard / A, B, or C. Prints an ominous prompt, and returns the corresponding question/answers
  Inputs: None
  Outputs: Difficulty level, Ominous prompt, returns question/answers"""
  if level == "EASY":
    print "\nYou've chosen to take the Kingsroad. Safe travels my friend.\n"
    return EASY_QUESTION, EASY_ANSWERS
  elif level == "MEDIUM":
    print "\nA difficult path lies before you. The Vale can be a dangerous place.\n"
    return MEDIUM_QUESTION, MEDIUM_ANSWERS
  elif level == "HARD":
    print "\nWinter is coming. Hope you've read the books.\n"
    return HARD_QUESTION, HARD_ANSWERS
  elif level == "LEGENDARY":
    print "\nWinter has come. You will not survive.\n"
    return LEGENDARY_QUESTION, LEGENDARY_ANSWERS



def replaced_answer():
  """Behavior: Executes a while loop prompting player for their answer. If correct it will print a Good Job prompt, and will reprint the question with the blank filled in. If incorrect it'll tell the player to try again. If they fail 5 times it's game over. If you win it prints a victory message
  Inputs: None 
  Outputs: Correct/Incorrect answer prompts, program kill switch, reprinted question with filled in blank, victory message"""   
  question, answers = Game_Setup()
  zero = 0
  one = 1
  attempts = 5
  index = 0
  while index < len(blanks_list):
    for answer in answers:
      print question
      player_input = raw_input("\nWhat is your answer to "+ blanks_list[index] +"?: ").upper()
      while player_input != answer:
        print random.choice(incorrect)
        attempts = attempts - one
        print "You have "+ str(attempts) +" attempts left."
        if attempts == zero:
          print "\nGame over. Your watch has ended.\n"
          quit()
        player_input = raw_input("\nWhat is your answer to "+ blanks_list[index] +"?: ").upper()
      if player_input == answer.upper():
        print random.choice(correct)
        question = question.replace(blanks_list[index], player_input)
        index = index + one
  print question
  print "====================== VICTORY! ======================"
  print "\nCongratulations, you've won the game! You are truly " + name + " of the House Targaryen, First of your Name, the Unburnt, ruler of the Andals and the First Men, Khaleesi of the Great Grass Sea, Breaker of Chains, and the Mother/Father of Dragons. I shall follow you from this day until everyone dies in season 8!"


def execute_game():
  """Behavior: Executes program functions. Prompts the player to type their difficulty level. Changes raw_input to capital letters. If incorrect, will prompt them for an actual level. Starts Welcome function and replaced_answer function.
  Inputs: Player's raw_input for difficulty level
  Outputs: Executes program functions, difficulty level selected"""   
  Welcome()
  levels_list = ["EASY", "MEDIUM", "HARD", "LEGENDARY", "A", "B", "C", "D"]
  global level
  level = raw_input("Please type your difficulty level here: ")
  level = level.upper()
  while level not in levels_list:
    level = raw_input("Invalid level. Please enter an actual level. ")
    level = level.upper()
  if level == "A": level = level.replace("A", "EASY")
  if level == "B": level = level.replace("B", "MEDIUM")
  if level == "C": level = level.replace("C", "HARD")
  if level == "D": level = level.replace("D", "LEGENDARY")
  print "\n==================== QUIZ: "+ level +" ====================="
  replaced_answer()
execute_game()






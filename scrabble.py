#Python_Scrabble
#Created as part of Codecademy - Dictionaries Project
#By: E.Cope
#Date: Jan. 2020


letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#step1
letter_to_points = {}

for key, value in zip(letters, points):
  letter_to_points[key] = value
  
#print(letter_to_points)

#2
letter_to_points[" "] = 0

#3-8
def score_word(word):
  
  point_total = 0
  
  for i in range(len(word)):
    char = word[i]
    point_total += letter_to_points.get(char, 0)
  
  return point_total
  
brownie_points = score_word('BROWNIE')
#print(brownie_points)

#9
player_to_words = {'player1': ['BLUE', 'TENNIS', 'EXIT'], 'wordNerd': ['EARTH', 'EYES', 'MACHINE'], 'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'], 'Prof Reader': ['ZAP', 'COMA', 'PERIOD']}

#10-14
player_to_points = {}

for player in player_to_words:
  player_point = 0
  
  for word in player_to_words[player]:
    player_point += score_word(word)
    
  player_to_points[player] = player_point
  
#print(player_to_points)

#updates scores
def update_point_totals():
  updated_points = {}

  for player in player_to_words:
    points = 0
  
    for word in player_to_words[player]:
      points += score_word(word)
    
    updated_points[player] = points
  print(updated_points)

#plays a word from a player and updates score
def play_word(player, word):
  wordList = player_to_words[player]
  wordList.append(word)
  player_to_words[player] = wordList
  score = score_word(word)
  
  print(player+" played the word: "+ word + " for " + str(score) + " points.")
  
  update_point_totals()

  
#TEST
play_word('player1', 'BEEF')

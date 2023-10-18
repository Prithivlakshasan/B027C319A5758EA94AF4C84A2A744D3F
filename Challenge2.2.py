# 2.2 implement a class called player that represents a cricket player. the player class should have a method called play() which prints " the player is playing cricket.derive two classes ,batsman and bowler,from the player class .override the play() Method in each derived class to print"the batsman is batting"and"the bowler is bowling",respectively.write a program to create objects of both the batsman and bowler classes and call the play()method for each object.

#define the base class player
class Player:
    def play(self):
        print("the player is playing cricket.")
      
#define the derived class batsman
class Batsman(Player):
  def play(self):
      print("The batsman is batting")


#define the derived class bowler
class Bowler(Player):
  def play(self):
    print("The bowler is bowling")
    

#create objects of batsman and bowler classes
batsman = Batsman()
bowler = Bowler()

#call the play() method for each object
batsman.play()
bowler.play()
class Person(object):
  name = ""
  age = 0
  drinkChoice = ""
  weakness = ""
  transportation = ""

  def __init__(self, name, age, drinkChoice, weakness, transportation):
    self.name = name
    self.age = age
    self.drinkChoice = drinkChoice
    self.weakness = weakness
    self.transportation = transportation

  def print_self(self):
    print self.name + " drinks " + self.drinkChoice + "."
    print self.name + " is " + str(self.age) + " years old."
    print self.name + " has a fear of " + self.weakness
    print self.name + " drives a " + self.transportation

TheDude = Person("The Dude", 41, "White Russian", "working", "green car, some brown, rust coloration")
TheDude.print_self()

print ""

halfnhalf = ["good", "good", "bad", "good", "good", "good", "good", "bad", "good"]

count = 0

for x in halfnhalf:
  if x == "good":
    print "Pour me another caucasian"
  if x == "bad":
    count += 1
    print "oh god man!"
  if count == 2:
    print "All right, I'm leaving. I'm sorry ma'am."
    break

print ""

Walter = Person("Walter", 43, "Miller Lite", "dying face down in the muck", "white van")
Walter.print_self()

print ""

class Nihilist(Person):
  belief = ""
  occupation = ""

  def __init__(self, name, age, drinkChoice, weakness, transportation, belief, occupation):
    self.name = name
    self.age = age
    self.drinkChoice = drinkChoice
    self.weakness = weakness
    self.transportation = transportation
    self.belief = belief
    self.occupation = occupation

  def print_nihilist(self):
    print self.name + " is a " + self.occupation + " that believes in " + self.belief

Uli = Nihilist("Uli", 52, "nossing", "nossing", "motorcycle", "NOSSING", "Criminal")
Uli.print_self()
Uli.print_nihilist()

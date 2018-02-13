from .person import Person


class MITPerson(Person):
  nextIdNum = 0

  def __init__(self, name):
    Person.__init__(self, name)
    self.idNum = MITPerson.nextIdNum
    MITPerson.nextIdNum += 1

  def getIdNum(self):
    return self.idNum

  def __lt__(self, other):
    return self.idNum < other.idNum

  def speak(self, utterance):
    return (self.getLastName() + " says: " + utterance)

class Student(MITPerson):
  pass

class UG(Student):
  def __init__(self, name, classYear):
    MITPerson.__init__(self, name)
    self.year = classYear

  def getClass(self):
    return self.year

  def speak(self, utterance):
    return MITPerson.speak(self, " Dude, " + utterance)

class Grad(Student):
  pass

class TransferStudent(Student):
  pass

def isStudent(obj):
  return isinstance(obj, Student)

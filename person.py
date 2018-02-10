import datetime

class Person(object):
  def __init__(self, name):
    self.name = name
    self.birthday = None
    self.lastname = name.split(' ')[-1]
  
  def get_last_name(self):
    return self.lastname

  def __str__(self):
    return self.name

  def setBirthday(self, month, day, year):
    self.birthday = datetime.time(year, month, day)

  def get_age(self):
    if self.birthday == None:
      raise ValueError
    return (datetime.date.today() - self.birthday).days

  def __lt__(self, other):
    if self.lastname == other.lastname:
      return self.name < other.name
    return self.lastname < other.lastname

class Cat:
  def drink(self):
    print('drink')

class Animal(Cat):
  def eat(self):
    print('eat')

if __name__ == '__main__':
  a = Animal()
  a.drink()
  a.eat()    
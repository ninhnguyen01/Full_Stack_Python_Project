class Car():
     pass

class Yugo(Car):
     pass

print(issubclass(Yugo, Car))

give_me_a_car = Car()
give_me_a_yugo = Yugo()

class Car():
     def exclaim(self):
          print("I'm a Car!")

class Yugo(Car):
     def exclaim(self):
          print("I'm a Yugo! You go not very far with me.")
     def need_a_push(self):
          print("A little help here?")

give_me_a_car = Car()
give_me_a_yugo = Yugo()
give_me_a_car.exclaim()

give_me_a_yugo.exclaim()
give_me_a_yugo.need_a_push()

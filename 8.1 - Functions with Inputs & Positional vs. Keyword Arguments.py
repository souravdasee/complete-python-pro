#Simple Function
def greet():
  print("Hello Sourav")
  print("How do you do Jack?")
  print("Isn't the weather nice today?")
greet()

#Function that allows for input
#'name' is the parameter.
#'Jack Bauer' is the argument.
def greet_with_name(name):
  print(f"Hello {name}")
  print(f"How do you do {name}?")
greet_with_name("Jack")

#Functions with more than 1 input
def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}?")

#Calling greet_with() with Positional Arguments
greet_with("Jack", "Nowhere")
#vs.
greet_with("Nowhere", "Jack")


#Calling greet_with() with Keyword Arguments
greet_with(location="India", name="Sourav")
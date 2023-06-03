from stack_and_queue import Queue

class Animal:
    def __init__(self, species, name):
        """
        Represents an animal with its species and name.

        Args:
            species (str): The species of the animal ("dog" or "cat").
            name (str): The name of the animal.
        """
        self.species = species
        self.name = name

class AnimalShelter:
    def __init__(self):
        """
        Initializes an empty animal shelter with separate queues for dogs and cats.
        """
        self.dog_queue = Queue()
        self.cat_queue = Queue()

    def enqueue(self, animal):
        """
        Adds an animal to the animal shelter.

        Args:
            animal (Animal): The animal object to be added to the shelter.

        Raises:
            ValueError: If the animal species is not valid ("dog" or "cat").
        """
        if animal.species == "dog":
            self.dog_queue.enqueue(animal)
        elif animal.species == "cat":
            self.cat_queue.enqueue(animal)
        else:
            raise ValueError("Invalid animal species. Only 'dog' or 'cat' allowed.")

    def dequeue(self, pref):
        """
        Removes and returns the first dog or cat in the animal shelter based on the preference.

        Args:
            pref (str): The preference for either "dog" or "cat".

        Returns:
            Animal: The first dog or cat object based on the preference, or None if the queue is empty or the preference is invalid.

        Raises:
            ValueError: If the preference is not valid ("dog" or "cat").
        """
        if pref == "dog":
            if not self.dog_queue.is_empty():
                return self.dog_queue.dequeue()
            else:
                return None
        elif pref == "cat":
            if not self.cat_queue.is_empty():
                return self.cat_queue.dequeue()
            else:
                return None
        else:
            raise ValueError("Invalid preference. Only 'dog' or 'cat' allowed.")

shelter = AnimalShelter()

shelter.enqueue(Animal("dog", "Ricks"))
shelter.enqueue(Animal("cat", "Lucy"))
shelter.enqueue(Animal("dog", "Oreo"))

dog = shelter.dequeue("dog")
print(dog.name)

cat = shelter.dequeue("cat")
print(cat.name)

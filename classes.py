class Food:
  def __init__(self, name, calories, carbs, protein, fat):
    self.name = name
    self.calories = calories
    self.carbs = carbs
    self.protein = protein
    self.fat = fat
  def __str__(self):
    return self.name + ": calories: " + str(self.calories) + ", carbs: " + self.carbs + ", protein: "+self.protein+", fat: "+self.fat
  def List(self):
    return [self.calories, self.carbs, self.protein, self.fat]
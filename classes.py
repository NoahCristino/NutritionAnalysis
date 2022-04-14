class Food:
  def __init__(self, name, fat, cholesterol, calories, sodium, carbs, protein, vits_and_mins):
    self.name = name
    self.fat = fat
    self.cholesterol = cholesterol
    self.calories = calories
    self.sodium = sodium
    self.carbs = carbs
    self.protein = protein
    self.vits_and_mins = vits_and_mins
  def __str__(self):
    return self.name + ": calories: " + str(self.calories) + ", fat: "+str(self.fat)+", cholesterol: "+str(self.cholesterol)+", sodium: "+str(self.sodium)+", carbs: "+str(self.carbs)+", protein: "+str(self.protein)+", vitamins and minerals: "+str(self.vits_and_mins)
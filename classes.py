class Food:
  def __init__(self, name, total_fat, sat_fat, cholesterol, calories, sodium, choline, folate):
    self.name = name
    self.total_fat = total_fat
    self.cholesterol = cholesterol
    self.calories = calories
    self.sodium = sodium
    self.sat_fat = sat_fat
    self.choline = choline
    self.folate = folate
  def __str__(self):
    return self.name + ": calories: " + str(self.calories) + ", total_fat: "+str(self.total_fat)+", sat_fat: "+str(self.sat_fat)+", sodium: "+str(self.sodium)+", cholesterol: "+str(self.cholesterol)+", choline: "+str(self.choline)+", folate: "+str(self.folate)
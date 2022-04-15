from classes import *
import csv
import numpy as py
from scipy.optimize import nnls

food_list = []

with open('nutrition.csv', newline='') as csvfile:
     reader = csv.DictReader(csvfile)
     its = 10
     it_count = 0
     for row in reader:
         total_fat_per_gram = float(row['total_fat'][:-1])*(1/float(row['serving_size'][:-2]))
         if row['cholesterol'] != '0':
             cholesterol_per_gram = (float(row['cholesterol'][:-2])/1000)*(1/float(row['serving_size'][:-2]))
         else:
             cholesterol_per_gram = 0
         calories_per_gram = float(row['calories'])*(1/float(row['serving_size'][:-2])) #assumed serving_size is in grams
         if row['sodium'] != '0':
             sodium_per_gram = float(row['sodium'][:-2])*(1/float(row['serving_size'][:-2]))
         else:
             sodium_per_gram = 0
         if row['saturated_fat'] != '':
             sat_fat_per_gram = float(row['saturated_fat'][:-1])*(1/float(row['serving_size'][:-2]))
         else:
             sat_fat_per_gram = 0
         if row['choline'] != '0':
             choline_per_gram = (float(row['choline'][:-3])/1000)*(1/float(row['serving_size'][:-2]))
         else:
             choline_per_gram = 0
         if row['folate'] != '0':
             folate_per_gram = (float(row['folate'][:-3])/1000)*(1/float(row['serving_size'][:-2]))
         else:
             folate_per_gram = 0
         f = Food(row['name'], total_fat_per_gram, sat_fat_per_gram, cholesterol_per_gram, calories_per_gram, sodium_per_gram, choline_per_gram, folate_per_gram)
         food_list.append(f)
         it_count = it_count + 1
         if it_count == its:
             break


calories_list = []
sat_fat_list = []
total_fat_list = []
for i in range(0, 10):
    calories_list.append(food_list[i].calories)
    sat_fat_list.append(food_list[i].sat_fat)
    total_fat_list.append(food_list[i].total_fat)
A = [calories_list, sat_fat_list, total_fat_list]
target_calories = 150
target_sat_fat = 5
target_total_fat = 25
B = py.array([target_calories, target_sat_fat, target_total_fat])
x = nnls(A,B)
i = 0
cals = 0
satfat = 0
totalfat = 0
names = []
for scale in x[0]:
    cals = cals + (scale * food_list[i].calories)
    satfat = satfat + (scale * food_list[i].sat_fat)
    totalfat = totalfat + (scale * food_list[i].total_fat)
    names.append(food_list[i].name)
    i = i + 1
for idx, name in enumerate(names):
    print(str("{:.2f}".format(x[0][idx]))+" grams "+name)
print("========================================================================")
print("target: "+str(target_calories)+", actual: "+str(cals)+", difference: "+str(target_calories-cals))
print("target: "+str(target_sat_fat)+", actual: "+str(satfat)+", difference: "+str(target_sat_fat-satfat))
print("target: "+str(target_total_fat)+", actual: "+str(totalfat)+", difference: "+str(target_total_fat-totalfat))
error_score = abs(target_calories-cals) + abs(target_sat_fat-satfat) + abs(target_total_fat-totalfat)
print("error score: "+str(error_score))
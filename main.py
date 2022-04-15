from classes import *
import csv
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
         #print(f)
         it_count = it_count + 1
         if it_count == its:
             break

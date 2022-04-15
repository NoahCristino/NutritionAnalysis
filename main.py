from sys import argv
from classes import *
import csv
import numpy as py
from scipy.optimize import nnls
from tqdm import tqdm

food_list = []

with open('nutrition.csv', newline='') as csvfile:
     reader = csv.DictReader(csvfile)
     its = 1000000
     it_count = 0
     for row in reader:
         fat_per_gram = float(row['total_fat'][:-1])*(1/float(row['serving_size'][:-2]))
         calories_per_gram = float(row['calories'])*(1/float(row['serving_size'][:-2])) #assumed serving_size is in grams
         carbs_per_gram = float(row['carbohydrate'][:-2])*(1/float(row['serving_size'][:-2]))
         protein_per_gram = float(row['protein'][:-2])*(1/float(row['serving_size'][:-2]))
         f = Food(row['name'], calories_per_gram, carbs_per_gram, protein_per_gram, fat_per_gram)
         food_list.append(f)
         it_count = it_count + 1
         if it_count == its:
             break

def predict(foodlist, target_calories, target_carbs, target_protein, target_fat, verbose=0):
    calories_list = []
    fat_list = []
    carbs_list = []
    protein_list = []
    for food in foodlist:
        calories_list.append(food.calories)
        fat_list.append(food.fat)
        carbs_list.append(food.carbs)
        protein_list.append(food.protein)
    A = [calories_list, carbs_list, protein_list, fat_list]
    B = py.array([target_calories, target_carbs, target_protein, target_fat])
    x = nnls(A,B)
    i = 0
    cals = 0
    carbs = 0
    protein = 0
    fat = 0
    names = []
    for scale in x[0]:
        cals = cals + (scale * food_list[i].calories)
        carbs = carbs + (scale * food_list[i].carbs)
        protein = protein + (scale * food_list[i].protein)
        fat = fat + (scale * food_list[i].fat)
        
        names.append(food_list[i].name)
        i = i + 1
    for idx, name in enumerate(names):
        if verbose == 1:
            print(str("{:.2f}".format(x[0][idx]))+" grams "+name)
    if verbose == 1:
        print("========================================================================")
        print("target calories: "+str(target_calories)+", actual: "+str(cals)+", difference: "+str(target_calories-cals))
        print("target carbs: "+str(target_carbs)+", actual: "+str(carbs)+", difference: "+str(target_carbs-carbs))
        print("target protein: "+str(target_protein)+", actual: "+str(protein)+", difference: "+str(target_protein-protein))
        print("target fat: "+str(target_fat)+", actual: "+str(fat)+", difference: "+str(target_fat-fat))
    error_score = abs(target_calories-cals) + abs(target_carbs-carbs) + abs(target_protein-protein) + abs(target_fat-fat)
    if verbose == 1 or verbose == 2:
        print("error score: "+str(error_score))
    return error_score

from itertools import combinations
import random
order_length = int(argv[2])
#selection = random.choice(options)
#print(selection)
#print(len(options))
lowest_error = 99999
lowest_combo = None
random_sampling = True
random_count = int(argv[1])
random_target = 80
random_mode = True #true is random for random_count iterations, false is til reaches below random_target
if random_sampling == False:
    options = list(combinations(food_list, order_length)) #len = c(len(food_list), order_length)) = 20c5 = 15504
    for option in options:
        e = predict(option, 3506, 468, 145, 117)
        if e < lowest_error:
            lowest_error = e
            lowest_combo = option
else:
    if random_mode:
        for i in range(random_count):
            option = []
            for i in range(order_length):
                option.append(random.choice(food_list))
            e = predict(option, 3506, 468, 145, 117)
            if e < lowest_error:
                lowest_error = e
                lowest_combo = option
    else:
        while lowest_error > random_target:
            option = []
            for i in range(order_length):
                option.append(random.choice(food_list))
            e = predict(option, 3506, 468, 145, 117, 0)
            if e < lowest_error:
                lowest_error = e
                lowest_combo = option
e = predict(lowest_combo, 3506, 468, 145, 117, 1)
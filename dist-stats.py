import csv
import sys
import pandas as pd
import numpy as np
from collections import defaultdict
import argparse
from pprint import pprint
import collections
import operator


def restaurant_category_dist(filename, city):
    df = pd.read_csv(filename)
    list_of_all_types_of_categories = []

    
    for index,row in df.iterrows():
       if (("Restaurants" not in row.categories) or (row.city != city)):
            df.drop(index,inplace=True)
      
    #splits all subcategories and put 
    #all into one list
    for string in list(df.categories):
        for s in string.split(';'):
            list_of_all_types_of_categories.append(s)

    while "Restaurants" in list_of_all_types_of_categories:
        list_of_all_types_of_categories.remove("Restaurants") 

    while "Food" in list_of_all_types_of_categories:
        list_of_all_types_of_categories.remove("Food") 
    

    dictionary_of_everything = {}
    for l in list_of_all_types_of_categories:
        dictionary_of_everything[l] = list_of_all_types_of_categories.count(l)
    
    sorted_answer = sorted(dictionary_of_everything.items(),key=operator.itemgetter(1))
    

    for categories,occurences in sorted_answer[::-1]:
        print(categories,":",occurences)

def restaurant_review_dist(filename,city):
    df = pd.read_csv(filename)
    list_of_all_types_of_categories = []
    list_categories_count =[]

    for index,row in df.iterrows():
       if (("Restaurants" not in row.categories) or (row.city != city)):
            df.drop(index,inplace=True)

    for string in list(df.categories):
        for s in string.split(';'):
            list_of_all_types_of_categories.append(s)
            
    while "Restaurants" in list_of_all_types_of_categories:
        list_of_all_types_of_categories.remove("Restaurants") 

    while "Food" in list_of_all_types_of_categories:
        list_of_all_types_of_categories.remove("Food") 
    
    counter_for_stars = 0
    sum_of_stars = 0
    dict_for_stars = {}
    dict_for_reviews = {}


    for cat in list_of_all_types_of_categories:
        for index, row in df.iterrows():
            if(cat in row.categories):
                counter_for_stars = counter_for_stars +1
                sum_of_stars = sum_of_stars + row.stars

        dict_for_stars[cat] = round(sum_of_stars/counter_for_stars,2)
        dict_for_reviews[cat] = list_of_all_types_of_categories.count(cat)
    
    sorted_answer = sorted(dict_for_reviews.items(),key=operator.itemgetter(1))

    for categories,occurences in sorted_answer[::-1]:
        print(categories,":",occurences,":",dict_for_stars[categories])
    

def command_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="csv file")
    parser.add_argument("city", help="city of choice")
    args = parser.parse_args()
    filename = args.filename
    city = args.city

    #restaurant_category_dist(filename,city)
    #restaurant_review_dist(filename,city)

def main():
        command_line_args()


if __name__ == "__main__":
    main()
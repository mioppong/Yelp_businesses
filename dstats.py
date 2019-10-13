
import csv
import sys
import pandas as pd
import numpy as np
from collections import defaultdict
import argparse

           
def num_of_business(filename, city):
        df = pd.read_csv(filename)
        counter=0
        list_of_cities = df["city"]
        
        for c in list_of_cities:
                if (c == city):
                        counter = counter + 1
        print ("num_of_business in",city, "is:",counter)

def avg_stars(filename,city):
        df = pd.read_csv(filename)
        avg_stars = 0
        #print(df[])

        for s in df.stars:
                avg_stars = avg_stars + s
        
        avg_stars = round( (avg_stars /len(df.stars)), 2)

        print("avg_stars of a business in",city,"is:", avg_stars)

def num_of_restaurants(filename,city):
        df = pd.read_csv(filename)
        businesses_in_city = df[["city","categories"]]
        counter = 0
        for index,row in businesses_in_city.iterrows():
                if ("Restaurants" in row.categories and row.city == city):
                        counter  = counter +1

        print("num_of_restaurants in",city,"is",counter)

def avg_stars_restaurants(filename,city):
        df = pd.read_csv(filename)
        businesses_in_city = df[["city","categories","stars"]]
        counter = 0
        stars_total = 0.0
        avg_stars = 0.0
        for index,row in businesses_in_city.iterrows():
                if ("Restaurants" in row.categories and row.city == city):
                        counter  = counter +1
                        stars_total = stars_total + int(row.stars)

        avg_stars = round(stars_total / counter,2)
        print("avg_stars_restaurants in",city,"is",avg_stars)

def avg_num_of_reviews(filename,city):
        df = pd.read_csv(filename)
        reviews_total = 0
        
        for index, row in df.iterrows():
                reviews_total = reviews_total + int(row.review_count)
                
        answer = reviews_total / len(df)
        answer = round(answer,2)
        print("avg_num_of_reviews in",city,"is",answer)

def avg_num_of_reviews_bus(filename,city):
        df = pd.read_csv(filename)

        reviews_total=0
        counter = 0
        for index, row in df.iterrows():
                if ("Restaurants" in row.categories and row.city == city):
                        counter = counter + 1
                        reviews_total = reviews_total + int(row.review_count)
        
        answer = reviews_total / counter
        answer = round(answer,2)

        print("avg_num_of_reviews of Restaurants in", city, "is", answer)

def command_line_args():
        parser = argparse.ArgumentParser()
        parser.add_argument("filename", help="csv file")
        parser.add_argument("city", help="city of choice")
        args = parser.parse_args()
        filename = args.filename
        city = args.city
        
        num_of_business(filename, city)
        avg_stars(filename,city)
        num_of_restaurants(filename,city)
        avg_stars_restaurants(filename,city)
        avg_num_of_reviews(filename,city)
        avg_num_of_reviews_bus(filename,city)
        
def main():
        #count_business()
        #dealing_with_args()
        command_line_args()


if __name__=="__main__":
        main()
        
       




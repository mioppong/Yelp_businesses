# Yelo Businesses

This was another class project, where given a csv file from the yelp website, calculate certain things such as

dstats.py contains

* numOfBus: the number of businesses in the city
* avgStars: the average number of stars of a business in the city
* numOfRestaurants: the number of restaurants in the city
* avgStarsRestaurants: the average number of stars of restaurants in the city
* avgNumOfReviews: the average number of reviews for all businesses in the city
* avgNumOfReviewsBus: the average number of reviews for restaurants in the city
 
and

dist-stats.py containts

* restaurantCategoryDist: a frequency distribution of the number of restaurants in each
category of restaurants (e.g., Chinese, Japanese, Korean, Greek, etc.) in a descending order of
popularity (from the most popular category to the least popular). 

* restaurantReviewDist: a frequency distribution of the number of reviews submitted for
each category of restaurants (e.g., Chinese, Japanese, Korean, Greek, etc.) in a descending order
(from the most reviewed category to the least reviewed), along with the average number of
stars received per category.

* create a bar chart that shows the top-10 of restaurantCategoryDist found earlier,
where the x-axis represents the restaurant category and the y-axis represents its frequency 

## Getting Started
* Download files and unzip them
* A copy of the yelp_business.csv is called Book1.csv, its the same just less rows

## Running program

* to get the answers in the dstats for a city,

example below we use Toronto, and Book1.csv, but we can use the yelp_business.csv, as well as another city
```
python dstats.py Book1.csv Toronto
    
```

* to get the answers in the dist-stats for a city,
```
python dist-stats.py Book1.csv Toronto
    
```

## Future Work
* In the future, i hope to asnwer more queries, and comment my code better, so people can read them easier

## Acknowledgments
* TheNewBoston

## Author
* Michael Oppong
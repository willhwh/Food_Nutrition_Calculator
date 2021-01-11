import os
import csv


#pasring variables
class Parse():
    meal_translator =  {'B':'Breakfast','L':"Lunch",'D':'Dinner','O':"Others"}
    
    def __init__(self, web_url, driver):
        self.web_url = web_url
        self.driver = driver
       
    
    #create csv file for records
    def create_file(self):
        columns = ['Date', 'Meal_Time' , 'Brand', 'Food', 'Calories', 'Fat', 'Carbs', 'Fiber', 'Protein']
        if os.path.isfile('record/food_recoder.csv') == False:
            with open('record/food_recoder.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(columns)
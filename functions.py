import matplotlib.pyplot as plt
import numpy as np
from config import username, password
from flask import Flask
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, insert
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import os
import csv
import pandas as pd

from food_class import food
from main import main


def static():

    meal_translator = {'B':'Breakfast','L':"Lunch",'D':'Dinner','O':"Others"}
    web_url = 'https://www.calorieking.com/us/en/foods/'
    def start_program():
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(options=options)
        return driver
    driver = start_program()
    
    app = Flask(__name__)
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0  # Prevent caching

    engine = create_engine(
        f"postgresql://{username}:{password}@localhost:5432/food")
    base = automap_base()
    base.prepare(engine, reflect=True)

    database_tables = base.classes
    session = Session(bind=engine)
    
    food_tb = database_tables.Food
    record_tb = database_tables.Record
    user_tb = database_tables.User

def create_file():
    global columns
    columns = ['Date', 'Meal_Time' , 'Brand', 'Food', 'Calories', 'Fat', 'Carbs', 'Fiber', 'Protein']
    if os.path.isfile('food_recoder.csv') == False:
        with open('food_recoder.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(columns)
            
def create_user():
    static()
    user_id = session.query(user_tb).count()+1
    if user_id ==1:
        print("Creating User File...")
        weight = int(input("Please enter your weight.\t"))
        print("Please pick your activity level from one of the options below:\t")
        print("A---Light\nB---Mediumn\nC---Heavy")
        act = str(input("A or B or C?\t")).upper()
        print("Please pick your purpose from one of the options below:\t")
        print("A---Gain Weight\nB---Keep Weight\nC---Loss Weight")
        purpose = str(input("A or B or C?\t")).upper()
        calories_dict = {'AA': 35, 'AB': 30, 'AC': 25,
                        'BA': 40, 'BB': 35, 'BC': 30,
                        'CA': 45, 'CB': 40, 'CC': 35}
        global target_calories 
        global target_protein
        global target_fat
        global target_carbs
        target_calories = calories_dict[act+purpose] * weight
        target_protein = target_calories * 0.3/4
        target_fat = target_calories * 0.2/9
        target_carbs = target_calories * 0.5/4
        
        user_input = user_tb(User_ID=1, Target_Calories = target_calories,
                             Target_Protein = target_protein, Target_Carbs = target_carbs,
                             Target_Fat = target_fat)
        session.add(user_input)
        session.commit()

def get_key_word():
    driver.get(web_url)
    print('Recoridng your eating history...')
    time.sleep(0.2)
    search_terms = input('Please enter a brand.\t')
    print(f'search for the terms: \t{search_terms}')
    # search the key words
    search_field = driver.find_element_by_id('keywords')
    search_field.send_keys(search_terms)
    search_field.send_keys(Keys.RETURN)
    # get search terms results
    brands = driver.find_elements_by_class_name('jss5')
    global result_lst
    result_lst = [ i.find_element_by_class_name('MuiTypography-root').text for i in brands]
    if 'iOS'in str(result_lst):
        print('Please try another search tearms for brand.')
        get_key_word(driver, web_url)
    return result_lst

def get_brand():
    def check_brand():
        for i in result_lst:
            yield(i)
    brands = check_brand()
    correct = 'F'
    global target_brand
    while correct == 'F':
        try:
            brand_candidate = next(brands)
            correct = input(f'If {brand_candidate} the brand you are looking for? T/F:\t').upper()
            if correct =='T':
                target_brand = str(brand_candidate)
                return target_brand 
                break
        except: 
            print('Please try another search tearms for brand.')
            get_key_word()
            target_brand = get_brand()
            return target_brand 
            break   

def get_key_word_checked():
    driver.get(web_url)
    time.sleep(0.2)
    global meal_terms
    meal_terms = input('Please enter the main meal ingrediant.\t').upper()
    search_terms = target_brand + ' ' + meal_terms
    print(f'search for the terms: {search_terms}')
    # search the key words
    search_field = driver.find_element_by_id('keywords')
    search_field.send_keys(search_terms)
    search_field.send_keys(Keys.RETURN)
    # get search terms results
    foods = driver.find_elements_by_class_name('jss374')
    global food_lst
    food_lst = [ i.text for i in foods]
    if 'iOS'in str(food_lst):
        print('Please try another search tearms for brand.')
        get_key_word_checked()
    return food_lst

# narrow down to the specific dish and get the dish's info link
def get_food():
    count=0
    def check_food(food_lst):
        for i in food_lst:
            yield(i)
    foods = check_food(food_lst)
    correct = 'F'
    global target_food_url
    global target_food
    while correct == 'F':
        try:
            food_candidate = next(foods)
            correct = input(f'If {food_candidate} the meal you are looking for? T/F:\t').upper()
            if correct =='T':
                target_food = str(food_candidate)
                url = driver.find_elements_by_class_name('MuiListItem-button')[count].get_attribute('href')
                target_food_url = (url)
                return target_food_url, target_food
                break
            else:
                count=count+1
        except: 
            print('Please try another search tearms for meal.')
            get_key_word_checked()
            target_food_url, target_food = get_food()
            return target_food_url, target_food
            break

def get_food_info():
    driver.get(target_food_url)
    infos = driver.find_element_by_class_name('jss374')
    infos = infos.text.split('\n')
    
    calories = infos[0].split(' ')[0]
    fat = infos[6].split(' ')[0]
    carbs = infos[8].split(' ')[0]
    fiber = infos[10].split(' ')[0]
    protein = infos[12].split(' ')[0]
    
    return calories, fat, carbs, fiber, protein

def get_time():
    global date
    date = input('Please enter the date. mm/dd/yyyy.\t')
    print('Please enter the meal time.')
    global meal_time_transfered
    meal_time = input('B---Breakfast\nL---Lunch\nD---Dinner\nO---Others').upper()
    if meal_time in ['B','L','D','O']:
        meal_time_transfered = meal_translator[meal_time]
    else:
        print('Please enter the meal time again.')
        get_time()
    return date, meal_time_transfered

def get_inputs(): 
    result_lst = get_key_word()
    target_brand = get_brand()
    food_lst = get_key_word_checked()
    target_food_url, target_food = get_food()
    calories, fat, carbs, fiber, protein = get_food_info()
    date, meal_time_transfered = get_time()
    return date, meal_time_transfered, target_brand, target_food, calories, fat, carbs, fiber, protein

def run_again():
    run = input('Have another meal to record? T/F \t').upper()
    if run == 'T':
        start_record()
    else:
        back_to_menu()

def back_to_menu():
    print('Back to Main Menu.')
    main()

def start_record():
    create_file()
    create_user()
    date, meal_time_transfered, target_brand, target_food, calories, fat, carbs, fiber, protein = get_inputs()
    meal = food(date, meal_time_transfered, target_brand, target_food, calories, fat, carbs, fiber, protein)
    meal.show_info()
    meal.save_result()
    run_again()

def start_visualize():
    search_date = input('Please enter the date you are looking at.\t')
    records = session.query(food_tb).join(record_tb,food_tb.Food_ID == record_tb.Food_ID
                                           ).filter(record_tb.Time == search_date)
    intake_calories = 0
    intake_protein = 0
    intake_carbs = 0
    intake_fat = 0
    for intake in records:
        intake_calories += intake.Calories
        intake_protein += intake.Protein
        intake_carbs += intake.Carbs
        intake_fat += intake.Fat
        
    target = session.query(user_tb)
    for goal in target:
        target_calories = goal.Target_Calories
        target_protein = goal.Target_Protein
        target_carbs = goal.Target_Carbs
        target_fat = goal.Target_Fat
    
    
    plt.figure(figsize=(10,10))
    plt.title('Intaken Nutritions vs. Target Goals')
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.5)
    ax1=plt.subplot(221)
    ax2=plt.subplot(222)
    ax3=plt.subplot(223)
    ax4=plt.subplot(224)

    axes = [ax1,ax2,ax3,ax4]
    intakes = [intake_calories,intake_protein,intake_carbs,intake_fat]
    targets = [target_calories,target_protein,target_carbs,target_fat]
    nutritions = ['Caloires','Protein','Carbs','Fat']
    
    
    
    for ax,intake,target,nutrition in zip(axes,intakes,targets,nutritions):
        print(f'You have {intake}g {nutrition} on {search_date}.')
        sizes = np.array([int(intake),int(target)])
        def absolute_value(val):
            a  = round(val/100*sizes.sum(), 0)
            return a
        ax.pie(sizes,
               labels = [f'Intaken {nutrition}',f'Target {nutrition}'],
                autopct = absolute_value,
                pctdistance = 0.6,
                textprops = {"fontsize" : 12})
    plt.show()

def get_command():
    '''
    Get command, upper-case it
    '''
    print("'A' => Add to Record")
    print("'V' => View Daily Intake")
    print("'Q' => Quit")
    command = input("Enter command: ").upper()
    return command
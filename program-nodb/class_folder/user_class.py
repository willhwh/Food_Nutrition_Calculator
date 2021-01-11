import matplotlib.pyplot as plt
import numpy as np
import os
import csv
import pandas as pd

#user relative class
class User():
   
    #craete a user
    def create_user(self):
        columns = ['User_ID', 'Target_Calories','Target_Protein','Target_Carbs','Target_Fat']
        if os.path.isfile('record/user.csv') == False:
            with open('record/user.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(columns)

        user_data = pd.read_csv('record/user.csv')
        if len(user_data)<1:
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

            target_calories = calories_dict[act+purpose] * weight
            target_protein = target_calories * 0.3/4
            target_fat = target_calories * 0.2/9
            target_carbs = target_calories * 0.5/4

            with open('record/user.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                user_input = [1, target_calories, target_protein, target_carbs, target_fat]
                writer.writerow(user_input)
            
    #return the intake nutrition for a user assigned date
    def start_visualize(self):
        search_date = input('Please enter the date you are looking at. mm/dd/yyyy.\t')
        records = pd.read_csv('record/food_recoder.csv')
        data_for_the_date = []
        for i in range(len(records)):
            if records['Date'][i] == search_date:
                data_for_the_date.append(i)

        intake_calories = 0
        intake_protein = 0
        intake_carbs = 0
        intake_fat = 0

        for intake in data_for_the_date:
            intake_calories += records['Calories'][intake]
            intake_protein += records['Protein'][intake]
            intake_carbs += records['Carbs'][intake]
            intake_fat += records['Fat'][intake]

        target = pd.read_csv('record/user.csv')
        target_calories = target['Target_Calories']
        target_protein = target['Target_Protein']
        target_carbs = target['Target_Carbs']
        target_fat = target['Target_Fat']


        plt.figure(figsize=(8,8))
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


        print(f'You have intaken the nutrition belows:')
        for ax,intake,target,nutrition in zip(axes,intakes,targets,nutritions):
            print(f'{intake}g {nutrition} on {search_date}.')
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
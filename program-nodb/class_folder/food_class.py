import csv

#store nurtrition info to RMDB
class Food:
    def __init__(self, date, meal_time_transfered, target_brand, target_food,
                 calories, fat, carbs, fiber, protein):
        self.date = date
        self.meal_time_transfered = meal_time_transfered
        self.target_brand = target_brand 
        self.target_food = target_food
        self.calories = calories
        self.fat = fat
        self.carbs = carbs
        self.fiber = fiber
        self.protein = protein

    
    #show the recording meal info
    def show_info(self): 
        meal_info = f'The meal contains \n{self.calories} kcal calories,\n{self.fat} g fat,\n{self.carbs} g carbs,\n{self.fiber} g fiber,\n{self.protein} g protein'
        print(meal_info)
    
    #save the record to csv
    def save_result(self):
        with open('record/food_recoder.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([self.date, self.meal_time_transfered, self.target_brand, self.target_food, self.calories, self.fat, self.carbs, self.fiber, self.protein]) 
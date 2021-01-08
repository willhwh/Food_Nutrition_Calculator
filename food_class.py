import pandas as pd
import functions

class food:

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
        self. protein = protein
        
    def show_info(self): 
        data = [self.date, self.meal_time_transfered, self.target_brand, 
                self.target_food, self.calories, self.fat, 
                self.carbs, self.fiber, self.protein]
        columns = ['Date', 'Meal_Time' , 'Brand', 'Food', 'Calories', 'Fat', 'Carbs', 'Fiber', 'Protein']
        meal_info = pd.DataFrame([data], columns = columns)
        return meal_info

        
    def save_result(self):
        
        #User
        user_id = 1
        
        #food
        food_id = session.query(food_tb).count()+1
        search_history = session.query(food_tb).filter(food_tb.Brand == self.target_brand
                                                          ).filter(food_tb.Meal == self.target_food)
        if search_history.count()>0:
            for history_data in search_history:
                food_id = history_data.Food_ID
                
        else:
            print(food_id,self.target_brand,self.meal_time_transfered,self.calories,self.fat,self.carbs,self.fiber,self.protein)
            food_data = food_tb(Food_ID = food_id, Brand = self.target_brand,
                                            Meal= self.target_food,
                                            Calories = self.calories,Fat = self.fat,
                                            Carbs = self.carbs, Fiber = self.fiber, Protein = self.protein)
            session.add(food_data)
            session.commit()

        #record 
        record_id = session.query(record_tb).count()+1
        record_data = session.add(record_tb(Record_ID = record_id, Time = self.date, 
                                                Meal_Time = self.meal_time_transfered,
                                                Food_ID = food_id, User_ID = 1))
        session.commit()
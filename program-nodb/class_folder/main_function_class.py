from function_folder.functions_file import static, back_to_menu
from class_folder.parse_class import Parse
from class_folder.user_class import User
from class_folder.inputs_class import Inputs
from class_folder.food_class import Food


#main menu lists
class main_function():
    def __init__(self):
        self.web_url = None
        self.driver = None
        self.user_info = None

    
    #static for start record and star visulize function
    def __start__(self):
        web_url, driver = static()
        parse_tool = Parse(web_url, driver)
        parse_tool.create_file()
        user_info = User()
        user_info.create_user()
        self.web_url = web_url
        self.driver = driver
        self.user_info = user_info
    
    #start the recording function
    def start_record(self):
        user_input = Inputs(self.web_url, self.driver)
        date, meal_time_transfered, target_brand, target_food, calories, fat, carbs, fiber, protein = user_input.get_inputs()
        food_nutrition = Food(date, meal_time_transfered, target_brand, target_food, calories, fat, carbs, fiber, protein)
        food_nutrition.show_info()
        food_nutrition.save_result()
        back_to_menu()
 
    #start the visualizing functino   
    def start_visualize(self):
        self.user_info.start_visualize()
        back_to_menu()
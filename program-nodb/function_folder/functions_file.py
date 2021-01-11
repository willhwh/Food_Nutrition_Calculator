#for parsing food info
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#create varaibles for future usage
def static():
    web_url = 'https://www.calorieking.com/us/en/foods/'
    
    #chrome setting
    def start_program():
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(options=options)
        return driver
    
    #chrome driver
    driver = start_program()
    
    return web_url, driver


#back to main menu
def back_to_menu():
    print('Back to Main Menu.')
    pass

#get user command
def get_command():
    '''
    Get command, upper-case it
    '''
    print("'A' => Add to Record")
    print("'V' => View Daily Intake")
    print("'Q' => Quit")
    command = input("Enter command: ").upper()
    return command
const serverBaseURL = "http://127.0.0.1:5000";
const nullLabel = "Unknown";




function goal_calculate_trigger() {
    
    weight = document.getElementById("weight").value
    activity_level = document.getElementById("activity_level").value.toUpperCase()
    purpose = document.getElementById("purpose").value.toUpperCase()
    check_string = ['A','B','C']
    console.log(weight)

    if (check_string.indexOf(activity_level) >= 0 && check_string.indexOf(purpose)>=0 && weight>0){
        target_calories = document.getElementById('target_calories')
        target_proteins = document.getElementById('target_proteins')
        target_fat = document.getElementById('target_fat')
        target_carbs = document.getElementById('target_carbs')
        calories_dict = {'AA': 35, 'AB': 30, 'AC': 25,
                        'BA': 40, 'BB': 35, 'BC': 30,
                        'CA': 45, 'CB': 40, 'CC': 35}
        cal_coefficient = calories_dict[activity_level+purpose]
        target_calories.value = Math.round(cal_coefficient*weight)
        target_proteins.value = Math.round(target_calories.value * 0.3/4)
        target_fat.value = Math.round(target_calories.value * 0.2/9)
        target_carbs.value = Math.round(target_calories.value * 0.5/4)
    }

    else {
        //document.getElementById('target_form').reset()
        document.getElementById('weight').value=""
        document.getElementById('activity_level').value =''
        document.getElementById('purpose').value=''
        window.alert('Please enter number for itme 1, and A, B, or C for item 2 and item 3. Try again, thanks.')

    }


};



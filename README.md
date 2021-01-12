# food_nutrition_calculator
<em>Will Huang</em>
<br>


## Project Summary
<hr>
This project is a food nutritions recording program that parses food data from [CalorieKing](
https://www.calorieking.com/us/en/) and stores the nutritions information into a postgreSQL database. Also, a user can query the database to see if a certain day meet the daily target intake nutritions.

<ol>
<li>To begin I created a postgreSQL database, food, via PgAdmin. </li>
<li>Next, I used QuickDBD to create the schemea of the food database with 3 tables, including Food table, User table, and Record table.</li>
<li>Next, I exported the schema as a SQL script.</li>
<li>Next, I ran the SQL script in PgAdmin to create the talbes and the relationships.</li>
<li>Lastly, I wrote the parsing, storing, and visulizing functions for the program with Python.</li>
<li>At this point, a user can type in the resetaurant's name and the meal name to search for the nutritions of the meal. The program will store the data into database and provid the function of visualizing the daily target nutritions and daily intaken nutritions with pie plots.
</li>
</ol>

## How to Run
<hr>

### Setup Database



### Run Program
#### Enter User Info If It Is the First Time of Using the Program

#### Main Functions


<hr>

## Example
Sample User Information:
<ul>
    <li>User Weight: 70
    </li>
    <li>Activity Level: (B) Medium
    </li>
    <li>Diet Purpose: (A) Gain Weight
    </li>
</ul>

Sample User's Diet Records:
<ul>
Date: 01/13/2021
    <li>Breakfast
    </li>
    <li>Lunch
    </li>
    <li>Dinner
    </li>
    <li>Other
    </li>
    <li>Other
    </li>
</ul>

Sample User's Daily Intaken Condition Visuals: 
<ul>
Date: 01/13/2021
    <li>Breakfast
    </li>
    <li>Lunch
    </li>
    <li>Dinner
    </li>
    <li>Other
    </li>
    <li>Other
    </li>
</ul>
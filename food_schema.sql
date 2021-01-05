-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "Food" (
    "Food_ID" int   NOT NULL,
    "Brand" varchar   NOT NULL,
    "Meal" varchar   NOT NULL,
    "Calories" int   NOT NULL,
    "Fat" int   NOT NULL,
    "Carbs" int   NOT NULL,
    "Fiber" int   NOT NULL,
    "Protein" int   NOT NULL,
    CONSTRAINT "pk_Food" PRIMARY KEY (
        "Food_ID"
     )
);

CREATE TABLE "Record" (
    "Record_ID" int   NOT NULL,
    "Time" char(8)   NOT NULL,
    "Meal_Time" str   NOT NULL,
    "Food_ID" int   NOT NULL,
    "User_ID" int   NOT NULL,
    CONSTRAINT "pk_Record" PRIMARY KEY (
        "Record_ID"
     )
);

CREATE TABLE "User" (
    "User_ID" int   NOT NULL,
    "Target_Calories" int   NOT NULL,
    "Target_Protein" int   NOT NULL,
    "Target_Carbs" int   NOT NULL,
    "Target_Fat" int   NOT NULL,
    CONSTRAINT "pk_User" PRIMARY KEY (
        "User_ID"
     )
);

ALTER TABLE "Record" ADD CONSTRAINT "fk_Record_Food_ID" FOREIGN KEY("Food_ID")
REFERENCES "Food" ("Food_ID");

ALTER TABLE "Record" ADD CONSTRAINT "fk_Record_User_ID" FOREIGN KEY("User_ID")
REFERENCES "User" ("User_ID");


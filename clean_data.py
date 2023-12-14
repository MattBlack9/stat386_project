import collegefood as cf
import pandas as pd

food = pd.read_csv("college_food.csv")

columns = ["GPA","Gender","comfort_food","comfort_food_reasons","cook","diet_current","eating_changes","eating_changes_coded","eating_out","exercise",
           "father_profession","fav_cuisine","fruit_day","grade_level","income","marital_status","mother_education","on_off_campus",
           "self_perception_weight","sports","vitamins","weight"]
food2 = cf.keep_columns(dataframe=food,columns_to_keep=columns)  

cf.cleaning_col(column="weight",data=food2,type=float)
cf.cleaning_col(column="GPA",data=food2,type=float)

food2.to_csv("food_cleaned.csv")
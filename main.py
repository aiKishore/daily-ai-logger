# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 15:35:51 2023
Daily AI Productivity Logger

@author: Dr.KB
"""

from datetime import datetime

operation_choice = input("To read your log enter 1,to save enter 2 and for summarizing enter 3:")
file_path = "log.txt"


if operation_choice == "1":
    with open(file_path, "r") as file:
        content = file.read()
        if not content:
            print("No logs found yet.")
        else:
            print("\n--------- All logs----------")
            print(content)
        
elif operation_choice == "2":
    name = input("Please enter your first name: ")
    daily_AI_goal = input("Your today's AI related goal: ")
    
    now = datetime.now()
    dateNtime = now.strftime("%d/%m/%Y %H:%M:%S")
    
    with open(file_path, "a") as file:
        file.write(f"{dateNtime} | {name} | {daily_AI_goal}\n")
        
    print("log saved successfully")
        
elif operation_choice == "3":
    print("Not implemented yet!")
    
else:
    print("Invalid input, try again.")


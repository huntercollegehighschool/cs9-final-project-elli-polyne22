"""
Name(s): Ellison and Josie
Name of Project: Summer Themed Mad Lib
"""

print("Welcome to Josie and Ellison's Mad Libs game! This game is compromised of 4 short stories in which you will be asked to give either a noun, verb or adjective. These words will be placed into the story.")

program = int(input("Which code (1 or 2 or 3 or 4)? "))
if program == 1:
  import page1
if program == 2:
  import page2
if program == 3:
  import page3
if program == 4:
  import page4
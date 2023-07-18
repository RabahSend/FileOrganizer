import os
import sorts

Directory = ""
titleMenu = r"""
  ______ _ _                                    _              
 |  ____(_) |                                  (_)             
 | |__   _| | ___    ___  _ __ __ _  __ _ _ __  _ _______ _ __ 
 |  __| | | |/ _ \  / _ \| '__/ _` |/ _` | '_ \| |_  / _ \ '__|
 | |    | | |  __/ | (_) | | | (_| | (_| | | | | |/ /  __/ |   
 |_|    |_|_|\___|  \___/|_|  \__, |\__,_|_| |_|_/___\___|_|   
                               __/ |                           
                              |___/                            
"""

print(titleMenu)

while (not os.path.exists(Directory)):
  Directory = input("Choose an existing root directory:")

options = {
    "First sort" : sorts.firstSort
}

print("Now choose the option you want to use to organize your directory:")

for i in range(len(options)):
  print(i + 1, " - ", list(options.keys())[i])

choice = int(input("Your choice: "))

keys = list(options.keys())
options[keys[choice - 1]](Directory)
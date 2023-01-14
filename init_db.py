import sqlite3

conn = sqlite3.connect('./database.db')
cur = conn.cursor()


# Create Accounts table
cur.execute("CREATE TABLE accounts(id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, email TEXT, password TEXT)")

# Create food plan table
cur.execute("CREATE TABLE food_plan(userid INTEGER, name TEXT)")

# Create shopping list table
cur.execute("CREATE TABLE shopping_list(userid INTEGER, ingred_name TEXT, quantity INTEGER)")

# Create current items table
cur.execute("CREATE TABLE curr_items(userid INTEGER, ingred_name TEXT, quantity INTEGER)")

# Create recipes table
cur.execute("CREATE TABLE recipes(userid INTEGER, recipe_name TEXT, ingredients TEXT)")

# Insert data into table
cur.execute("INSERT INTO recipes(userid, recipe_name, ingredients) VALUES (?,?,?)", (0, "BLT-Sandwich", "Bacon.3_Bread.1_Mustard.1_Lettuce.1_Tomato(es).1"))

cur.execute("INSERT INTO recipes(userid, recipe_name, ingredients) VALUES (?,?,?)", (0, "Steak", "Steak.1_Potato(es).3_Lettuce.1_Tomato(es).1_Butter.3_Salt.1_Pepper.1_Canola Oil.1_Garlic.3_Thyme.3_Rosemary.2"))

cur.execute("INSERT INTO recipes(userid, recipe_name, ingredients) VALUES (?,?,?)", (0, "Carbonara", "Olive Oil.1_Bacon.1_Eggs.3_Parmesan.1_Packet of Spaghetti.1_Salt.1_Pepper.1"))

cur.execute("INSERT INTO recipes(userid, recipe_name, ingredients) VALUES (?,?,?)", (0,"Veggie-Pasta", "Zucchini.1_Squash.1_Red Pepper(s).1_Packet of Spaghetti.1_Salt.1_Pepper.1_Packet Of Peas.1_Onion.1_Garlic.1_Tomato Can.1_Parsley.1_Mint.1_Oregano.1_Pepper flakes.1_Basil.1_"))

cur.execute("INSERT INTO recipes(userid, recipe_name, ingredients) VALUES (?,?,?)", (0, "Cake-Pops", "Cake Mix.1_Eggs.3_Frosting.1_Sprinkles.1_Oil.1_Sticks.1_Candy.1_Frosting.1"))

cur.execute("INSERT INTO recipes(userid, recipe_name, ingredients) VALUES (?,?,?)", (0, "Smoked-Salmon", "Salmon.1_Salt.1_Pepper.1_Oil.1_Lemon.1"))

cur.execute("INSERT INTO recipes(userid, recipe_name, ingredients) VALUES (?,?,?)", (0, "Eggs-Benedict", "Bacon.8_Eggs.7_Vinegar.2_English Muffins.2_Butter.2_Lemon.1_Parsley.2_Salt.1"))

cur.execute("INSERT INTO recipes(userid, recipe_name, ingredients) VALUES (?,?,?)", (0, "Banh-Mi", "Baguette.1_Green Onion.2_Coriander.1_Mayo.1_Carrot.2_Cucumber.1_Chilli.2_Pate.1_Slice(s) of Pork.2"))


cur.execute("INSERT INTO accounts(username, email, password) VALUES (?, ?, ?)", ('tom', 'tom@gmail.com', 'tommy'))




conn.commit()
conn.close()



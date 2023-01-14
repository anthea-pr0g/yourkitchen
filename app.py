import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
USERNAME = ''
USERID = ''

@app.route('/', methods=['POST', 'GET'])
def home():
    if not USERNAME:
       return redirect(url_for('login'))
    with sqlite3.connect('./database.db') as conn:
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        cur.execute(f"SELECT recipe_name FROM recipes WHERE userid = 0")
        data = cur.fetchall()
        recipe_list = []
        for r in data:
            recipe_list.append(r[0])
        

    if request.method == 'POST':
        option = request.form['myselect']
        print(option)
        cur.execute("INSERT INTO food_plan(userid, name) VALUES (?,?)", (USERID, option))
        conn.commit()

    with sqlite3.connect('./database.db') as conn:
        conn.row_factory = lambda cursor, row: row[0]
        cur = conn.cursor()
        cur.execute(f"SELECT name FROM food_plan WHERE userid = USERID")
        chosen_food = cur.fetchall()
        print(chosen_food)
        return render_template('home.html', username=USERNAME, food=data, chosen_food=chosen_food)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        email = request.form['email']
        password = request.form['password']

        with sqlite3.connect('./database.db') as conn:
            cur = conn.cursor()
            cur.execute(f"SELECT id, username FROM accounts WHERE email='{email}' AND password='{password}'")
            user_info = cur.fetchone()
            if not user_info:
                return render_template('login.html')
            global USERNAME, USERID
            USERNAME = user_info[1]
            USERID = user_info[0]
        return redirect(url_for('home'))


@app.route('/recipes', methods=['POST', 'GET'])
def recipes():
    with sqlite3.connect('./database.db') as conn:
        cur = conn.cursor()
        cur.execute(f"SELECT ingredients FROM recipes WHERE userid = 0")
    return render_template('recipes.html')

@app.route('/groceries', methods=['POST', 'GET'])
def groceries():
    curr_items = []
    #curr_item_num = []
    with sqlite3.connect('./database.db') as conn:
        cur = conn.cursor()
        cur.execute(f"SELECT ingred_name, quantity FROM curr_items WHERE userid = USERID")
        items = cur.fetchall()
        for i in items:
            full_name = str(i[1]) + " " + i[0]
            curr_items.append(full_name)
            
        #cur.execute(f"SELECT ingredients FROM recipes WHERE userid = USERID")

    if request.method == 'GET':
        return render_template('groceries.html', existing_food=curr_items)
    else:
        quantity = request.form['quantity']
        ingred_name = request.form['ingred_name']

        with sqlite3.connect('./database.db') as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO curr_items(userid, ingred_name, quantity) VALUES (?,?,?)", (USERID, ingred_name, quantity))
            
        return render_template('groceries.html', existing_food=curr_items)


@app.route('/leftovers', methods=['POST', 'GET'])
def leftovers():
    with sqlite3.connect('./database.db') as conn:
        cur = conn.cursor()
        cur.execute(f"SELECT ingredients FROM recipes WHERE userid = 0")
        data = cur.fetchone()
        ingred = data[0].split("_")
        for item in ingred:
            res = item.split(".")
            item_name = res[0]
            item_count = res[1]
            print("My items are: " + item_count + " " + item_name)

    return render_template('leftovers.html')

@app.route('/form', methods=['POST', 'GET'])
def form():
    return render_template('form.html')


if __name__ == '__main__':
    app.run(port=8081, debug=True)
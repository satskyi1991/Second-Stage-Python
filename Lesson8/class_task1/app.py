from flask import Flask
from flask import render_template
import sqlite3
app = Flask(__name__)


conn = sqlite3.connect('Goods.db')
cursor = conn.cursor()

category = []
cursor.execute("SELECT * FROM category")
for id,name in cursor:
    category.append({'id': id,'name': name})

good = []
cursor.execute("SELECT * FROM goods")
for category_id, id, name, price, availability, number_of_units in cursor:
    good.append({'category_id': category_id,
                  'id':id,
                  'name':name,
                  'price':price,
                  'availability': availability,
                  'number_of_units':number_of_units,})
# print(good)

good1 =[]
good2 =[]
good3 =[]
for elem in good:
    if elem.get("category_id") == '1':
        good1.append(elem)
    elif elem.get("category_id") == '2':
        good2.append(elem)
    elif elem.get("category_id") == '3':
        good3.append(elem)

print(good1)

conn.close()
@app.route('/')
@app.route('/<int:category_id>')
def categories(category_id = None):
    if category_id == 1:
        return render_template('goods.html', goods = good1)
    if category_id == 2:
        return render_template('goods.html', goods = good2)
    if category_id == 3:
        return render_template('goods.html', goods = good3)
    return render_template('categories.html', categories = category)

# @app.route('/<int:category_id>/<good_id>')
# def categories(good_id = None):
#     if category_id == 1:
#         return render_template('goods.html', goods = good1)
#     if category_id == 2:
#         return render_template('goods.html', goods = good2)
#     if category_id == 3:
#         return render_template('goods.html', goods = good3)
#     return render_template('categories.html', categories = category)

#return render_template('goods.html', categories = category[category_id -1])
if __name__ == '__main__':
    app.run(debug = True)

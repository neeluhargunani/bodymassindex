from flask import Flask, render_template, request
import pymysql


class MyClass():
    def __init__(self):
        host = "localhost",
        user = "root",
        password = "webcreationz@1234",
        database = "db1",
        self.con = pymysql.connect(host=host, user=user, password=password,
                                   database=database, cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()

    def bmi_height(self):
        self.cur.execute("SELECT * FROM bmiheight")
        result = self.cur.fetchall()
        return result
app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def calculator():
    bmi = ''
    if request.method == 'POST' and 'weight' in request.form and 'height' in request.form:
        name = request.form.get('name')
        w = float(request.form.get('weight'))
        h = float(request.form.get('height'))
        bmi = round(w/((h/100)**2), 2)
        if bmi < 18.5:
            bmi = f"Hello {name} Your {bmi} weight is underweight..! you need to follow the healthy tips below"
        elif bmi < 26:
            bmi = f"Hello {name} we are happy to inform...! your {bmi} weight has optimal (normal) weight"
        else:
            bmi = f"Hello {name} Your {bmi} weight is overweight..! you need to follow the healthy tips below"



    def db_query():
        db = MyClass()
        bmih = db.bmi_height()
        return bmih

    res = db_query()

    return render_template("index.html", bmi=bmi, results=res)


if __name__ == '__main__':
    app.run(debug=True)

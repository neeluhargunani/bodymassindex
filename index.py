from flask import Flask, render_template, request

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

    return render_template("index.html", bmi=bmi)


if __name__ == '__main__':
    app.run(debug=True)

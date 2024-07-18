from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pre_mas = float(request.form['mas'])
        volume3 = round(0.378 * pre_mas, 2)
        volume4 = round(0.907 * pre_mas, 2)
        volume5 = round(2.364 * pre_mas, 2)
        volume6 = round(2.364 * pre_mas, 2)
        volume7 = round(0.916 * pre_mas, 2)
        volume8 = round(0.889 * pre_mas, 2)
        volume9 = round(1.125 * pre_mas, 2)
        volume10 = round(0.067 * pre_mas, 2)
        return render_template('index.html', volume3=volume3, volume10=volume10
                               , volume4=volume4, volume5=volume5, volume6=volume6, volume7=volume7
                               , volume8=volume8, volume9=volume9)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

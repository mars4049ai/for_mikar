from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pre_mas = float(request.form['mas'])
        volume2 = 27.072 * pre_mas
        volume3 = 0.378 * pre_mas
        volume4 = 0.907 * pre_mas
        volume5 = 0.377 * pre_mas
        volume6 = 2.364 * pre_mas
        volume7 = 0.916 * pre_mas
        volume8 = 0.889 * pre_mas
        volume9 = 1.125 * pre_mas
        volume10 = 0.067 * pre_mas
        return render_template('index.html',  volume2=volume2, volume3=volume3, volume10=volume10
                               , volume4=volume4, volume5=volume5, volume6=volume6, volume7=volume7
                               , volume8=volume8, volume9=volume9)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request



app = Flask(__name__)




@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pre_mas = float(request.form['mas'])
        volume_mer = round(0.378 * pre_mas, 2)
        volume_ven = round(0.907 * pre_mas, 2)
        volume_mars = round(2.364 * pre_mas, 2)
        volume_qpt = round(2.364 * pre_mas, 2)
        volume_ctr = round(0.916 * pre_mas, 2)
        volume_yrn = round(0.889 * pre_mas, 2)
        volume_nep = round(1.125 * pre_mas, 2)
        volume_plt = round(0.067 * pre_mas, 2)
        return render_template('index.html', volume_mer=volume_mer, volume_plt=volume_plt
                               , volume_ven=volume_ven, volume_mars=volume_mars, volume_qpt=volume_qpt, volume_ctr=volume_ctr
                               , volume_yrn=volume_yrn, volume_nep=volume_nep)
    return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True)

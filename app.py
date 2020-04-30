from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/results', methods=['GET', 'POST'])
def results():

    if request.method == 'POST':
        data = request.form
        return render_template('results.html', data=data)
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)

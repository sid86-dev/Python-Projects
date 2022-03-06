import shutil
import os


from flask import Flask, render_template, request
from gen_qr import*

app = Flask(__name__)


cwd = os.getcwd()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/genqr', methods=['GET', 'POST'])
def gen():
    initial = "no"
    if request.method == "POST":
        link = request.form.get('link')
        text = request.form.get('text')

        print(link)
        print(text)

        if link != "": 
            gen_qr(link)
            initial = "yes"
            
        elif text != "": 
            gen_qr(text)
            initial = "yes"

        else:
            initial = "no"

        # copy paste
        original = f'{cwd}\qr.png'
        target = f'{cwd}\static\qr.png'
        shutil.copyfile(original, target)

    return render_template('genqr.html', initial=initial)

if __name__ == "__main__":
    app.run(debug=True)



from flask import render_template, Flask, request

app = Flask(__name__)

# @app.route('/', methods =['GET','POST'])
#
# @login_required
#     def home():
#     error = None
#     form = PostForm(request.form)
#     if form.validate_on_submit() :
#         info = form.info.data
# def index():
#     return render_template('index.html')
#
# if __name__ == '__main__':
#     app.run(debug=True)     ## pass DEBUG param
#

@app.route('/')
def my_form():
    #return render_template("my-form.html")
    return render_template("index.html")

@app.route('/', methods=['POST'])
def my_form_post():

    text = request.form['text']
    processed_text = text.upper()
    return processed_text

@app.route('/test', methods=['POST'])
def submitted():
    first_name = request.form.get('firstname')
    last_name = request.form.get('lastname')
    return first_name + " " + last_name

if __name__ == '__main__':
    app.run(debug = True)
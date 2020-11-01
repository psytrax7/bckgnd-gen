from flask import Flask, render_template, url_for
app = Flask(__name__)
print(__name__)

@app.route('/') #decorator 
def Abhinav_Home():
    return render_template('index.html')

@app.route('/location') #decorator 
def location():
    return 'Ranchi-834009'


@app.route('/<string:page_name>') #decorator 
def html_page(page_name):
    return render_template(page_name)





# @app.route('/favicon.ico') #decorator 
# def favio():
#     return 




if __name__== "__main__":
	app.run(debug=True)

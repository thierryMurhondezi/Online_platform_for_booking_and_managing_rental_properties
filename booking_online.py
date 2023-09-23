from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    location = request.form['location']
    num_bedrooms = request.form['num_bedrooms']
    max_price = request.form['max_price']
    # Perform search logic here using above variables
    # Return search results as HTML
    return "Search results for {} bedrooms in {} under ${}".format(num_bedrooms, location, max_price)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('forums.html')

@app.route('/category.html')
def load_category():
    return render_template('category.html')

@app.route('/post.html')
def load_post():
    return render_template('post.html')

@app.route('/create_post.html')
def load_create_post():
    return render_template('create_post.html')

@app.route('/create_post', methods=['POST'])
def create_post():
    # Process the form data
    # For now, let's just redirect back to the category page
    return redirect(url_for('load_category'))

if __name__ == '__main__':
    app.run(debug=True)
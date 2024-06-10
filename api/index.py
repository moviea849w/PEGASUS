import os
from flask import Flask, render_template

app = Flask(__name__)

DATA_FOLDER = os.path.join(os.path.dirname(__file__), 'data')

def create_route(filename):
    def route():
        data = {}
        with open(os.path.join(DATA_FOLDER, filename), 'r') as f:
            for line in f:
                if ': ' in line:
                    key, value = line.split(': ', 1)
                    data[key.strip()] = value.strip()
        
        return render_template("post.html", data=data, title=data.get('Name', 'No Title'))
    
    route_name = filename.replace('.so', '_so')
    app.add_url_rule(f'/{filename.replace(".so", "")}', endpoint=route_name, view_func=route)
    print(f"Created route: /{filename.replace('.so', '')}")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about") 
def about(): 
    return render_template("about.html")

@app.route("/genre") 
def genre(): 
    return render_template("genre.html")

@app.route("/posts")
def posts():
    posts_data = []
    for filename in os.listdir(DATA_FOLDER):
        if filename.endswith('.so'):
            post = {}
            post['filename'] = filename.replace('.so', '')
            with open(os.path.join(DATA_FOLDER, filename), 'r') as f:
                for line in f:
                    if ': ' in line:
                        key, value = line.split(': ', 1)
                        post[key.strip()] = value.strip()
            posts_data.append(post)
    return render_template("posts.html", posts=posts_data)

if __name__ == "__main__":
    # Dynamically create routes for each .so file in the data folder
    if os.path.exists(DATA_FOLDER):
        for filename in os.listdir(DATA_FOLDER):
            if filename.endswith('.so'):
                create_route(filename)
    else:
        print(f"Data folder not found: {DATA_FOLDER}")
    
    app.run(debug=True)

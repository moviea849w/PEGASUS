from flask import Flask, render_template
import os

app = Flask(__name__)

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
    data_folder = os.path.join(os.path.dirname(__file__), 'data')
    for filename in os.listdir(data_folder):
        if filename.endswith('.so'):
            post = {}
            post['filename'] = filename.replace('.so', '')
            with open(os.path.join(data_folder, filename), 'r') as f:
                for line in f:
                    key, value = line.split(': ', 1)
                    post[key.strip()] = value.strip()
            posts_data.append(post)
    return render_template("posts.html", posts=posts_data)

def create_route(filename):
    def route():
        data = {}
        data_folder = os.path.join(os.path.dirname(__file__), 'data')
        with open(os.path.join(data_folder, filename), 'r') as f:
            for line in f:
                key, value = line.split(': ', 1)
                data[key.strip()] = value.strip()
        
        return render_template("post.html", data=data, title=data['Name'])
    
    route.__name__ = filename.replace('.so', '_so')
    app.add_url_rule(f'/{filename.replace(".so", "")}', route.__name__, route)
    print(f"Created route: /{filename.replace('.so', '')}")

# Dynamically create routes for each .so file in the data folder
data_folder = os.path.join(os.path.dirname(__file__), 'data')
if os.path.exists(data_folder):
    for filename in os.listdir(data_folder):
        if filename.endswith('.so'):
            create_route(filename)
else:
    print(f"Data folder not found: {data_folder}")

if __name__ == "__main__":
    app.run(debug=True)

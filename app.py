import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
<center>
    <h1> <a href="https://mraman.onrender.com">Welcome to My website </a></h1>
    <p style="color:blue;"> This is the first website by Aman using HTML </p>
    <img src="https://graph.org/file/5c0eca2c261e127d7bba1.jpg" alt="https://github.com/Amanraj654/Test" style="border-radius: 12px;"/> 
</center> 
<style>
    body { 
        background: pink;
    }
</style>"""

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

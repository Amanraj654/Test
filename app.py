import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
<center>
    <h1> <a href="https://mraman.onrender.com"><b>Welcome to My website</b> </a></h1>
    <h3 style="color:blue;"> <em>This is the first website by Aman using HTML </em> </h3>
    
    <a href="https://www.youtube.com/embed/wTjszS6qFm8"> <img src="https://graph.org/file/5c0eca2c261e127d7bba1.jpg"> </a> 
    <hr> <hr> <br>
    <iframe width="900" height="600" src="https://www.youtube.com/embed/wTjszS6qFm8">
</iframe>

</center>

<style>
    body { 
        background: pink;
    }
</style>"""

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

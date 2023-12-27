import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
<center> 
    <img src="https://graph.org/file/5c0eca2c261e127d7bba1.jpg" style="border-radius: 12px;"/> 
</center> 
<style>
    body { 
        background: pink;
    }
</style>"""

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

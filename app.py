from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")
    return """
<!DOCTYPE html>
<html>
<head>
    <title>My Page</title>
</head>
<body>
<div>
    <center>
        <h1>
            Hello you are  in the HELL
        </h1>
        <p>-------------------------------------------------------------</p>
    </center>

</body>
</html>
    """.format(time=the_time)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

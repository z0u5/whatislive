from flask import Flask
app = Flask(__name__)

@app.route('/')
def homepage():
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
    <h4>Hi, I use this site for my RAT or Backdoor</h4>

</body>
</html>
    """

if __name__ == '__main__':
    app.run(port = 5000)

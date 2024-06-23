#!C:/Users/Dhanush P/AppData/Local/Programs/Python/Python311/python.exe
print("Content-type:text/html\r\n\r\n")
print("""
  <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Login</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" 
    integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
    <link rel="stylesheet" href="/car/css/smart.css">
</head>
<body class="bgimg">
    <section class="bglog py-3">
        <div class="container login2">
            <div class="row">
                <div class="col-md-12">
                    <form method="post" enctype="multipart/form-data">
                        <div class="username1 mb-3">
                          <label for="username" class="" style="color:white;">Username:</label>
                          <input type="text" class="form-control" id="" aria-describedby="" name="Username">
                        </div>
                        <div class="password1 mb-3">
                          <label for="exampleInputPassword1" class="form-label" style="color:white;">Password:</label>
                          <input type="password" class="form-control" id="" name="Password">
                        </div>
                        <div class="fpass"> 
                            <a href="" style="text-decoration: none; color:white;">Forget password</a><a href="" style="margin-left: 75px;text-decoration: none; color:white ; font-size: 15px;">Create acc?</a>
                        </div>
                        <center>
                            <div style="margin-top:20px;">
                                <input type="submit" class="login1 btn btn-primary" value="LOGIN" name="submit"> 
                            </div>
                        </center> 
                    </form>
                </div>
            </div>
        </div>
    </section>
</body>
</html>""")

import cgi
import cgitb
import pymysql
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="cars")
cur = con.cursor()
form = cgi.FieldStorage()
username = form.getvalue("Username")
password = form.getvalue("Password")
submit = form.getvalue("submit")

if submit != None:
    q = """SELECT id from userreg WHERE Username='%s' and Password='%s' """ % (username, password)
    cur.execute(q)
    rec = cur.fetchone()
    if rec != None:
        print("""
            <script>
            alert("Login success");
            window.location.href = "user_dashboard.py?id=%s";
            </script>
            """ % rec[0])

#!C:/Users/Dhanush P/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgi,cgitb,pymysql
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="cars")
cur = con.cursor()
form = cgi.FieldStorage()
y=form.getvalue("id")
q1="""select Name from userreg where id=%s"""%y
cur.execute(q1)
name=cur.fetchone()
pro=name[0]

print("""
       <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>user_dashboard</title> 
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" 
    integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" 
    integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
</head>
<style>
    .bootom a{
      text-decoration: none;
      font-size: 18px;
        font-weight: 500;
        display: flex;
        justify-content: center;
        margin-top: 100px;
    }   
</style>
<body>
     <nav class="navbar bg-body-tertiary fixed-top">
        <div class="container-fluid">
            <button class="navbar-toggler" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasNavbar" aria-controls="offcanvasNavbar" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon "></span>
              </button>
          <a class="navbar-brand" href="#">SMART</a>
           <div class="offcanvas offcanvas-start" tabindex="-1" id="offcanvasNavbar" aria-labelledby="offcanvasNavbarLabel" style="width: 300px;">
            <div class="offcanvas-header">
              <h5 class="offcanvas-title" id="offcanvasNavbarLabel">USER</h5>
              <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
            </div>
            <div class="offcanvas-body">
              <ul class="navbar-nav justify-content-start flex-grow-1 pe-3">
                     <li><a class="dropdown-item" href="user_profile.py?id=%s" style="font-size: 20px;">MY PROFILE</a></li>
                        <li><a class="dropdown-item" href="buy_car.py?id=%s"  style="font-size: 20px; margin-top: 20px;">BUY CAR</a></li> 
                        <li><a class="dropdown-item" href="pay_advance.py?id=%s"  style="font-size: 20px; margin-top: 20px;">PAY ADVANCE</a></li>  
              </ul>
              <div class="bootom">
                <a href="index.py">LOG OUT</a>
              </div>
            </div>
          </div>
        </div>
      </nav>""" %(y,y,y))
q = """SELECT * FROM booking_details where buyer_name='%s' """ % (name)
cur.execute(q)
rec = cur.fetchall()

print("""
      <section>
        <div class="container py-5">
            <div class="row">
                <div class="col-md-12">
                    <div class="py-3"><h4>USERS</h4></div>
                    <table class="table">
                        <thead>
                          <tr>
                            <th scope="col">id</th>
                            <th scope="col">buyer_name</th>
                            <th scope="col">price</th>
                            <th scope="col">car_name</th>
                            <th scope="col">car_model</th>
                            <th scope="col">seller_name</th>
                            <th scope="col">advance</th>
                            <th scope="col">adstatus</th>
                            <th></th>
                          </tr>
                </div>
            </div>""")
for i in rec:
    print(""" 
           <tr>
               <form method="post" enctype="multipart/form-data">                
               <td>%s</td>
               <td>%s</td>
               <td>%s</td>
               <td>%s</td>
               <td>%s</td>
               <td>%s</td>
               <td>%s</td>
               <td>%s</td>
               <td><input type="submit" class="btn btn-success" value="pay" name="submit" data-bs-toggle="modal" data-bs-target="#myModal%s" style="margin: 20px;color:black;font-weight: bold;">
           </form>
           </tr>""" % (i[0], i[1], i[3],i[4],i[5],i[6],i[8],i[9],i[0]))
psumbit = form.getvalue("submit")
if psumbit != None:
 print("""
            <script>
            window.location.href = "buynow.py?id=%s";
            </script>
            """ % y[0])


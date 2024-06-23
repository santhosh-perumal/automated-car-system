#!C:/Users/Dhanush P/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import cgi, cgitb, pymysql, smtplib
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="cars")
cur = con.cursor()
y = cgi.FieldStorage()
print("""
     <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title> 
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" 
    integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
   <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</head>
<style>
  .navbar-nav .nav-item a{
        font-size: 18px;
        font-weight: 500;
        /* padding-bottom: 35px; */
    }
    .bootom a{
      text-decoration: none;
      font-size: 18px;
        font-weight: 500;
        display: flex;
        justify-content: center;
        margin-top: 300px;
        color:red;
    } 
    .offcanvas-header a{
      text-decoration: none;
      font-size: 18px;
        font-weight: 500;
      color: black;
      cursor: pointer;
    }

</style>
<body>
    <nav class="navbar bg-body-tertiary fixed-top">
        <div class="container-fluid" style="background-color: rgb(139, 161, 161);">
            <button class="navbar-toggler" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasNavbar" aria-controls="offcanvasNavbar" aria-label="Toggle navigation" style="color:rgb(5, 5, 22); background-color:rgb(165, 231, 198);">
                <span class="navbar-toggler-icon "></span>
              </button>
          <img src="../media/wepik-gradient-professional-car-repair-company-logo-202404290727286CgX.png" alt="" style="width: 100px; height: 100px;">
          
          <div class="offcanvas offcanvas-start" tabindex="-1" id="offcanvasNavbar" aria-labelledby="offcanvasNavbarLabel" style="width: 300px;">
            <div class="offcanvas-header">
              <h5 class="offcanvas-title" id="offcanvasNavbarLabel" style="color: black;">ADMIN</h5>
              <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
            </div>
            <div class="offcanvas-body" style="background-color: rgb(51, 21, 21); color: white;">
              <ul class="navbar-nav justify-content-start flex-grow-1 pe-3">
                <div class="nav-item">
                  <li class="nav-item dropdown">
                  <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false" style="color: aliceblue">
                    BUYERS
                  </a>
                  <ul class="dropdown-menu" style="border:0px;">
                   <li><a class="dropdown-item" href="new_user.py">NEW-USERS</a></li>
                    <li><a class="dropdown-item" href="exeuser.py">EXISITING-USERS</a></li>
                    </ul>
                </li>
                  <ul class="navbar-nav justify-content-start flex-grow-1 pe-3">
                    <div class="nav-item">
                      <a class="nav-link active" aria-current="page" href="#"></a>
                      <li class="nav-item dropdown">
                      <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false"  style="color: aliceblue">
                        SELLERS
                      </a>
                      <ul class="dropdown-menu" style="border:0px;">
                        <li><a class="dropdown-item" href="newseller.py">NEW-SELLER</a></li>
                        <li><a class="dropdown-item" href="exeseller.py">EXEISTING-SELLER</a></li>
                        <li><a class="dropdown-item" href="cars.py">CARS-DETAILS</a></li>
                      </ul>
                     
                </li>
              </ul>
               <ul class="navbar-nav justify-content-start flex-grow-1 pe-3">
                    <div class="nav-item">
                      <a class="nav-link active" aria-current="page" href="#"></a>
                      <li class="nav-item dropdown">
                      <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false"  style="color: aliceblue">
                        EMPOLYEES
                      </a>
                      <ul class="dropdown-menu" style="border:0px;">
                        <li><a class="dropdown-item" href="empreg.py">ADD-EMPLOYEE</a></li>
                        <li><a class="dropdown-item" href="emp_details.py">EMP-DETAILS</a></li>
                        
                      </ul>
                     
                </li>
              </ul>
              <div class="bootom">
                <a href="index.py">LOG OUT</a>
              </div>
            </div>
          </div>
        </div>
      </nav>""")
q = """select * from userreg where Status="New" """
cur.execute(q)
det = cur.fetchall()
print("""
      <section>
        <div class="container py-5" style="margin-top:20px" >
            <div class="row">
                <div class="col-md-12">
                <center>
                    <div class="py-5" ><h4>NEW-USERS ARRIVED</h4></div> 
                    </center>
                    <table class="table">
                        <thead>
                          <tr>
                            <th scope="col">Id</th>
                            <th scope="col">Name</th>
                            <th scope="col">Contact</th>
                            <th scope="col">Email</th>
                            <th scope="col">Gender</th>
                            <th scope="col">DOB</th>
                            <th scope="col">City</th>
                            <th scope="col">Street</th>
                            <th scope="col">Pincode</th>
                            <th scope="col">Photo</th>
                            <th scope="col">Aadhar</th>
                            <th></th>

                          </tr>
                </div>
            </div>""")
for i in det:
    fn1 = "../images/" + i[9]
    fn2 = "../images/" + i[10]
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
                <td>%s</td>
                <td><img src="%s" alt="" height="100px" width="100px"></td>
                <td><img src="%s" alt=""height="100px" width="100px"></td>
                <td><button type="button" class="btn btn-success" data-bs-toggle="modal" data-bs-target="#myModal%s" style="margin: 20px;color:black;font-weight: bold;">
        Approve
    </button>
        </td>
            </form>
                </tr>""" % (i[0], i[1], i[2], i[3], i[4], i[5],i[6],i[7], i[8],fn1,fn2,i[0]))
    q = """SELECT * from userreg where id='%s'""" % i[0]
    cur.execute(q)
    x = cur.fetchone()
    if x[1] != None:
        n = x[1]
    else:
        n = 0
    a = n[0] + n[1]

    if x[3] != None:
        n = x[3]
    else:
        n = 0
    b = n[0] + n[1]
    Pass = a + b + "#not"
    Username = "x" + a + "@suuu"
    print("""
    <div class="modal fade" id="myModal%s" role="dialog">
        <div class="col-md-4"></div>
        <div class="modal-dialog col-md-5" style="margin-top: 180px;">
            <div class="modal-content">
                <div class="modal-header" style="background-color: skyblue; color: maroon; font-weight: 30px; text-align: center;">
                    <button type="button" class="close" data-dismiss="modal">&times;</button>
                    <h2 class="modal-title">Generate Password</h2>
                </div>
                <div class="modal-body">
                    <form method="post">          
                        <div class="container" style="text-align: center;"> 
                            <div class="card card-body">
                                <input type="hidden" class="form-control" name="sid" value='%s'>
                                <input type="hidden" class="form-control" name="email" value='%s'>
                                <input type="hidden" class="form-control" name="name" value='%s'>
                                <div class="form-group">
                                    <label for="username" style="font-weight: bolder; color: teal; font-size: 17px;">Username</label>
                                    <input type="text" class="form-control" name="username" style="width: 450px;" value='%s'>
                                </div> 
                                <div class="form-group">
                                    <label for="password" style="font-weight: bolder; color: teal; font-size: 17px;">Password</label>
                                    <input type="password" class="form-control" name="pwd" style="width: 450px;" value='%s'>
                                </div>
                                <div>
                                    <input type="submit" value="Send" name="sub" style="margin-left: 20px; margin-top:7px; background-color: green; padding: 10px; color: white; border-radius: 8px; box-shadow: 0 0 5px black;">
                                </div>
                            </div>
                        </div>
                    </form> 
                </div> 
            </div>
        </div>
    </div>
    """ % (i[0], i[0], i[3], i[1], Username, Pass))

Submit = y.getvalue("sub")
ID = y.getvalue("sid")
Username = y.getvalue("username")
Password = y.getvalue("pwd")
if Submit != None:
    q = """update userreg set Username="%s", Password="%s" ,Status="Approved" where id='%s' """ % (
        Username, Password, ID)
    cur.execute(q)
    con.commit()
    print("""<script>alert('Updated Successfully');</script>""")
Username = y.getvalue("username")
Password = y.getvalue("pwd")
Email = y.getvalue("email")
Name = y.getvalue("name")
if Submit != None:
    fromadd = "santhoshperumal678@gmail.com"
    passwords = "daxlwqlgqzxeqwpi"
    toadd = Email
    subject = "Regarding Username and Password"
    body = "Dear  {},\n\n Hereby I enclosed your verified username and password.\n\n Username: {} \n\n Password: {}".format(
        Name, Username, Password)
    msg = "Subject:{},\n\n {}".format(subject, body)
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()
    server.login(fromadd, passwords)
    server.sendmail(fromadd, toadd, msg)
    server.quit()
    print("""<script>alert('Mail sent Successfully');</script>
    """)

print("""
        </div>
      </section>
</body>
</html>     
        """)
con.commit()
con.close()

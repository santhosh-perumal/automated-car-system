#!C:/Users/Dhanush P/AppData/Local/Programs/Python/Python311/python.exe

print("content-type:text/html \r\n\r\n")
import cgi, cgitb, pymysql, smtplib

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="cars")
cur = con.cursor()
y = cgi.FieldStorage()
run=y.getvalue("id")
q = """select * from empdetails where Status='' """
cur.execute(q)
det = cur.fetchall()
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
    .table th{
background-color:rgb(13, 141, 98);
color:white;
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
      </nav> """)

print("""
      <section>
        <div class="container" style="margin-top:50px;">
            <div class="row">
                <div class="col-md-12">
                    <div class="py-3"><h4>Emp-details</h4></div>
                    <table class="table">
                        <thead>
                          <tr>
                            <th scope="col">id</th>
                            <th scope="col">name</th>
                            <th scope="col">contact</th>
                            <th scope="col">email</th>
                            <th scope="col">jobtype</th>
                            <th scope="col">street</th>
                            <th scope="col">city</th>
                            <th scope="col">pincode</th>
                            <th scope="col">experience</th>
                            <th scope="col">education</th>
                            <th scope="col">degreename</th>
                            <th scope="col">photo</th>
                            <th scope="col">id_proof</th>
                            <th> </th>
                          </tr>
                </div>
                </div>
            </div>""")
for i in det:
    fn1 = "../images/" + i[11]
    fn2 = "../images/" + i[12]
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
                <td>%s</td>
                <td>%s</td>
                <td><img src="%s" alt="" height="100px" width="100px"></td>
                <td><img src="%s" alt=""height="100px" width="100px"></td>
                <input type="hidden" name="id" value="%s">
                <td><input type="submit" class="btn btn-success" value="Remove" name="Remove" 
                 style="margin: 20px;color:black;font-weight: bold;">
        </td>
            </form>
                </tr>""" % (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7],i[8],i[9],i[10],fn1, fn2,i[0]))
    print("""
            </section>
            </body>
            </html>""")
s=y.getvalue("id")
remove = y.getvalue("Remove")
if remove != None:
    q1="""Update empdetails set Status="Removed" where id='%s'""" % (s)
    cur.execute(q1)
    con.commit()
    print("""
    <script>
    alert("Remove successfully");
    </script>
    """)
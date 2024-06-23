#!C:/Users/Dhanush P/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgi,cgitb,pymysql,os
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="cars")
cur=con.cursor()
form=cgi.FieldStorage()
y=form.getvalue("id")
q= """SELECT * from userreg where id = "%s" """ %y
cur.execute(q)
rec=cur.fetchall()
print("""
            <!DOCTYPE html>
    <html lang="en">
    <head>
       <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title> 
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" 
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" 
        integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
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
              <h5 class="offcanvas-title" id="offcanvasNavbarLabel">USER</h5>
              <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
            </div>
            <div class="offcanvas-body" style="background-color: rgb(51, 21, 21); color: white;">
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
      </nav>
          <section>""" % (y, y, y))
print("""
        <div class="container">
            <div class="row">""")
for i in rec:
    fn = "../images/" + i[9]
    print("""
              <div class="col-md-3 py-5" style="margin: 20px; margin-top:100px;">
                     <div class="card" style="width: 19rem;">
                         <img src="%s" class="card-img-top" alt="..." height="100px" width="100px">
                         <div class="card-body">
                             <p class="card-text">Details</p>
                             Name:%s <br>
                             Contact:%s <br>
                             Email:%s <br>
                             Gender:%s <br>
                             city:%s <br>
                         </div>
                     </div>
                 </div>"""% (fn, i[1], i[2], i[3],i[4],i[5]))

print("""
         </div>
         </div>
     </section>
     </body>
     </html>
          """ )







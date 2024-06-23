#!C:/Users/Dhanush P/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgi,cgitb,pymysql
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="cars")
cur=con.cursor()
form=cgi.FieldStorage()
x=form.getvalue("id")
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
.container-fluid{
background-color: rgb(59, 148, 148); 
height:100px;
}
.table th{
background-color:rgb(13, 141, 98);
color:white;
}


</style>
<body>
    <nav class="navbar fixed-top">
            <div class="container-fluid" style="background-color: rgb(139, 161, 161);">
                <button class="navbar-toggler" style="color:rgb(45,44,44); background-color:white; border:2px solid black;" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasNavbar" aria-controls="offcanvasNavbar" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon "></span>
                  </button>
               <img src="../media/wepik-gradient-professional-car-repair-company-logo-202404290727286CgX.png" alt="" style="width: 100px; height: 100px;">
               <div class="offcanvas offcanvas-start" tabindex="-1" id="offcanvasNavbar" aria-labelledby="offcanvasNavbarLabel" style="width: 300px;">
                <div class="offcanvas-header">
                  <h5 class="offcanvas-title" id="offcanvasNavbarLabel">SELLER</h5>
                  <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
                </div>
                <div class="offcanvas-body" style="background-color: rgb(13, 141, 98); color: white;">
                  <ul class="navbar-nav justify-content-start flex-grow-1 pe-3">
                         <li><a class="dropdown-item" href="seller_profile.py?id=%s" style="font-size: 20px;">PROFILE</a></li>
                            <li><a class="dropdown-item" href="reg_car.py?id=%s"  style="font-size: 20px; margin-top: 20px;">SELL CAR</a></li>
                  <li><a class="dropdown-item" href="booking_info.py?id=%s"  style="font-size: 20px; margin-top: 20px;">BUYER-INFO</a></li>
                  </ul>
                  <div class="bootom">
                    <a href="index.py">LOG OUT</a>
                  </div>
                </div>
              </div>
            </div>
          </nav><center>
      <h3 class="py-6" style="margin-top:120px; margin-left:30px;">WELCOME TO CARS PARADISE</h3>
      <h6 style="color:rgb(167, 107, 18);">sellers pannel</h6></center>
</body>
</html>""" % (x,x,x))


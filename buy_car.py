#!C:/Users/Dhanush P/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgi, cgitb, pymysql
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="cars")
cur = con.cursor()
form = cgi.FieldStorage()
y = form.getvalue("id")
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

</style>""")
print("""
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
                        <li><a class="dropdown-item" href="buy_car.py?id=%s"  style="font-size: 20px; margin-top: 20px;">CAR-DETAILS</a></li> 
                        <li><a class="dropdown-item" href="pay_advance.py?id=%s"  style="font-size: 20px; margin-top: 20px;">PAY ADVANCE</a></li>   
              </ul>
              <div class="bootom">
                <a href="index.py">LOG OUT</a>
              </div>
            </div>
          </div>
        </div>
      </nav>""" %(y,y,y))
q = """SELECT * FROM details where status='New'"""
cur.execute(q)
rec = cur.fetchall()
print("""<section>
     <div class="container">
         <div class="row">""")
for i in rec:
    fn = "../images/" + i[7]
    print("""
         <div class="col-md-3 py-5" style="margin-top:100px;">
             <div class="card" style="width: 17rem;">
                 <img src="%s" class="card-img-top" alt="...">
                 <div class="card-body">
                     <p class="card-text">Details</p>
                     seller_name:%s <br>
                     car_name:%s <br>
                     car_model:%s <br>
                     price:%s <br>
                      kilometers:%s <br>
                       contact:%s <br>
                       <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#myModal%s" style="margin: 20px;color:black;font-weight: bold;">
        Book Now
    </button>            
                 </div>
             </div>
         </div>
         """ % (fn,i[1], i[3], i[4], i[5],i[6],i[2],i[0]))

print("""<div class="modal fade" id="myModal%s" role="dialog">
        <div class="col-md-4"></div>
        <div class="modal-dialog col-md-5" style="margin-top: 180px;">
            <div class="modal-content">
                <div class="modal-header" style="background-color: skyblue; color: maroon; font-weight: 30px; text-align: center;">
                    <button type="button" class="close" data-bs-dismiss="modal">&times;</button>
                    <h2 class="modal-title">Generate Password</h2>
                </div>
                <div class="modal-body">
                    <form method="post">          
                        <div class="container" style="text-align: center;"> 
                         <div class="card card-body">
                            <label for="pincode" class="form-label">BUYER_NAME:</label>
                            <input type="text" class="form-control" id="pincode" name="buyer_name">
                             <label for="pincode" class="form-label">EMAIL_ID:</label>
                            <input type="text" class="form-control" id="pincode" name="email">
                                 <label for="pincode" class="form-label">PRICE:</label>
                            <input type="text" class="form-control" id="pincode" name="price" value="%s">
                                <div>
                                 <label for="pincode" class="form-label">CAR_NAME:</label>
                            <input type="text" class="form-control" id="pincode" name="car_name" value="%s">
                             <label for="pincode" class="form-label">CAR_MODEL:</label>
                            <input type="text" class="form-control" id="pincode" name="car_model" value="%s">
                            <label for="pincode" class="form-label">SELLER_NAME:</label>
                            <input type="text" class="form-control" id="pincode" name="seller_name" value="%s">
                                    <input type="submit" value="Submit" name="submit" style="margin-left: 40px; margin-top: 15px; background-color: green; padding: 10px; color: white; border-radius: 8px; box-shadow: 0 0 5px black;">
                                </div>
                            </div>
                        </div>
                </div> 
                 </form>
            </div>
        </div>
    </div>
    """ % (i[0],i[5],i[3],i[4],i[1]))

print("""
         </div>
     </div>
/ </section>
 </body>
 </html>""")

msubmit = form.getvalue("submit")
if msubmit:
    if len(form) != 0:
        mbuyer_name = form.getvalue("buyer_name")
        memail = form.getvalue("email")
        mprice = form.getvalue("price")
        mcar_name = form.getvalue("car_name")
        mcar_model = form.getvalue("car_model")
        mseller_name = form.getvalue("seller_name")
        status = 'new'
        y = """INSERT  INTO booking_details (buyer_name, email, price, car_name, car_model, seller_name, status) VALUES('%s','%s','%s','%s','%s','%s','%s')"""%(mbuyer_name, memail, mprice, mcar_name, mcar_model, mseller_name, status)
        cur.execute(y)
        con.commit()
        print("""
        <script>
        alert("Registered successfully")
        </script>
        """)

#!C:/Users/Dhanush P/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgi, cgitb, pymysql, smtplib
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="cars")
cur = con.cursor()
form = cgi.FieldStorage()
x = form.getvalue("id")
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
          </nav>"""%(x,x,x))
z = """select * from booking_details where status= "new" """
cur.execute(z)
det = cur.fetchall()
print("""
      <section>
        <div class="container py-5" >
            <div class="row">
                <div class="col-md-12"><center>
                    <div class="py-3"><h4>BUYER INFORMATION</h4></div></center>
                    <table class="table" >
                        <thead>
                          <tr>
                            <th scope="col">id</th>
                            <th scope="col">buyer_name</th>
                            <th scope="col">email</th>
                            <th scope="col">price</th>
                            <th scope="col">car_name</th>
                            <th scope="col">car_model</th>
                            <th scope="col">seller_name</th>
                            <th></th>
                          </tr>
                """)
for i in det:
    print("""
            <tr>
                <form method="post">                
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td><input type="button" class="btn btn-success" value="Approve" name="submit" data-bs-toggle="modal" data-bs-target="#myModal%s">
        </td></tr>"""%(i[0], i[1], i[2],i[3], i[4], i[5], i[6], i[0]))
    print("""
        
        <div class="modal" id="myModal%s" role="dialog">
        <div class="col-md-4"></div>
        <div class="modal-dialog col-md-5" style="margin-top: 180px;">
            <div class="modal-content">
                <div class="modal-header" style="background-color: skyblue; color: maroon; font-weight: 30px; text-align: center;">
                    <button type="button" class="close" data-dismiss="modal">&times;</button>
                    <h2 class="modal-title">Advance</h2>
                </div>
                <div class="modal-body">      
                        <div class="container" style="text-align: center;"> 
                            <div class="card card-body"> 
                                <div class="form-group">
                                
                                    <label for="advance" style="font-weight: bolder; color: teal; font-size: 17px;">ADVANCE</label>
                                    <input type="hidden"name="pid" value='%s'>
                                    <input type="hidden"name="email" value='%s'>
                                    <input type="text" class="form-control" name="advance" style="width: 450px;">
                                </div>
                                <div>
                                    <input type="submit" value="Send" name="sub2" style="margin-left:20px; margin-top:7px; background-color: green; padding: 10px; color: white; border-radius: 8px; box-shadow: 0 0 5px black;">
                                </div>
                            </div>
                        </div>
                    </form> 
                </div> 
            </div>
        </div>
    </div>
            """ % (i[0],i[0],i[2]))

submit = form.getvalue("sub2")
id = form.getvalue("pid")
mail = form.getvalue("email")
if submit!= None:
    advance = form.getvalue("advance")
    q = """ update booking_details set status="Approved", advance ='%s',adstatus='new' where id ='%s' """%(advance,id)
    cur.execute(q)
    con.commit()
    fromadd = "santhoshperumal678@gmail.com"
    passwords = "daxlwqlgqzxeqwpi"
    toadd = mail
    subject = "BOOKING STATUS"
    body = (f"Dear ,\n\n Hereby I enclosed your verified booking details.\n YOUR VECHICAL BOOKING IS SUCCESSFULLY APPROVED.\n you have to paid advance{advance}.")
    message = "Subject:{}, \n\n {}".format(subject, body)
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()
    server.login(fromadd, passwords)
    server.sendmail(fromadd, toadd,message)
    server.quit()
    print("""<script>alert('Updated and Mail sent Successfully');</script>
    """)

print("""
</div>
            </div>
        </div>
      </section>
</body>
</html>     
        """)



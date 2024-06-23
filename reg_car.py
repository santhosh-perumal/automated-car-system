#!C:/Users/Dhanush P/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import cgi, cgitb, pymysql, os
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="cars")
cur = con.cursor()
f = cgi.FieldStorage()
x = f.getvalue("id")

print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title> selling-Car details</title>
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
    <nav class="navbar bg-body-tertiary fixed-top">
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
          </nav>""" %(x,x,x))
print("""
    <center>
    <section class="py-5" style="margin-top:100px; background-image:url(../media/card-7.jpg);">
        <div class="form container mt-3" style="backdrop-filter: blur(2px);">
            <div class="row">
            <div class="col-md-12">
                <form method="post" enctype="multipart/form-data">

                    <h4 class="" style="color:black;">CAR DETAILS</h4>
                   <div class="mb-3" style="width: 500px; color:black;">
                      <label for="exampleInputEmail1" class="form-label"> Seller_Name:</label>
                      <input type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp"  name="seller_name">
                      </div>
                      <div class="mb-3" style="width: 500px; color:black;">
                        <label for="exampleInputEmail1" class="form-label">Contact:</label>
                        <input type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp"  name="contact">
                        </div>
                    <div class="mb-3" style="width: 500px; color:black;;">
                      <label for="" class="form-label" >Car Name:</label>
                      <input type="text" class="form-control" id="exampleInputPassword1" name="car_name">
                    </div>
                   <div class="" style="width: 500px; color:black;">
                    <label for="" class="form-label">Car Model:</label>
                      <input type="text" class="form-control" id="exampleInputPassword1"  name="car_model">
                    </div> <br>
                    <div class="" style="width: 500px; color:black;">
                        <label for="" class="form-label" >Price:</label>
                          <input type="text" class="form-control" id="exampleInputPassword1"  name="price">
                        </div> <br>
                        <div class="" style="width: 500px;color:black;">
                            <label for="" class="form-label">Kilometers:</label>
                              <input type="text" class="form-control" id="exampleInputPassword1"  name="kilometers">
                            </div> <br>
                            <div class="" style="width: 500px; color:black;">
                              <label for="" class="form-label">Car_photo:</label>  
                                <input type="file" class="form-control" id="exampleInputPassword1" name="car_photo">
                              </div> <br>
                              <div class="" style="width: 500px; color:black;">
                                <label for="" class="form-label" >Car_Documents:</label>
                                  <input type="file" class="form-control" id="exampleInputPassword1" name="car_documents">
                                </div> <br>
                  <input type="submit" class=" submit btn btn-primary mb-4 value="submit"
                   name="submit">
                  </form>
            </div>
            </div>
        </div>
    </section>
    </center>
</body>""")

q= """SELECT * from sellerreg where id = "%s" """ %x
cur.execute(q)
rec=cur.fetchall()

msubmit = f.getvalue("submit")

if msubmit != None:
    if len(f) != 0:
        mseller_name = f.getvalue("seller_name")
        mcontact = f.getvalue("contact")
        mcar_name = f.getvalue("car_name")
        mcar_model = f.getvalue("car_model")
        mprice = f.getvalue("price")
        mkilometers = f.getvalue("kilometers")
        mcar_photo = f['car_photo']
        mcar_documents = f['car_documents']
        status = "new"
        if mcar_photo.filename:
            fn = os.path.basename(mcar_photo.filename)
            open("../images/" + fn, "wb").write(mcar_photo.file.read())
            fn2 = os.path.basename(mcar_documents.filename)
            open("../images/" + fn2, "wb").write(mcar_documents.file.read())

            q = """INSERT INTO details (seller_name,contact,car_name,car_model,price,kilometers,car_photo,car_documents, 
            status)VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % (mseller_name,mcontact,mcar_name,
                                                                                      mcar_model,mprice,mkilometers,fn,fn2,status)
            cur.execute(q)
            con.commit()
            print("""
                                <script>
                                alert("Register successfully")
                                </script>
                            """)



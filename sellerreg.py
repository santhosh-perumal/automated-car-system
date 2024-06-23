#!C:/Users/Dhanush P/AppData/Local/Programs/Python/Python311/python.exe

print("content-type:text/html \r\n\r\n")
print(
    """ <!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <title> Seller Registration</title>
   <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" 
   integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
   <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" 
   integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
  <link rel="stylesheet" href="/car/css/smart.css">
</head>
<body class="body">
   <section id="user" style="">
   <div class="form container">
       <div class="row">
       <div class="col-md-12">
           <form method="post" enctype="multipart/form-data">
               <center>
               <h4 class="" style="color: black;"> SELLER REGISTER</h4></center>
               <div class="mb-3" style="width: 300px;">
                 <label for="exampleInputEmail1" class="form-label">Name:</label>
                 <input type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" name="Name">
                 </div>
                 <div class="mb-3" style="width: 300px;">
                   <label for="exampleInputEmail1" class="form-label">Contact:</label>
                   <input type="number" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" name="Contact">
                   </div>
               <div class="mb-3" style="width: 300px;">
                 <label for="" class="form-label">Email:</label>
                 <input type="email" class="form-control" id="exampleInputPassword1" name="Email">
               </div>
               <div class="radio" >
                   <label for="">Gender:</label>
                   <input type="radio" name="Gender" id="male" value="male"  required>
                   <label for="male">Male</label>
                   <input type="radio" name="Gender" id="female" value="female" required>
                   <label for="female">Female</label>

               </div> <br>
            
              <div class="city" style="width: 300px;">
               <label for="" class="form-label">City:</label>
                 <input type="text" class="form-control" id="exampleInputPassword1" name="City">
               </div> <br>
               <div class="street" style="width: 300px;">
                   <label for="" class="form-label">Street:</label>
                     <input type="text" class="form-control" id="exampleInputPassword1" name="Street">
                   </div> <br>
                   <div class="pincode" style="width: 300px;">
                       <label for="" class="form-label">Pincode:</label>
                         <input type="text" class="form-control" id="exampleInputPassword1" name="Pincode">
                       </div> <br>
                       <div class="pincode" style="width: 300px;">
                         <label for="" class="form-label">photo:</label>
                           <input type="file" class="form-control" id="exampleInputPassword1" name="Photo">
                         </div> <br>
                         <div class="pincode" style="width: 300px;">
                           <label for="" class="form-label">Aadhar:</label>
                             <input type="file" class="form-control" id="exampleInputPassword1" name="Aadhar">
                           </div> <br>
                          <center>
                                    <input type="submit" class="btn btn-primary" type="submit" name="submit">
                                    </center>
             </form>
       </div>
       </div>
   </div>
</section>
</body>
</html>
"""
)
import cgi
import cgitb
import pymysql
import os

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="cars")
cur = con.cursor()

form = cgi.FieldStorage()
psubmit = form.getvalue("submit")

if psubmit:
    if len(form) != 0:
        pName = form.getvalue("Name")
        pContact = form.getvalue("Contact")
        pEmail = form.getvalue("Email")
        pGender = form.getvalue("Gender")
        pCity = form.getvalue("City")
        pStreet = form.getvalue("Street")
        pPincode = form.getvalue("Pincode")
        pPhoto = form['Photo']
        pAadhar = form['Aadhar']
        Status = "New"


        if pPhoto.filename:
            fn = os.path.basename(pPhoto.filename)
            open("../images/" + fn, "wb").write(pPhoto.file.read())
            fn2 = os.path.basename(pAadhar.filename)
            open("../images/" + fn2, "wb").write(pAadhar.file.read())

            q = """INSERT INTO sellerreg (Name, Contact, Email, Gender,City, Street, Pincode, Photo, Aadhar, Status)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            cur.execute(q,(pName, pContact, pEmail, pGender,pCity, pStreet, pPincode, fn, fn2, Status))
            con.commit()
            print("""
                    <script>
                    alert("Register successfully")
                    location.href=("index.py")
                    </script>
                """)
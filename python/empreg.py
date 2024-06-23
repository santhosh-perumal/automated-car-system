#!C:/Users/Dhanush P/AppData/Local/Programs/Python/Python311/python.exe

print("content-type:text/html \r\n\r\n")
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>salesexe</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" 
    integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" 
    integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
</head>
<style>
.empreg{
    color: white;
    backdrop-filter: blur(2px);
}
.bgimg{
    background-image: url(/car/media/card-5.jpg);
    background-repeat: no-repeat;
    background-size: cover;
}
</style>
<body class="bgimg">
    <section class="py-3">
        <div class="empreg container py-3" style="width: 350px;">
            <div class="row">
                <div class="col-md-12">
                    <center>
                        <h4>EMPLOYEE REGISTER</h4>
                    </center>
                    <br>
                    <form method="post" enctype="multipart/form-data">
                        <div class="mb-3">
                            <label for="name" class="form-label">Name:</label>
                            <input type="text" class="form-control" id="name" name="name"> 
                        </div>
                        <div class="mb-3">
                            <label for="contact" class="form-label">Contact:</label>
                            <input type="text" class="form-control" id="contact" name="contact">
                        </div>
                        <div class="mb-3">
                            <label for="email" class="form-label">Email:</label>
                            <input type="email" class="form-control" id="email" name="email">
                        </div>
                        <div class="mb-3">
                            <label for="jobtype" class="form-label">Job Type:</label>
                            <select name="jobtype" class="form-select" style="width: 325px; height: 40px; border-radius: 8px;">
                                <option value="Sales Executive">Sales Executive</option>
                                <option value="Mechanic">Mechanic</option>
                            </select>
                        </div>
                        <center>
                            <h5>Address</h5>
                        </center>
                        <div class="mb-3">
                            <label for="street" class="form-label">Street:</label>
                            <input type="text" class="form-control" id="street" name="street">
                        </div>
                        <div class="mb-3">
                            <label for="city" class="form-label">City:</label>
                            <input type="text" class="form-control" id="city" name="city">
                        </div>
                        <div class="mb-3">
                            <label for="state" class="form-label">State:</label>
                            <input type="text" class="form-control" id="state" name="state">
                        </div>
                        <div class="mb-3">
                            <label for="pincode" class="form-label">Pincode:</label>
                            <input type="text" class="form-control" id="pincode" name="pincode">
                        </div>
                        <center>
                            <h5>Education</h5>
                        </center>
                        <div class="mb-3">
                            <label for="experience" class="form-label">Experience:</label>
                            <select name="experience" class="form-select" style="width:325px; height: 40px; border-radius: 8px;">
                                <option value="fresher">Fresher</option>
                                <option value="0-2">0-2 Y</option>
                                <option value="3-5">3-5 Y</option>
                                <option value="5-10">5-10 Y</option>
                            </select>
                        </div>
                        <div class="mb-3">
                            <label for="education" class="form-label">Education:</label>
                            <select name="education" class="form-select" style="width:325px; height: 40px; border-radius: 8px;">
                                <option value="ug">UG</option>
                                <option value="pg">PG</option>
                                <option value="diploma">Diploma</option>
                            </select>
                        </div>
                        <div class="mb-3">
                            <label for="degree" class="form-label">Degree Name:</label>
                            <input type="text" class="form-control" id="degree" name="degreename">
                        </div>
                        <center>
                            <h5>Id-Proof</h5>
                        </center>
                        <div class="mb-3">
                            <label for="photo" class="form-label">Photo:</label>
                            <input type="file" class="form-control" id="photo" name="photo">
                        </div>
                        <div class="mb-3">
                            <label for="id_proof" class="form-label">Idproof:</label>
                            <input type="file" class="form-control" id="id_proof" name="id_proof">
                        </div>
                        <center>
                            <input type="submit" class="btn btn-primary" name="submit" value="Submit">
                        </center>
                    </form>
                </div>
            </div>
        </div>
    </section>
</body>
</html>
""")


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
    pName = form.getvalue("name")
    pContact = form.getvalue("contact")
    pEmail = form.getvalue("email")
    pJobType = form.getvalue("jobtype")
    pStreet = form.getvalue("street")
    pCity = form.getvalue("city")
    pPincode = form.getvalue("pincode")
    pExperience = form.getvalue("experience")
    pEducation = form.getvalue("education")
    pDegreename = form.getvalue("degreename")
    pPhoto = form['photo']
    pIdproof = form['id_proof']
    if pPhoto.filename:
        fn = os.path.basename(pPhoto.filename)
        open("../images/" + fn, "wb").write(pPhoto.file.read())
        fn2 = os.path.basename(pIdproof.filename)
        open("../images/" + fn2, "wb").write(pIdproof.file.read())

        q = """INSERT INTO empdetails (name, contact, email, jobtype, street, city, pincode, experience, education, degreename, photo, id_proof,Status)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s ,%s,%s)"""
        cur.execute(q, (
        pName, pContact, pEmail, pJobType, pStreet, pCity, pPincode, pExperience, pEducation, pDegreename, fn, fn2))
        con.commit()

        try:
            cur.execute(q, (
            pName, pContact, pEmail, pJobType, pStreet, pCity, pPincode, pExperience, pEducation, pDegreename, fn, fn2))
            con.commit()
            print("""
                    <script>
                    alert("Register successfully")
                    </script>
                """)
        except Exception as e:
            print("Error:", e)

#!C:/Users/VISHNAVEE/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.4/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
</head>""")
import cgi,cgitb,pymysql,smtplib

cgitb.enable()
con=pymysql.connect(host="localhost",user="root",password="",database="test")
cur=con.cursor()
x = cgi.FieldStorage()
print("""
<table border="2px">
<tr>
<th>S.No</th>
<th>Name</th>
<th>Email Id</th>
<th></th>
</tr>
""")
s="""select * from reg where Status="New" """
cur.execute(s)
rec=cur.fetchall()
for i in rec:
    print("""
    <tr>
    <td>%s</td>
    <td>%s</td>
    <td>%s</td>
     <td><button type="button" class="btn btn-success" data-toggle="modal" data-target="#myModal%s" style="margin: 20px;color:black;font-weight: bold;">
    Approve</button>
    <input type="submit" name="reject" value="Reject" class="btn btn-danger" style="margin: 20px;color:black;font-weight: bold;"></td>
    </tr>
    """ %(i[0],i[1],i[2],i[0]))
    print("""
    <div class="modal fade" id="myModal%s" role="dialog">
    <div class="col-md-4"></div>
            <div class="modal-dialog col-md-5" style="margin-top: 180px;">
                <div class="modal-content">
                    <div class="modal-header" style="background-color: skyblue;color: maroon;font-weight:30px;text-align: center;">
                        <button type="button" class="close" data-dismiss="modal">&times;</button>
                        <h2 class="modal-title">Generate Password</h2>
                    </div>
                    <div class="modal-body">
                        <form method="post">          
                        <div class="container style="text-align: center;"  > 
                            <div class="card card-body">
                                <input type="hidden" class="form-control" name="id" value='%s'>
                                <input type="hidden" class="form-control" name="email" value='%s'>
                                <input type="hidden" class="form-control" name="name" value='%s'>
                                <div class="form-group">
                                <label for="username" style="font-weight: bolder;color: teal;font-size: 17px;">Username</label>
                                <input type="text"class="form-control" name="username"  style="width: 450px;">
                                </div> 
                                <div class="form-group">
                                <label for="password" style="font-weight: bolder;color: teal;font-size: 17px;">Password</label>
                                <input type="password" class="form-control" name="pwd"   style="width: 450px;">
                                </div> 
                                <div>
                                    <input type="submit" value="Send" name="sub" style="margin-left:200px;background-color: green;
                                    padding: 10px;color: white;border-radius: 8px;box-shadow: 0 0 5px black;">
                                </div>
                            </div>
                        </div>
                     </form> 
                    </div> 
                </div>
            </div>
    </div>""" % (i[0], i[0], i[1],i[2]))
Submit = x.getvalue("sub")
Id = x.getvalue("id")
Username = x.getvalue("username")
Password = x.getvalue("pwd")
if Submit != None:
    q3 = """update reg set Username="%s", Password="%s" ,Status="Approved" where Id='%s' """ % (Username, Password, Id)
    cur.execute(q3)
    con.commit()
    print("<script>alert('Updated Successfully');</script>")
Username = x.getvalue("username")
Password = x.getvalue("pwd")
Email = x.getvalue("email")
Name = x.getvalue("name")
if Submit != None:
    fromadd = "your email"
    passwords = "your password"
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
con.close()
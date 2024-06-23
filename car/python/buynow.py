#!C:/Users/Dhanush P/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import cgi, cgitb, pymysql,smtplib
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="cars")
cur = con.cursor()
form = cgi.FieldStorage()
y = form.getvalue("id")
q1="""select Name from userreg where id=%s"""%y
cur.execute(q1)
name=cur.fetchone()
pro=name[0]
print("""<!DOCTYPE html>
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
    .bootom a{
      text-decoration: none;
      font-size: 18px;
        font-weight: 500;
        display: flex;
        justify-content: center;
        margin-top: 100px;
    }
    /* Payments card */
.pay b u
{
  font-size: 20px;
}
.credit-card{
  padding-top: 30px;
}
.cred-card{
  border: 1px solid black;
 padding-right: 20px;
 margin-top:10px;
 margin-left: 12px;
}
.payments{
  margin-top: 100px;
}
.payments{
  display: none;
}
       
</style>
<script>
function calculateAmount(val){
    var Prizeval = document.getElementById("Prize");
    // replace that dolar symbol
    var Prize = parseFloat(Prizeval.value.replace('$', '')); 
    var tot_price = val * Prize;
    console.log("Total Price: " + tot_price);
    // Display the total
    var hello = document.getElementById("Total");
    hello.value = tot_price;
}
  function kalai() {
  var payments = document.querySelector(".payments");
  payments.style.display = "block";
}
</script>
<body>
     <nav class="navbar bg-body-tertiary fixed-top">
        <div class="container-fluid">
            <button class="navbar-toggler" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasNavbar" aria-controls="offcanvasNavbar" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon "></span>
              </button>
          <a class="navbar-brand" href="#">SMART</a>
           <div class="offcanvas offcanvas-start" tabindex="-1" id="offcanvasNavbar" aria-labelledby="offcanvasNavbarLabel" style="width: 300px;">
            <div class="offcanvas-header">
              <h5 class="offcanvas-title" id="offcanvasNavbarLabel">SELLER</h5>
              <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
            </div>
            <div class="offcanvas-body">
              <ul class="navbar-nav justify-content-start flex-grow-1 pe-3">
                     <li><a class="dropdown-item" href="user_profile.py" style="font-size: 20px;">MY PROFILE</a></li>
                        <li><a class="dropdown-item" href="cars.py"  style="font-size: 20px; margin-top: 20px;">CAR-DETAILS</a></li>
                        
              </ul>
              <div class="bootom">
                <a href="index.py">LOG OUT</a>
              </div>
            </div>
          </div>
        </div>
      </nav>
        </section>""")
x = """SELECT * from booking_details where buyer_name="%s" and adstatus!="paid" """ %pro
cur.execute(x)
rec = cur.fetchall()

print("""
            <section class="BuyNow-card">
                <div class="container mt-5">
                    <div class="row">
                    """)
for i in rec:
    print("""
                
        <div class="prof col-md-6 py-5">
            <form method="post" style="border: 1px solid; width: fit-content;" class="form">
                <input type="hidden" name="email" value="%s">
                <input type="hidden" name="bid" value="%s">
                
                <h3 class="card-title">Details</h3>
                <label for="buyer_name">Buyer Name:</label>
                <input type="text" name="buyer_name" id="buyer_name" value="%s" style="width:fit-content;"><br><br>
                <label for="car_name">Car Name:</label>
                <input type="text" name="car_name" id="car_name" value="%s" style="width:fit-content;"><br><br>
                <label for="car_model">Car Model:</label>
                <input type="text" name="car_model" id="car_model" value="%s" style="width:fit-content;"><br><br>
                <label for="Prize" class="Prize">Advance:</label>
                <input type="text" name="Prize" id="Prize" value="%s" readonly style="width:fit-content;"><br><br>
                <label for="Payment_Method" class="Pay-method">Payment Method:</label>
                <select name="Payment_Method" id="Payment_Method" onchange="kalai()">
                    <option value="Cash On Delivery">Cash On Delivery</option>
                    <option value="Card">Card</option>
                </select><br><br>
                <label for="mobno">Mobile Number:</label>
                <input type="text" name="mobno" id="mobno" placeholder="Confirmation Number" class="num"><br><br>
                <center><input type="submit" value="buynow" name="sub" style="border-radius: 5px;"></center>
            </form>
        </div>                               
                            </div>
                             <div class="payments col-lg-6 py-5">
                                    <!-- Payment information -->
                                    <div class="card" style="width:25rem;">
                          <div class="pay card-body">
                            <center>
                              <img src="/Garments/admin/pay.png" alt=""><br><br>
                            <i class="fa-solid fa-lock"></i> <b><u>Secure Payment</u></b> 
                          </center>

                            <div class="credit-card">
                            <h5 class="card-title">Credit Card</h5>
                          <label for=""><b>Credit Card Number*</b></label><br>
                          <input type="text" name="card_Num" class="cred-card" placeholder="XXXX XXXX XXXX XXXX"><br> <br>

                          <label for=""><b>Name of Card Holder*</b></label>
                          <input type="text" name="card_Holder" class="cred-card"><br><br><br>

                          <label for=""><b>Expiration Date*</b></label><br>
                          <input type="date" name="expDate" class="cred-card"><br><br>

                          <label for=""><b>Security Code*</b></label><br>
                          <input type="text" name="Security" class="cred-card">
                           <center>
                            <input type="submit" name="confirm" value="Confirm" class="BuyNow mt-5">
                           </center>
                          </div>    
                          </div>
                      
                            </div>
                          </form>
                   
        """ %(i[2],i[0],i[1],i[4],i[5],i[8]))
    print("""
             </div>
                </div>
            </section>
        </body>
        </html> """)

submit = form.getvalue("sub")
mail = form.getvalue("email")
bid = form.getvalue("bid")
advance = form.getvalue("advance")
if submit!= None:
    q = """ update booking_details set adstatus='paid' where id ='%s' """%bid
    cur.execute(q)
    con.commit()


    fromadd = "santhoshperumal678@gmail.com"
    passwords = "daxl wqlg qzxe qwpi"
    toadd = mail
    subject = "PAYMENT STATUS"
    body = (f"Dear ,\n\n Hereby I enclosed your verified payment details.\n YOUR VECHICAL BOOKING IS SUCCESSFULLY APPROVED.\n you are successfully paid your advance amount.\n your test driving is avilable now and you may visit our store in a couple of days \n THANK YOU  ")
    message = "Subject:{}, \n\n {}".format(subject, body)
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()
    server.login(fromadd, passwords)
    server.sendmail(fromadd, toadd, message)
    server.quit()
    print("""<script>alert('Updated and Mail sent Successfully');</script>
    """)




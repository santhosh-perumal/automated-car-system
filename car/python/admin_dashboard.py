#!C:/Users/Dhanush P/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
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
      </nav>
       <div class="container">
  <div class="row">
    <div class="col-md-12">
    <center>
    <h3 style="margin-top: 130px; color:red">WELCOME TO CARS PARADISE</h3>
    <p>ADMIN PANNEL</p>
      </center>
  </div>
  </div>
</div>
      </section>
</body>
</html>""")
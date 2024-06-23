#!C:/Users/Dhanush P/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    
    <title>smart car-e</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/car/css/smart.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
</head>
<body>
  <!-- nav-bar  -->
 <nav class="navbar navbar-expand-lg  py-3 text-uppercase  sticky-top" style="background-color:white ; height:80px ;">
    <div class=" change container-fluid">
      <img src="/car/media/wepik-gradient-professional-car-repair-company-logo-202404290727286CgX.png" alt="" style="width: 100px; height: 100px;">
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent ">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0 gap-4 ">
          <li class=" nav1 nav-item">
            <a class="nav-link active" aria-current="page" href="/html/homepage.html">HOME</a>
          </li>
          <li class=" nav2 nav-item" style="color: white;">
            <a class="nav-link active" href="/html/cars.html">CARS</a>
          </li>
         </ul>
       <!-- Example split danger button -->
       <div class="reg container">
<div class="btn-group"> 
  <button type="button" class="abc btn btn-danger">REGISTER</button>
  <button type="button" class="btn btn-danger dropdown-toggle dropdown-toggle-split" data-bs-toggle="dropdown" aria-expanded="false">
    <span class="visually-hidden">Toggle Dropdown</span>
  </button>
  <ul class="dropdown-menu w-75">
    <li><a class="dropdown-item" href="userreg.py" >USER</a></li>
    <li><a class="dropdown-item" href="sellerreg.py" >SELLER</a></li>

      </ul>
            
</div>
<div class="btn-group ">
  <button type="button" class=" login btn btn-danger">LOG IN</button>
  <button type="button" class="btn btn-danger dropdown-toggle dropdown-toggle-split" data-bs-toggle="dropdown" aria-expanded="false">
    <span class="visually-hidden">Toggle Dropdown</span>
  </button>
  <ul class="dropdown-menu w-75">
    <li><a class="dropdown-item" href="user_login.py">USER</a></li>
    <li><a class="dropdown-item" href="admin_login.py">ADMIN</a></li>
    <li><a class="dropdown-item" href="#">SALES EXECUTIVE</a></li>
    <li><a class="dropdown-item" href="seller_login.py">SELLER</a></li>
  </ul>
</div>

</div>
    </div>
  </nav>
  <!-- carousel of banners -->

 <!-- text and some carousel of images -->
 <section id="about" class="py-5">
  <div class="container">
      <div class="row align-items-center">
          <div class="col-md-6">
              <h1 class="pb-3">Find The Simplest Way <br>To Drive Revoluation <br>With Terra Auto</h1>
              <p class="pb-3">

                  As a recent graduate eager to embark on my professional journey,
                   I am seeking opportunities to apply my skills and knowledge in [software industries]. 
                   With a passion for [software developer],
                   I am dedicated to contributing positively to any team I join while continuously learning and growing.</p>
                   
          </div>
          <!-- carousel of cars -->
          <div class=" image col-md-6 text-center">
            <div id="carouselExampleIndicators" class="carousel slide" data-interval="2000">
              <div class="carousel-indicators">
                <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
                <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
                <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
              </div>
              <div class="carousel-inner">
                <div class="carousel-item active">
                  <img src="/car/media/card-2.jpg" class="d-block w-100" alt="...">
                </div>
                <div class="carousel-item">
                  <img src="/car/media/card-3.jpg" class="d-block w-100" alt="...">
                </div>
                <div class="mustang2 carousel-item">
                  <img src="/car/media/card-6.jpg" class="d-block w-100" alt="...">
                </div>
              </div>
              <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
              </button>
              <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
              </button>
            </div>
          </div>
          
      </div>
      <button class=" ride btn  m-0 btn-outline-success" type="submit" >Book Your Ride</button>
        <button class=" selling btn btn-outline-success text-uppercase text-succcess" type="submit ">Sell Your Car</button>
  </div>
</section>
<!-- about -->
<section>
  <div class="container">
    <div class="row">
      <div class="col-md-12">
        <div class="about">
          <hr style="width:50%;margin-left:30%;">
            <h1 class="text-center mb-10px">ABOUT US</h1>
        </div>
      </div>
    </div>
  </div>
</section>
<!-- overview of about us -->
<section>
  <div class="container-fluid">
    <div class="row">
      <div class="col-md-12">
        <div id="carouselExampleCaptions" class="carousel slide">
          <div class="carousel-indicators">
            <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
            <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1" aria-label="Slide 2"></button>
            <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2" aria-label="Slide 3"></button>
          </div>
          <div class="carousel-inner">
            <div class="carousel-item active">
              <img src="/car/media/suuuuu.jpg" class="d-block w-100" alt="...">
              <div class="carousel-caption d-none d-md-block">
                <h1></h1>
                <h5>BOOK YOUR RIDE</h5>
                <p class="boo text-uppercase" style="color: rgba(238, 234, 8, 0.877);">we garuntee for your safe ride and give your support.</p>
                <button type="button" class=" booking btn btn-dark">book now</button>
              </div>
            </div>
            <div class="carousel-item">
              <img src="/car/media/suuuuu1.jpg" class="d-block w-100" alt="..." style="height: 880px;">
              <div class="carousel-caption d-none d-md-block">
                <h5>BOOK YOUR RIDE</h5>
                <p class="boo text-uppercase" style="color: rgba(238, 234, 8, 0.877);">we garuntee for your safe ride and give your support.</p>
                <button type="button" class=" booking btn btn-dark">book now</button>  
              </div>
            </div>
            <div class="carousel-item">
              <img src="/car/media/suuuu2.jpg" class="d-block w-100" alt="..." style="height: 880px;">
              <div class="carousel-caption d-none d-md-block">
                <h5>BOOK YOUR RIDE</h5>
                <p class="boo text-uppercase" style="color: rgba(238, 234, 8, 0.877);">we garuntee for your safe ride and give your support.</p>
                <button type="button" class=" booking btn btn-dark">book now</button>    
              </div>
            </div>
          </div>
          
        </div>
      </div>
    </div>
  </div>
</section>
<!-- missions of ours -->
<section class="bg-light">
  <div class="container">
    <div class="col-md-12">
      <h1 class="missions text-center text-uppercase mt-4">missions</h1>
    </div>
    <di class="row">
      <div class="col-md-4">
        <div class="card mb-3 w-80 mt-5 ml-5">
          <img src="/car/media/car-8.jpg" class="card-img-top w-75 " alt="...">
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
            <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
          </div>
        </div>
         </div>
         <div class="col-md-4">
          <div class="card mb-3 w-80 mt-5 ml-5">
            <img src="/car/media/card-3.jpg" class="card-img-top w-100 " alt="...">
            <div class="card-body">
              <h5 class="card-title">Card title</h5>
              <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
              <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
            </div>
          </div>
        </div>
        <div class="col-md-4">
          <div class="card mb-3 w-80 mt-5 ml-5">
            <img src="/car/media/card-7.jpg" class="card-img-top w-100" alt="...">
            <div class="card-body">
              <h5 class="card-title">Card title</h5>
              <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
              <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p> 
            </div>
          </div>
        </div>
        
    </div>
  </div>
  <hr class="hr" style="width:50%;margin-left:300px;">
</section>
<section>
  <div class="container">
    <div class="row">
      <div class="col-md-6">
        <p>
          <h3>WIDE SELECTION:</h3> With a vast inventory of vehicles from trusted sellers, you'll find the perfect car to suit your needs and budget. <br> <br>
<H3>Transparent Pricing:</H3> Say goodbye to hidden fees and surprises. We believe in transparent pricing, so you can shop with confidence. <br> <br>
<h3>Easy Selling Process:</h3> Selling your car has never been easier. Our streamlined process takes the stress out of selling, allowing you to get top dollar for your vehicle in no time.<br> <br> 
<h3>Expert Support:</h3> Our team of automotive experts is here to assist you every step of the way. Whether you have questions about a listing or need guidance on selling your car, we're always here to help.</b>
        </p>

      </div>
      <div class="col-md-6">
        
        <div class="image">
          <img src="/car/media/taxi-driver-female-client-interacting-formal-way.jpg" class="w-100 py-5 p-6 mt-5" alt="" >
        </div>
      
      </div>
    </div>
  </div>
</section>
<section class="contact">
  <div class="container">
    <div class="row">
      <div class="col-md-12">
        <div class="content">
          <!-- Your content goes here -->
          <h1 class="text-uppercase" style="font-size: 50px; color: black;">Contact Us</h1>
          <p>This is the contact section. You can add your contact information here.</p>
        </div>
      </div>
    </div>
  </div>
</section>
<section class="py-3 bg-light">
  <div class="container">
    <div class="row">
      <div class="col-md-4">
        <div class="card" style="width: 17rem;margin-top: 10px; height:20rem;">
          <img src="/car/media/map.png" class="card-img-top w-75" alt="...">
          <div class="card-body">
            <h4>Address Line</h4>
            <p class="card-text">123,kavundampalayam,coimbatore.</p>
          </div>
        </div>
      </div>
      <div class="col-md-4">
        <div class="card" style="width: 16rem;margin-top: 10px; height:20rem;">
          <img src="/car/media/customer-service.png" class="card-img-top w-75" alt="...">
          <div class="card-body">
            <h4>customer-service</h4>
            <p class="card-text">123,kavundampalayam,coimbatore.</p>
          </div>
        </div>
      </div>
      <div class="col-md-4">
        <div class="card" style="width: 16rem;margin-top: 10px; height:20rem;">
          <img src="/car/media/24-hours-delivery.png" class="card-img-top w-75" alt="...">
          <div class="card-body">
            <h4>Opening Time</h4>
            <p class="card-text">123,kavundampalayam,coimbatore.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
<section class="bg-dark">
  <footer>
  <div class="container py-5">
    <div class="row">
      <div class="col-md-3">
        <div class="footer">
          <h4 class="" style="color: white;">Get in touch</h4>
          <form>
            <div class="mb-3">
              <label for="exampleInputEmail1" class="form-label" style="color: white;">Email address:</label>
              <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="@gmail.com">
              <div id="emailHelp" class="form-text" style="color: white;">We'll never share your email with anyone else.</div>
            </div>
            <div class="mb-3">
              <label for="exampleInputPassword1" class="form-label"style="color: white;">comments:</label>
              <textarea name="" id="" cols="30" rows="5"></textarea>
             </div>
            <button type="submit" class="btn btn-primary">submit</button>
          </form>
        </div>
      </div>
      <div class="col-md-3">
        <div class="cars" style="margin-left:100px;">
        <h4 class=""style="color: white;">cars</h4>
        <a href="#">•maruti</a> <br>
        <a href="#">•Audi</a> <br>
        <a href="#">•Hyundai</a><br>
        <a href="#">•Mahindra</a><br>
        <a href="#">•Honda</a><br>
        <a href="#">•Skoda</a><br>
        <a href="#">•Volkswagen</a> <br>
        <a href="#">•Renault</a> <br>
        <a href="#">•Toyoto</a> <br>
        <a href="#">•Nissan</a> <br>
        <a href="#">•MG Motor</a> <br>
        
      </div>
      </div>
      <div class="col-md-3">
        <div class="help" style="margin-left:100px;">
        <h4 class="" style="color: white;">Help</h4>
        <a href="#">•FAQ</a> <br>
        <a href="#">•Terms & Conditions</a> <br>
        <a href="#">•Reporting</a><br>
        <a href="#">•Documentation</a><br>
        <a href="#">•Support & Policy</a><br>
        <a href="#">•Privacy</a><br> 
      </div>
      </div>
      <div class="col-md-3">
        <div class="media" style="margin-left:100px;">
        <h4 class="" style="color: white;">Social Media</h4>
        <i class="fa-brands fa-square-x-twitter" style="color: rgb(169, 200, 209);"></i> <a href="#">Twitter-x</a> <br>
        <i class="fa-brands fa-square-instagram" style="color: #d42692;"></i>  <a href="#">Instagram</a><br>
        <i class="fa-brands fa-youtube" style="color: #c93232;"></i>  <a href="#">Youtube</a><br>
        <i class="fa-brands fa-square-whatsapp" style="color: #40ca4c;"></i> <a href="#">Whatsapp</a>
      </div>
    </div>
  </div>
</footer>
</section>
</body>
</html>
    """)
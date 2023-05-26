<div class="row">
  <div class="col-xl-6 col-sm-6 mb-3">
    <div class="card text-white bg-dark o-hidden h-100">
      <div class="card-body">
        <div class="card-body-icon">
          <i class="fas fa-fw fa-eye"></i>
        </div>
        <div class="mr-5 text-success text-center">
          <?php
		  	include("inc/config.php");
			$query1 = "SELECT COUNT(id) FROM bots";
			$result1 = mysqli_query($conn, $query1) or die("Ошибка1 " . mysqli_error($conn));
			$row1 = mysqli_fetch_array($result1);
			echo $row1[0];
		  ?> Total Clients!
        </div>
      </div>
      <div class="card-footer text-white clearfix small z-1"></div>
    </div>
  </div>
  
  <div class="col-xl-6 col-sm-6 mb-3">
    <div class="card text-white bg-dark o-hidden h-100">
      <div class="card-body">
        <div class="card-body-icon">
          <i class="fab fa-fw fa-wpforms"></i>
        </div>
        <div class="mr-5 text-success text-center">
          <?php
			include("inc/config.php");
			$query2 = "SELECT COUNT(*) FROM tasks";
			$result2 = mysqli_query($conn, $query2) or die("Ошибка1 " . mysqli_error($conn));
			$row2 = mysqli_fetch_array($result2);
			echo $row2[0];
		  ?> Total Tasks!
        </div>
      </div>
      <div class="card-footer text-white clearfix small z-1"></div>
    </div>
  </div>
</div>
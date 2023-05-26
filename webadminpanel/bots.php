<div class="card mb-3 border-dark">
  <div class="card-header bg-dark text-success">
    <i class="fas  fa-user-circle text-success"></i>
    Bot List</div>
  <div class="card-body bg-dark text-success">
    <div class="table-responsive display responsive nowrap bg-dark">
      <table class="table table-bordered text-success" id="dataTable" width="100%" cellspacing="0">
        <thead>
          <tr>
            <th>ID</th>
            <th>IP Address</th>
            <th>PC Name</th>
            <th>Username</th>
            <th>Operating System</th>
            <th>Antivirus</th>
            <th>Machine GUID</th>
            <th>Version</th>
          </tr>
        </thead>
        <tbody>
          <?php 
          include("inc/config.php");
          $query ="SELECT `id`,`ip`,`pcname`,`username`,`sysinfo`,`avname`,`machineguid`,`version` FROM bots";
          $datares = mysqli_query($conn, $query) or die("Ошибка1 " . mysqli_error($conn));
          $n=mysqli_num_rows($datares);
          for($i=0;$i<$n;$i++){
          mysqli_data_seek($datares, $i);
          $datarow = mysqli_fetch_row($datares);
          $sysinfo = $datarow[4];
          $realsi = $sysinfo;
          if (strpos($sysinfo, 'Service Pack') !== false) $sysinfo = str_replace('Service Pack', 'SP', $sysinfo);
          if (strpos($sysinfo, 'Microsoft') !== false && strlen($sysinfo) >= 25) $sysinfo = str_replace('Microsoft', '', $sysinfo);
          if (strpos($sysinfo, 'Майкрософт') !== false && strlen($sysinfo) >= 25) $sysinfo = str_replace('Майкрософт', '', $sysinfo);
          if (strpos($sysinfo, 'Microsoft') == false && strlen($sysinfo) >= 30) $sysinfo =  mb_strimwidth($sysinfo, 0, 18, "...");
          if (strlen($procs) >= 25) $procs = mb_strimwidth($procs, 0, 19, "...");
          echo
          "<tr><td>",$datarow[0],
          "</td><td>",$datarow[1],
          "</td><td>",$datarow[2],
          "</td><td>",$datarow[3],
          "</td><td>",$sysinfo,
          "</td><td>",$datarow[5],
          "</td><td>",$datarow[6],
          "</td><td>",$datarow[7],
          "</td></tr>";
          }
          ?>
        </tbody>
      </table>
    </div>
  </div>
</div>
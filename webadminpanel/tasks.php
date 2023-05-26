<!DOCTYPE html>
<html>

<head>
  <?php include_once 'components/meta.php'; ?>
  <title>BotNet - Tasks</title>
  <?php include_once 'components/css.php'; ?>
</head>

<body id="page-top" class="bg-secondary">
  <?php include_once 'components/header.php'; ?>
  <div id="wrapper">
    <div id="content-wrapper">
      <div class="container-fluid bg-secondary">
        <ol class="breadcrumb bg-dark">
          <li class="breadcrumb-item bg-dark text-success">
            <a>System Logs</a>
          </li>
        </ol>
        <div class="card mb-3 border border-dark">
        <form method="POST" action="scripts/deletelogs.php">
            <div class="card-header bg-dark text-success">
              <i class="fas fa-clipboard-check text-success"></i>
              System Logs</div>
            <div class="card-body bg-dark">
              <div class="container text-center bg-sondary text-success">
                <div class="table-center pt-4 pb-4 bg-dark">
                  <table class="table table-bordered bg-dark text-success" id="dataTable" width="100%" cellspacing="0">
                    <thead>
                      <tr>
                        <th>ID</th>
                        <th>Started</th>
                        <th>Completed</th>
                        <th>Target</th>
                        <th>Command</th>
                        <th>Arguments</th>
                        <th>Status</th>
                      </tr>
                    </thead>
                    <tbody>
                    <?php
                    include ('inc/config.php');
                    $query ="SELECT cid,started,completed,target,cmd,arg1,arg2,arg3,arg4,status FROM tasks";
                    $result = mysqli_query($conn, $query) or die("Ошибка " . mysqli_error($conn));
                    mysqli_close($conn);
                    $n=mysqli_num_rows($result);
                    for($i=0;$i<$n;$i++)
                    {
                    mysqli_data_seek($result, $i);
                    $data_row = mysqli_fetch_row($result);
                    $cmdvalue = $data_row[4];
                    $arg1 = $data_row[5];
                    $arg2 = $data_row[6];
                    $arg3 = $data_row[7];
                    $arg4 = $data_row[8];
                    if ($arg1 != "" && $arg1 != null) $arg1 = $data_row[5]; else $arg1 = "null";
                    if ($arg2 != "" && $arg2 != null) $arg2 = ", ".$data_row[6]; else $arg2 = "";
                    if ($arg3 != "" && $arg3 != null) $arg3 = ", ".$data_row[7]; else $arg3 = "";
                    if ($arg4 != "" && $arg4 != null) $arg4 = ", ".$data_row[8]; else $arg4 = "";
                    $args = $arg1.$arg2.$arg3.$arg4;
                    if (strlen($args) > 26) $args = mb_strimwidth($args, 0, 27, "...");
                    if ($data_row[9] == "completed") $class = "status--process";
                    if ($data_row[2] == null) $comptd = "null"; else $comptd = $data_row[2];
                    if ($data_row[9] == "failed") $class = "status--denied";
                    if ($data_row[9] == "processing") $class = "stproc";
                    echo
                    "<tr><td class='supertable'>",$data_row[0],
                    "</td><td class='txt'>",$data_row[1],
                    "</td><td class='txt'>",$comptd,
                    "</td><td class='txt'>",$data_row[3],
                    "</td><td class='txt'>",$cmdvalue,
                    "</td><td class='txt'>", $args,
                    "</td><td class='$class'>",$data_row[9],
                    "</td></tr>";
                    }
                    ?>
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
            <div class="card-footer bg-dark">
              <button type="submit" class="btn btn-danger text-dark">Delete Logs</button>
            </div>
            </form>
        </div>
      </div>
    </div>
  </div>
  <?php include_once 'components/footer.php'; ?>

  <?php include_once 'components/js.php'; ?>

  <script src="asset/vendor/datatables/jquery.dataTables.js"></script>
  <script src="asset/vendor/datatables/dataTables.bootstrap4.js"></script>
  <script src="asset/vendor/responsive/dataTables.responsive.js"></script>
  <script src="asset/vendor/responsive/responsive.bootstrap4.js"></script>
  <script src="asset/js/demo/datatables-demo.js"></script>
</body>

</html>
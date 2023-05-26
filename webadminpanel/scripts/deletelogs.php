<?php
include("../inc/config.php");
$query ="DELETE FROM tasks";
$result = mysqli_query($conn, $query) or die("Ошибка1 " . mysqli_error($conn));
header('Location:'.$url."tasks.php");
?>
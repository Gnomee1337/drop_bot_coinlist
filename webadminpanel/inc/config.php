<?php
$host = "localhost";
$user = "adminbotnet";
$password = "admin123";
$db = "botnet";
$url = "http://www.test.botnet.com/"; // path to index.php
$conn = mysqli_connect($host, $user, $password, $db);
if (!$conn) {
    echo "Ошибка: Невозможно установить соединение с MySQL." . PHP_EOL;
    echo "Код ошибки errno: " . mysqli_connect_errno() . PHP_EOL;
    echo "Текст ошибки error: " . mysqli_connect_error() . PHP_EOL;
}
?>
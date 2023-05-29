<?php
require(__DIR__ .'/..'."//vendor//autoload.php");

# __DIR__ location of the .env file
$dotenv = Dotenv\Dotenv::createImmutable(__DIR__);
$dotenv->load();

$db_host = $_ENV['DB_HOST'];
$db_user = $_ENV['DB_USER'];
$db_password = $_ENV['DB_PASSWORD'];
$db_database = $_ENV['DB_DATABASE'];

$db = mysqli_connect($db_host, $db_user, $db_password, $db_database);
if (!$db) {
    echo "Ошибка: Невозможно установить соединение с MySQL." . PHP_EOL;
    echo "Код ошибки errno: " . mysqli_connect_errno() . PHP_EOL;
    echo "Текст ошибки error: " . mysqli_connect_error() . PHP_EOL;
}

?>
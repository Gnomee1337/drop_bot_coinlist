<?php
require(".\\vendor\\autoload.php");

# __DIR__ location of the .env file
$dotenv = Dotenv\Dotenv::createImmutable(__DIR__);
$dotenv->load();

$db_path = $_ENV['FULL_DB_PATH'];

$db = new SQLite3($db_path);
$foreign_keys_statement = $db->prepare("PRAGMA foreign_keys = ON");
$foreign_keys_statement->execute();

?>
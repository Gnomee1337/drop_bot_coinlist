<?php
session_start();
if (!isset($_SESSION['loggedin'])) {
  header('Location: login.php');
  exit;
} else {
  header('Location: main_panel.php');
  exit;
}
?>
<?php
session_start();
include("../inc/config.php");

// Now we check if the data from the login form was submitted, isset() will check if the data exists.
if (!isset($_POST['username'], $_POST['password'])) {
    // Could not get the data that should have been sent.
    exit('Please fill both the username and password fields!');
} else {
    $username = $_POST['username'];
    $statement = $db->prepare("SELECT `id_wp_accs`,`password_wp_accs` FROM webpanel_accounts WHERE `username_wp_accs` = '$username'");
    $result = $statement->execute();

    while ($accounts = $result->fetchArray())
        if (!empty($accounts)) {
            $id = $accounts[0];
            $password = $accounts[1];
            if (password_verify($_POST['password'], $password)) {
                session_regenerate_id();
                $_SESSION['loggedin'] = TRUE;
                $_SESSION['name'] = $_POST['username'];
                $_SESSION['id'] = $id;
                header('Location: ../index.php');
            } else {
                // Incorrect password
                echo 'Incorrect use rname and/or password!';
                header('Location: ../login.php');
            }
        } else {
            // Incorrect username
            echo 'Incorrect username and/or password!';
            #break;
            header('Location: ../login.php');
        }
}
?>
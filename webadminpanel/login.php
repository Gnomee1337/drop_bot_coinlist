<?
include("inc/config.php");
session_start();
$auth = $_SESSION["auth"];
if ($auth == "1")
header('Location:'.$url);
else
if (!isset($error)) {
  if (isset($_POST['username']) && isset($_POST['password']))
  {
      $username = $_POST['username'];
      $password = $_POST['password'];
      if ($username == "test" && $password == "test")
      {
          $_SESSION['auth'] = "1";
          header('Location:'.$url);
      }
      else
      {
        $_SESSION['auth'] = "2";
        $error = "Username or Password is incorrect.";
      }
  }
}
?>

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>BotNet - Login</title>
  <?php include_once 'components/css.php'; ?>
</head>

  <link rel="stylesheet" type="text/css" href="css/inputs.css">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<body class="bg-dark">
<div class="card-img-overlay">
  <div class="container">
    <div class="card card-login mx-auto bg-secondary mt-5 border-success">
      <h5 class="card-header text-success border-success"><strong>Authorization</strong></h5>
      <div class="card-body">
        <form method="POST">
          <?php if (isset($error)) : ?>
            <div class="alert alert-danger">
              <span class="fa fa-times-circle"></span> <?php echo $error ?>
            </div>
          <?php endif; ?>

          <div class="form-group">
              <input type="text" id="username"  name="username" class="form-control bg-dark text-success border-success" placeholder="Username" required="required">
          </div>
          <div class="form-group">
              <input type="password" id="password" name="password" class="form-control bg-dark text-success border-success" placeholder="Password" required="required">
          </div>
          <div class="align-content-center text-center">
            <?php if ($getSettings->recaptchastatus == "on") : ?>
              <div class="form-group">
                <div class="g-recaptcha" data-sitekey="<?php echo $getSettings->recaptchapublic; ?>" required></div>
              </div>
            <?php endif; ?>
          </div>
          <button type="submit" class="btn btn-dark btn-block text-success border-success">Login</button>
        </form>
      </div>
    </div>
  </div>
<html>
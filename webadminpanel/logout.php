<?php
  	include("inc/config.php");

    session_start();
   if(session_unset() && session_destroy()) {
    if (isset($_GET['msg'])) {
        header('Location:'.$url."login.php?msg=yes");
    }
    else{
        header('Location:'.$url."login.php");
    }
   }

   header('Location:'.$url."login.php")
?>
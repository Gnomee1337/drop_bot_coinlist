<nav class="navbar navbar-expand-lg navbar bg-light">
  <a class="navbar-brand mr-1 " href="index.php">Панель</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav"
    aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav ml-auto">

      <li class="nav-item <?php if (strpos(urlencode(htmlentities($_SERVER['REQUEST_URI'])), "index.php")) {
        echo ("active");
      } ?>">
        <a class="nav-link text-primary" href="index.php"><span class="fa fa-home"></span> Главная</a>
      </li>

      <li class="nav-item <?php if (strpos(urlencode(htmlentities($_SERVER['REQUEST_URI'])), "drop_users.php")) {
        echo ("active");
      } ?>">
        <a class="nav-link text-primary" href="drop_users.php"><span class="fa fa-id-card"></span> Пользователи (<?php
          include("inc/config.php");
          $statement = $db->prepare("SELECT COUNT(`id_drop_accs`) FROM drop_accs");
          $statement->execute();
          $result2 = $statement->get_result();
          $row = $result2->fetch_array();
          echo $row[0];
          ?>)
        </a>

      </li>

      <li class="nav-item <?php if (strpos(urlencode(htmlentities($_SERVER['REQUEST_URI'])), "drop_managers.php")) {
        echo ("active");
      } ?>">
        <a class="nav-link text-primary" href="drop_managers.php"><span class="fa fa-eye"></span> Менеджеры (<?php
          include("inc/config.php");
          $statement = $db->prepare("SELECT COUNT(`drop_manager_id`) FROM drop_manager");
          $statement->execute();
          $result2 = $statement->get_result();
          $row = $result2->fetch_array();
          echo $row[0];
          ?>)
        </a>
      </li>

      <li class="nav-item">
        <a class="nav-link text-primary" data-toggle="modal" data-target="#logoutModal"><span
            class="fa fa-sign-out-alt "></span>Выйти</a>
      </li>
    </ul>
  </div>
</nav>
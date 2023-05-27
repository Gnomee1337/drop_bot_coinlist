<?php
$status = session_status();
if ($status == PHP_SESSION_NONE) {
    //There is no active session
    session_start();
}
if (!isset($_SESSION['loggedin'])) {
    header('Location: login.php');
    exit;
} else {
    ?>
    <!DOCTYPE html>
    <html>

    <head>
        <?php include_once 'components/meta.php'; ?>
        <title>Пользователи</title>
        <?php include_once 'components/css.php'; ?>
    </head>

    <body id="page-top" class="bg-secondary">
        <?php include_once 'components/header.php'; ?>
        <div id="wrapper">
            <div id="content-wrapper">
                <div class="container-fluid bg-secondary">
                    <ol class="breadcrumb ">
                        <li class="breadcrumb-item ">
                            <a>База пользователей</a>
                        </li>
                    </ol>
                    <div class="card mb-3 border border-dark">
                        <div class="card-header ">
                            <i class="fas fa-clipboard-check s"></i>
                            Пользователи
                        </div>
                        <div class="card-body ">
                            <!-- <div class="container text-center bg-sondary  "> -->
                                <div class="table-responsive display responsive nowrap">
                                    <table class="table table-bordered table-hover " id="dataTable" width="100%"
                                        cellspacing="0">
                                        <thead>
                                            <tr>
                                                <th>Имя</th>
                                                <th>Отчество</th>
                                                <th>Фамилия</th>
                                                <th>Страна</th>
                                                <th>Область</th>
                                                <th>Город</th>
                                                <th>Адрес</th>
                                                <th>Postcode</th>
                                                <th>Дата</th>
                                                <th>Документы</th>
                                                <th>Телефон</th>
                                                <th>TG Nickname</th>
                                                <th>От кого</th>
                                                <th>Статус</th>
                                                <th>Язык</th>
                                                <th>ID</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <?php
                                            include('inc/config.php');
                                            $statement = $db->prepare("SELECT `first_name`,`middle_name`,`surname`,`country`,`region`,`city`,`address`,`postcode`,`date_of_birth`,`document_id`,`phone_number`,`tg_username`,`referral_id`,`user_status`,`language`,`id_drop_accs` FROM drop_accs ORDER BY `id_drop_accs`");
                                            $drop_accs = $statement->execute();

                                            $statement = $db->prepare("SELECT `drop_manager_id`,`dm_tg_id`,`dm_tg_username` FROM drop_manager");
                                            $drop_managers = $statement->execute();

                                            #Output data
                                            while ($users_verify_row = $drop_accs->fetchArray()) {

                                                #Change referral_id to manager_nickname
                                                while ($manager_row = $drop_managers->fetchArray()) {
                                                    if ($manager_row[1] == $users_verify_row[12])
                                                        $users_verify_row[12] = $manager_row[2];
                                                }

                                                #Change user_status code to text
                                                $user_status = $users_verify_row[13];
                                                if ($user_status == "filled") {
                                                    $user_status = "Зареган";
                                                } elseif ($user_status == "photo") {
                                                    $user_status = "Фото";
                                                } elseif ($user_status == "new") {
                                                    $user_status = "Пустой";
                                                } elseif ($user_status == "manual") {
                                                    $user_status = "Ручник";
                                                } elseif ($user_status == "fail") {
                                                    $user_status = "Фейл";
                                                }

                                                #Output in table
                                                echo
                                                    "<tr><td class='supertable'>", $users_verify_row[0],
                                                    "</td><td class='txt'>", $users_verify_row[1],
                                                    "</td><td class='txt'>", $users_verify_row[2],
                                                    "</td><td class='txt'>", $users_verify_row[3],
                                                    "</td><td class='txt'>", $users_verify_row[4],
                                                    "</td><td class='txt'>", $users_verify_row[5],
                                                    "</td><td class='txt'>", $users_verify_row[6],
                                                    "</td><td class='txt'>", $users_verify_row[7],
                                                    "</td><td class='txt'>", $users_verify_row[8],
                                                    "</td><td class='txt'>", $users_verify_row[9],
                                                    "</td><td class='txt'>", $users_verify_row[10],
                                                    "</td><td class='txt'>", '@' . $users_verify_row[11],
                                                    "</td><td class='txt'>", '@' . $users_verify_row[12],
                                                    "</td><td class='txt'>", $user_status,
                                                    "</td><td class='txt'>", $users_verify_row[14],
                                                    "</td><td class='txt'>", $users_verify_row[15],
                                                    // "</td><td>","<input type=\"checkbox\" style=\"text-align:center;\" ng-model=\"x.dedbuffer\">",
                                                    "</td></tr>";
                                            }
                                            ?>
                                        </tbody>
                                    </table>
                                </div>
                            <!-- </div> -->
                        </div>
                        <form method="POST" action="server.php" id="form_drops" name="form_drops">
                            <div class="card-footer ">
                                <?php include_once 'components/commands_drops.php'; ?>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
        <?php include_once 'components/footer.php'; ?>

        <?php include_once 'components/js.php'; ?>

        <script src="asset/vendor/datatables/jquery.dataTables.js"></script>
        <script src="asset/vendor/datatables/dataTables.bootstrap4.js"></script>
        <script src="asset/vendor/responsive/dataTables.responsive.js"></script>
        <script src="asset/vendor/responsive/responsive.bootstrap4.js"></script>
        <script src="asset/js/demo/datatables-demo.js"></script>
    </body>

    </html>

<?php } ?>
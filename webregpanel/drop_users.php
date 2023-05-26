<?php
session_start();
if (!isset($_SESSION['loggedin'])) {
    header('Location: phplogin/login.php');
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
                            <div class="container text-center bg-sondary ">
                                <div class="table-center pt-4 pb-4 ">
                                    <table class="table table-bordered " id="dataTable" width="100%"
                                        cellspacing="0">
                                        <thead>
                                            <tr>
                                                <th>ФИО</th>
                                                <th>Страна</th>
                                                <th>Область</th>
                                                <th>Город</th>
                                                <th>Адрес</th>
                                                <th>Дата рождения</th>
                                                <th>Документы</th>
                                                <th>Номер телефона</th>
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
                                            $statement = $db->prepare("SELECT `full_name`,`country`,`region`,`city`,`address`,`date_of_birth`,`document_id`,`phone_number`,`tg_username`,`referral_id`,`user_status`,`language`,`id_drop_accs` FROM drop_accs ORDER BY `id_drop_accs`");
                                            $drop_accs = $statement->execute();

                                            $statement = $db->prepare("SELECT `drop_manager_id`,`dm_tg_id`,`dm_tg_username` FROM drop_manager");
                                            $drop_managers = $statement->execute();

                                            #Output data
                                            while ($users_verify_row = $drop_accs->fetchArray()) {

                                                #Change referral_id to manager_nickname
                                                while ($manager_row = $drop_managers->fetchArray()) {
                                                    if ($manager_row[1] == $users_verify_row[9])
                                                        $users_verify_row[9] = $manager_row[2];
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
                                                    "</td><td class='txt'>", '@' . $users_verify_row[8],
                                                    "</td><td class='txt'>", '@' . $users_verify_row[9],
                                                    "</td><td class='txt'>", $users_verify_row[10],
                                                    "</td><td class='txt'>", $users_verify_row[11],
                                                    "</td><td class='txt'>", $users_verify_row[12],
                                                    // "</td><td>","<input type=\"checkbox\" style=\"text-align:center;\" ng-model=\"x.dedbuffer\">",
                                                    "</td></tr>";
                                            }
                                            ?>
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                        </div>
                        <form method="POST" action="server.php" id="form_drop_users" name="form_drop_users">
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
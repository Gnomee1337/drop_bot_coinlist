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
        <title>Менеджеры</title>
        <?php include_once 'components/css.php'; ?>
    </head>

    <body id="page-top" class="bg-secondary">
        <?php include_once 'components/header.php'; ?>
        <div id="wrapper">
            <div id="content-wrapper">
                <div class="container-fluid bg-secondary">
                    <ol class="breadcrumb">
                        <li class="breadcrumb-item">
                            <a>База менеджеров</a>
                        </li>
                    </ol>
                    <div class="card mb-3 border border-dark">
                        <div class="card-header">
                            <i class="fas fa-clipboard-check"></i>
                            Менеджеры
                        </div>
                        <div class="card-body ">
                            <div class="container text-center bg-sondary ">
                                <div class="table-center pt-4 pb-4">
                                    <table class="table table-bordered" id="dataTable" width="100%" cellspacing="0">
                                        <thead>
                                            <tr>
                                                <th>Телеграм Ник</th>
                                                <th>Телеграм ID</th>
                                                <th>ID</th>
                                                <th>Всего Пригласил</th>
                                                <th>Зареганных</th>
                                                <th>Апрувнутых</th>
                                                <th>Апрув + Не Оплачен</th>
                                                <th>Оплаченных</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <?php
                                            include('inc/config.php');
                                            $statement = $db->prepare("SELECT `dm_tg_username`,`dm_tg_id`,`drop_manager_id` FROM drop_manager ORDER BY `drop_manager_id`");
                                            $statement->execute();
                                            $drop_managers = $statement->get_result();

                                            #Output data
                                            while ($managers_row = $drop_managers->fetch_array()) {
                                                
                                                #Total invited
                                                $statement = $db->prepare("SELECT COUNT(`referral_id`) FROM drop_accs WHERE `referral_id` = '$managers_row[1]'");
                                                $statement->execute();
                                                $invited_count = $statement->get_result();
                                                $invited_count = $invited_count->fetch_array();
                                                
                                                #Total reg
                                                $statement = $db->prepare("SELECT COUNT(`referral_id`) FROM drop_accs WHERE `user_status` != 'new' AND  `referral_id` = '$managers_row[1]'");
                                                $statement->execute();
                                                $reg_count = $statement->get_result();
                                                $reg_count = $reg_count->fetch_array();

                                                #Approved
                                                $statement = $db->prepare("SELECT COUNT(`referral_id`) FROM drop_accs WHERE `user_status` = 'approved' AND  `referral_id` = '$managers_row[1]'");
                                                $statement->execute();
                                                $approved_count = $statement->get_result();
                                                $approved_count = $approved_count->fetch_array();

                                                #Paid
                                                $statement = $db->prepare("SELECT COUNT(`referral_id`) FROM drop_accs WHERE `paid` = 'paid' AND  `referral_id` = '$managers_row[1]'");
                                                $statement->execute();
                                                $paid_count = $statement->get_result();
                                                $paid_count = $paid_count->fetch_array();

                                                #Approved and Unpaid
                                                $statement = $db->prepare("SELECT COUNT(`referral_id`) FROM drop_accs WHERE `paid` = 'unpaid' AND `user_status` = 'approved' AND `referral_id` = '$managers_row[1]'");
                                                $statement->execute();
                                                $approved_unpaid_count = $statement->get_result();
                                                $approved_unpaid_count = $approved_unpaid_count->fetch_array();


                                                #Output in table
                                                echo
                                                    "<tr><td class='supertable'>", '@' . $managers_row[0],
                                                    "</td><td class='txt'>", $managers_row[1],
                                                    "</td><td class='txt'>", $managers_row[2],
                                                    "</td><td class='txt'>", $invited_count[0],
                                                    "</td><td class='txt'>", $reg_count[0],
                                                    "</td><td class='txt'>", $approved_count[0],
                                                    "</td><td class='txt'>", $approved_unpaid_count[0],
                                                    "</td><td class='txt'>", $paid_count[0],
                                                    // "</td><td>","<input type=\"checkbox\" style=\"text-align:center;\" ng-model=\"x.dedbuffer\">",
                                                    "</td></tr>";
                                            }
                                            ?>
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                        </div>
                        <form method="POST" action="server.php" id="form_drop_managers" name="form_drop_managers">
                            <div class="card-footer">
                                <?php include_once 'components/commands_managers.php'; ?>
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
<div class="card mb-3 border-dark">
    <div class="card-header text-primary">
        <i class="fas  fa-user-circle"></i>
        На верификацию
    </div>
    <div class="card-body  ">
        <div class="table-responsive display responsive nowrap ">
            <table class="table table-bordered " id="dataTable" width="100%" cellspacing="0">
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
                        <th>Дата Рождения</th>
                        <th>Документы</th>
                        <th>Телефон</th>
                        <th>TG Nickname</th>
                        <th>От кого</th>
                        <th>Статус</th>
                        <th>Язык</th>
                        <th>ID</th>
                        <!-- <th>test checkbox</th> -->
                    </tr>
                </thead>
                <tbody>
                    <?php
                    include("inc/config.php");
                    $statement = $db->prepare("SELECT `first_name`,`middle_name`,`surname`,`country`,`region`,`city`,`address`,`postcode`,`date_of_birth`,`document_id`,`phone_number`,`tg_username`,`referral_id`,`user_status`,`language`,`id_drop_accs` FROM drop_accs WHERE `user_status` = 'filled' OR `user_status` = 'photo' ORDER BY `id_drop_accs`");
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
                            $user_status = "Связаться";
                        }
                        elseif($user_status == "photo"){
                            $user_status = "Фото";
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
    </div>
</div>
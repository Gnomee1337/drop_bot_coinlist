<?php
error_reporting(E_ALL);
ini_set('display_errors', TRUE);
ini_set('display_startup_errors', TRUE);
include("inc/config.php");

#Get command from user
if (isset($_POST['cmd']) && $_POST['cmd'] != "" && $_POST['cmd'] != null) {
    $cmd = $_POST['cmd'];
    $cmd = preg_replace("~[\\/:*?'<>|]~", ' ', $cmd);

    ## Commands for verify
    if ($cmd == "cmd_verify_drop") {
        $target = $_POST['target_verify_drop'];
        $verify_status = preg_replace("~[\\/:*?'<>|]~", ' ', $_POST['verify_status_input']);
        print($target);
        print($verify_status);
        $statement = $db->prepare("UPDATE `drop_accs` SET `user_status` = '$verify_status' WHERE `id_drop_accs` = '$target'");
        $update_drops = $statement->execute();
    }
    header('Location: ' . $url . 'index.php');

    ## Commands for drops
    //Create drop
    if ($cmd == "cmd_drop_add") {
        #$target = $_POST['target_drop'];
        $drop_tgid = preg_replace("~[\\/:*?'<>|]~", ' ', $_POST['add_drop_tgid']);
        $drop_username = preg_replace("~[\\/:*?'<>|]~", ' ', $_POST['add_drop_username']);
        $drop_fullname = preg_replace("~[\\/:*?'<>|]~", ' ', $_POST['add_drop_fullname']);
        $drop_country = preg_replace("~[\\/:*?'<>|]~", ' ', $_POST['add_drop_country']);
        $drop_region = preg_replace("~[\\/:*?'<>|]~", ' ', $_POST['add_drop_region']);
        $drop_city = preg_replace("~[\\/:*?'<>|]~", ' ', $_POST['add_drop_city']);
        $drop_address = preg_replace("~[\\/:*?'<>|]~", ' ', $_POST['add_drop_address']);
        $drop_dateofbirth = preg_replace("~[\\/:*?'<>|]~", ' ', $_POST['add_drop_dateofbirth']);
        $drop_documentid = preg_replace("~[\\/:*?'<>|]~", ' ', $_POST['add_drop_documentid']);
        $drop_phonenumber = preg_replace("~[\\/:*?'<>|]~", ' ', $_POST['add_drop_phonenumber']);
        $drop_referral = preg_replace("~[\\/:*?'<>|]~", ' ', $_POST['add_drop_referral']);
        $drop_userstatus = preg_replace("~[\\/:*?'<>|]~", ' ', $_POST['add_drop_userstatus']);
        $drop_language = preg_replace("~[\\/:*?'<>|]~", ' ', $_POST['add_drop_language']);

        // Add drop to table
        $statement = $db->prepare("INSERT INTO `drop_accs` (`tg_id`,`tg_username`,`full_name`,`country`,`region`,`city`,`address`,`date_of_birth`,`document_id`,`phone_number`,`referral_id`,`language`,`user_status`) VALUES ('$drop_tgid', '$drop_username', '$drop_fullname','$drop_country','$drop_region','$drop_city','$drop_address','$drop_dateofbirth','$drop_documentid','$drop_phonenumber','$drop_referral','$drop_userstatus','$drop_language')");
        $create_user = $statement->execute();

        header('Location: ' . $url . 'drop_users.php');
    }
    // Edit drop
    if ($cmd == "cmd_drop_edit") {
        $target = $_POST['target_drop'];
        $drop_tgid = preg_replace("~[\\/:*?'<>|]~", ' ', $_POST['edit_drop_tgid']);
        $drop_username = preg_replace("~[\\/:*?'<>|]~", ' ', $_POST['edit_drop_username']);
        $drop_fullname = preg_replace("~[\\/:*?'<>|]~", ' ', $_POST['edit_drop_fullname']);
        $drop_country = preg_replace("~[\\/:*?'<>|]~", ' ', $_POST['edit_drop_country']);
        $drop_region = preg_replace("~[\\/:*?'<>|]~", ' ', $_POST['edit_drop_region']);
        $drop_city = preg_replace("~[\\/:*?'<>|]~", ' ', $_POST['edit_drop_city']);
        $drop_address = preg_replace("~[\\/:*?'<>|]~", ' ', $_POST['edit_drop_address']);
        $drop_dateofbirth = preg_replace("~[\\/:*?'<>|]~", ' ', $_POST['edit_drop_dateofbirth']);
        $drop_documentid = preg_replace("~[\\/:*?'<>|]~", ' ', $_POST['edit_drop_documentid']);
        $drop_phonenumber = preg_replace("~[\\/:*?'<>|]~", ' ', $_POST['edit_drop_phonenumber']);
        $drop_referral = preg_replace("~[\\/:*?'<>|]~", ' ', $_POST['edit_drop_referral']);
        $drop_userstatus = preg_replace("~[\\/:*?'<>|]~", ' ', $_POST['edit_drop_userstatus']);
        $drop_language = preg_replace("~[\\/:*?'<>|]~", ' ', $_POST['edit_drop_language']);
        $statement = $db->prepare("UPDATE `drop_accs` SET `tg_id` = CASE WHEN COALESCE('$drop_tgid','') = '' THEN `tg_id` ELSE '$drop_tgid' END,
                                                            `tg_username` = CASE WHEN COALESCE('$drop_username','') = '' THEN `tg_username` ELSE '$drop_username' END, 
                                                            `full_name` = CASE WHEN COALESCE('$drop_fullname','') = '' THEN `full_name` ELSE '$drop_fullname' END, 
                                                            `country` = CASE WHEN COALESCE('$drop_country','') = '' THEN `country` ELSE '$drop_country' END, 
                                                            `region` = CASE WHEN COALESCE('$drop_region','') = '' THEN `region` ELSE '$drop_region' END,
                                                            `city` = CASE WHEN COALESCE('$drop_city','') = '' THEN `city` ELSE '$drop_city' END,
                                                            `address` = CASE WHEN COALESCE('$drop_address','') = '' THEN `address` ELSE '$drop_address' END,
                                                            `date_of_birth` = CASE WHEN COALESCE('$drop_dateofbirth','') = '' THEN `date_of_birth` ELSE '$drop_dateofbirth' END,
                                                            `document_id` = CASE WHEN COALESCE('$drop_documentid','') = '' THEN `document_id` ELSE '$drop_documentid' END,
                                                            `phone_number` = CASE WHEN COALESCE('$drop_phonenumber','') = '' THEN `phone_number` ELSE '$drop_phonenumber' END,
                                                            `referral_id` = CASE WHEN COALESCE('$drop_referral','') = '' THEN `referral_id` ELSE '$drop_referral' END,
                                                            `language` = CASE WHEN COALESCE('$drop_language','') = '' THEN `language` ELSE '$drop_language' END,
                                                            `user_status` = CASE WHEN COALESCE('$drop_userstatus','') = '' THEN `user_status` ELSE '$drop_userstatus' END
                                                          WHERE `id_drop_accs` = $target");
        $edit_drop = $statement->execute();
        header('Location: ' . $url . 'drop_users.php');
    }
    // Delete drop
    if ($cmd == "cmd_drop_delete") {
        $target = $_POST['target_drop'];
        #echo $target;
        if ($target == 'ВСЕ ПОЛЬЗОВАТЕЛИ') {
            $statement = $db->prepare("DELETE FROM drop_accs");
            $delete_drops = $statement->execute();
        } else {
            $statement = $db->prepare("DELETE FROM drop_accs WHERE `id_drop_accs` = $target");
            $delete_drops = $statement->execute();
        }
        header('Location: ' . $url . 'drop_users.php');
    }

    ## Commands for managers
    //Create manager
    if ($cmd == "cmd_manager_add") {
        #$target = $_POST['target_manager'];
        $manager_tgid = preg_replace("~[\\/:*?'<>|]~", ' ', $_POST['add_manager_tgid']);
        $manager_username = preg_replace("~[\\/:*?'<>|]~", ' ', $_POST['add_manager_username']);

        // Add manager to table
        $statement = $db->prepare("INSERT INTO `drop_manager` (`dm_tg_id`,`dm_tg_username`) VALUES ('$manager_tgid', '$manager_username')");
        $create_manager = $statement->execute();

        header('Location: ' . $url . 'drop_managers.php');
    }
    // Edit manager
    if ($cmd == "cmd_manager_edit") {
        $target = $_POST['target_manager'];
        $manager_tgid = preg_replace("~[\\/:*?'<>|]~", ' ', $_POST['edit_drop_tgid']);
        $manager_username = preg_replace("~[\\/:*?'<>|]~", ' ', $_POST['edit_drop_username']);
        $statement = $db->prepare("UPDATE `drop_accs` SET `dm_tg_id` = CASE WHEN COALESCE('$manager_tgid','') = '' THEN `dm_tg_id` ELSE '$manager_tgid' END,
                                                            `dm_tg_username` = CASE WHEN COALESCE('$manager_username','') = '' THEN `dm_tg_username` ELSE '$manager_username' END
                                                      WHERE `drop_manager_id` = $target");
        $edit_drop = $statement->execute();
        header('Location: ' . $url . 'drop_managers.php');
    }
    // Delete manager
    if ($cmd == "cmd_manager_delete") {
        $target = $_POST['target_manager'];
        #echo $target;
        if ($target == 'ВСЕ МЕНЕДЖЕРЫ') {
            $statement = $db->prepare("DELETE FROM drop_manager");
            $delete_managers = $statement->execute();
        } else {
            $statement = $db->prepare("DELETE FROM drop_manager WHERE `drop_manager_id` = $target");
            $delete_managers = $statement->execute();
        }
        header('Location: ' . $url . 'drop_managers.php');
    }
} else {
    header('Location: ' . $url . 'index.php');
}
?>
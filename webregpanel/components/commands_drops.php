<div class="col">
    <div class="card mb-3 border-dark">
        <div class="card-header ">
            <i class="fas fa-wrench"></i>
            Команды для пользователей
        </div>
        <div class="card-body ">
            <div class="table-responsive pb-4  ">
                <table class="table table-bordered  " width="100%" cellspacing="0">
                    <thead>
                        <tr>
                            <th>Команды</th>
                            <th>Номер пользователя</th>
                            <th>Выполнить</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>
                                <!-- Commands row -->
                                <select class="form-control " id="select1" name="cmd">
                                    <option value="nocommand" selected>Выберите Команду</option>
                                    <optgroup label="Пользователи">
                                        <option value="cmd_drop_add">Добавить пользователя</option>
                                        <option value="cmd_drop_edit">Изменить пользователя</option>
                                        <option value="cmd_drop_delete">Удалить пользователя</option>
                                    </optgroup>
                                </select>
                            </td>
                            <!-- User Number row -->
                            <td>
                                <?php
                                include("inc/config.php");
                                $statement = $db->prepare("SELECT `id_drop_accs` FROM drop_accs ORDER BY `id_drop_accs`");
                                $drop_accs = $statement->execute();

                                echo ('<select class="form-control " id="target_drop" name="target_drop" required="required">');
                                // echo ("<option selected='all'>ВСЕ ПОЛЬЗОВАТЕЛИ</option>");
                                echo ("<option disabled selected>Выберите ID пользователя</option>");

                                #Output drop id
                                while ($droprow = $drop_accs->fetchArray()) {
                                    echo ("<option>" . $droprow[0] . "</option>");
                                }
                                ?>
                            </td>
                            <!-- Execute row -->
                            <td>
                                <button type="submit" name="form_drops" for="form_drops"
                                    class="btn btn-block btn-primary">
                                    Выполнить команду
                                </button>
                            </td>
                        </tr>
                    </tbody>
                </table>
                <!-- Drop options -->
                <!-- Create drop -->
                <p>
                    <input id="add_drop_tgid" type="number" class="form-control    " placeholder="Укажите Telegram ID"
                        name="add_drop_tgid" style="display: none">
                    <input id="add_drop_username" type="text" class="form-control    "
                        placeholder="Укажите Telegram Username" name="add_drop_username" style="display: none">
                    <input id="add_drop_firstname" type="text" class="form-control    "
                        placeholder="Укажите Имя пользователя" name="add_drop_firstname" style="display: none">
                    <input id="add_drop_middlename" type="text" class="form-control    "
                        placeholder="Укажите Отчество пользователя" name="add_drop_middlename" style="display: none">
                    <input id="add_drop_surname" type="text" class="form-control    "
                        placeholder="Укажите Фамилию пользователя" name="add_drop_surname" style="display: none">
                    <input id="add_drop_country" type="text" class="form-control    " placeholder="Укажите страну"
                        name="add_drop_country" style="display: none">
                    <input id="add_drop_region" type="text" class="form-control    " placeholder="Укажите регион"
                        name="add_drop_region" style="display: none">
                    <input id="add_drop_city" type="text" class="form-control    " placeholder="Укажите город"
                        name="add_drop_city" style="display: none">
                    <input id="add_drop_address" type="text" class="form-control" placeholder="Укажите адрес"
                        name="add_drop_address" style="display: none">
                    <input id="add_drop_postcode" type="text" class="form-control    "
                        placeholder="Укажите почтовый индекс" name="add_drop_postcode" style="display: none">
                    <input id="add_drop_dateofbirth" type="text" class="form-control    "
                        placeholder="Укажите дату рождения" name="add_drop_dateofbirth" style="display: none">
                    <input id="add_drop_documentid" type="text" class="form-control    " placeholder="Укажите документы"
                        name="add_drop_documentid" style="display: none">
                    <input id="add_drop_phonenumber" type="text" class="form-control    "
                        placeholder="Укажите номер телефона" name="add_drop_phonenumber" style="display: none">
                    <input id="add_drop_referral" type="number" class="form-control    "
                        placeholder="Укажите реферальный ид" name="add_drop_referral" style="display: none">
                    <select id="add_drop_userstatus" class="form-control    " name="add_drop_userstatus"
                        style="display: none">
                        <option value="0" disabled selected>Укажите статус пользователя</option>
                        <option value="new">Пустой</option>
                        <option value="filled">Зареган</option>
                        <option value="photo">Нужно Фото</option>
                        <option value="manual">Ручник</option>
                        <option value="fail">Заблочен</option>
                        <option value="approved">Одобрен</option>
                    </select>
                    <select id="add_drop_language" class="form-control    " placeholder="Укажите язык пользователя"
                        name="add_drop_language" style="display: none">
                        <option value="ru" disabled selected>Укажите язык пользователя</option>
                        <option value="ru">Русский</option>
                        <option value="en">Английский</option>
                    </select>
                    <input id="add_drop_approvedate" type="text" class="form-control" onfocus="(this.type='date')"
                        placeholder="Укажите Дату апрува CoinList" name="add_drop_approvedate" style="display: none">
                    <input id="add_drop_paymentdate" type="text" class="form-control" onfocus="(this.type='date')"
                        placeholder="Укажите Дату оплаты CoinList" name="add_drop_paymentdate" style="display: none">
                </p>
                <!-- Edit drop -->
                <p>
                    <input id="edit_drop_tgid" type="number" class="form-control    " placeholder="Укажите Telegram ID"
                        name="edit_drop_tgid" style="display: none">
                    <input id="edit_drop_username" type="text" class="form-control "
                        placeholder="Укажите Telegram Username" name="edit_drop_username" style="display: none">
                    <input id="edit_drop_firstname" type="text" class="form-control    "
                        placeholder="Укажите Имя пользователя" name="edit_drop_firstname" style="display: none">
                    <input id="edit_drop_middlename" type="text" class="form-control    "
                        placeholder="Укажите Отчество пользователя" name="edit_drop_middlename" style="display: none">
                    <input id="edit_drop_surname" type="text" class="form-control    "
                        placeholder="Укажите Фамилию пользователя" name="edit_drop_surname" style="display: none">
                    <input id="edit_drop_country" type="text" class="form-control    " placeholder="Укажите страну"
                        name="edit_drop_country" style="display: none">
                    <input id="edit_drop_region" type="text" class="form-control    " placeholder="Укажите регион"
                        name="edit_drop_region" style="display: none">
                    <input id="edit_drop_city" type="text" class="form-control    " placeholder="Укажите город"
                        name="edit_drop_city" style="display: none">
                    <input id="edit_drop_address" type="text" class="form-control    " placeholder="Укажите адрес"
                        name="edit_drop_address" style="display: none">
                    <input id="edit_drop_postcode" type="text" class="form-control    "
                        placeholder="Укажите почтовый индекс" name="edit_drop_postcode" style="display: none">
                    <input id="edit_drop_dateofbirth" type="text" class="form-control    "
                        placeholder="Укажите дату рождения" name="edit_drop_dateofbirth" style="display: none">
                    <input id="edit_drop_documentid" type="text" class="form-control    "
                        placeholder="Укажите документы" name="edit_drop_documentid" style="display: none">
                    <input id="edit_drop_phonenumber" type="text" class="form-control    "
                        placeholder="Укажите номер телефона" name="edit_drop_phonenumber" style="display: none">
                    <input id="edit_drop_referral" type="number" class="form-control    "
                        placeholder="Укажите реферальный ид" name="edit_drop_referral" style="display: none">
                    <select id="edit_drop_userstatus" class="form-control    " name="edit_drop_userstatus"
                        style="display: none">
                        <option value="0" disabled selected>Укажите статус пользователя</option>
                        <option value="new">Пустой</option>
                        <option value="filled">Заполнен</option>
                        <option value="photo">Нужно Фото</option>
                        <option value="manual">Ручник</option>
                        <option value="fail">Заблочен</option>
                        <option value="approved">Одобрен</option>
                    </select>
                    <select id="edit_drop_language" class="form-control    " placeholder="Укажите язык пользователя"
                        name="edit_drop_language" style="display: none">
                        <option value="ru" disabled selected>Укажите язык пользователя</option>
                        <option value="ru">Русский</option>
                        <option value="en">Английский</option>
                    </select>
                    <input id="edit_drop_approvedate" type="text" class="form-control" onfocus="(this.type='date')"
                        placeholder="Укажите Дату апрува CoinList" name="edit_drop_approvedate" style="display: none">
                    <input id="edit_drop_paymentdate" type="text" class="form-control" onfocus="(this.type='date')" 
                        placeholder="Укажите Дату оплаты CoinList" name="edit_drop_paymentdate" style="display: none">
                </p>

                <!-- User options check -->
                <script type="text/javascript">
                    var doc = document,
                        sel = doc.getElementById('select1'),
                        //Add user
                        adds1 = doc.getElementById('add_drop_tgid'),
                        adds2 = doc.getElementById('add_drop_username'),
                        adds3 = doc.getElementById('add_drop_firstname'),
                        adds4 = doc.getElementById('add_drop_middlename'),
                        adds5 = doc.getElementById('add_drop_surname'),
                        adds6 = doc.getElementById('add_drop_country'),
                        adds7 = doc.getElementById('add_drop_region'),
                        adds8 = doc.getElementById('add_drop_city'),
                        adds9 = doc.getElementById('add_drop_address'),
                        adds10 = doc.getElementById('add_drop_postcode'),
                        adds11 = doc.getElementById('add_drop_dateofbirth'),
                        adds12 = doc.getElementById('add_drop_documentid'),
                        adds13 = doc.getElementById('add_drop_phonenumber'),
                        adds14 = doc.getElementById('add_drop_referral'),
                        adds15 = doc.getElementById('add_drop_userstatus'),
                        adds16 = doc.getElementById('add_drop_language'),

                        //Edit user
                        adds17 = doc.getElementById('edit_drop_tgid'),
                        adds18 = doc.getElementById('edit_drop_username'),
                        adds19 = doc.getElementById('edit_drop_firstname'),
                        adds20 = doc.getElementById('edit_drop_middlename'),
                        adds21 = doc.getElementById('edit_drop_surname'),
                        adds22 = doc.getElementById('edit_drop_country'),
                        adds23 = doc.getElementById('edit_drop_region'),
                        adds24 = doc.getElementById('edit_drop_city'),
                        adds25 = doc.getElementById('edit_drop_address'),
                        adds26 = doc.getElementById('edit_drop_postcode'),
                        adds27 = doc.getElementById('edit_drop_dateofbirth'),
                        adds28 = doc.getElementById('edit_drop_documentid'),
                        adds29 = doc.getElementById('edit_drop_phonenumber'),
                        adds30 = doc.getElementById('edit_drop_referral'),
                        adds31 = doc.getElementById('edit_drop_userstatus'),
                        adds32 = doc.getElementById('edit_drop_language'),
                        
                        //Add date
                        adds33 = doc.getElementById('add_drop_approvedate'),
                        adds34 = doc.getElementById('add_drop_paymentdate'),

                        //Edit date
                        adds35 = doc.getElementById('edit_drop_approvedate'),
                        adds36 = doc.getElementById('edit_drop_paymentdate');

                    sel.addEventListener('change', function () {
                        //Add
                        adds1.style.display = this.value == "cmd_drop_add" ? 'block' : 'none';
                        adds2.style.display = this.value == "cmd_drop_add" ? 'block' : 'none';
                        adds3.style.display = this.value == "cmd_drop_add" ? 'block' : 'none';
                        adds4.style.display = this.value == "cmd_drop_add" ? 'block' : 'none';
                        adds5.style.display = this.value == "cmd_drop_add" ? 'block' : 'none';
                        adds6.style.display = this.value == "cmd_drop_add" ? 'block' : 'none';
                        adds7.style.display = this.value == "cmd_drop_add" ? 'block' : 'none';
                        adds8.style.display = this.value == "cmd_drop_add" ? 'block' : 'none';
                        adds9.style.display = this.value == "cmd_drop_add" ? 'block' : 'none';
                        adds10.style.display = this.value == "cmd_drop_add" ? 'block' : 'none';
                        adds11.style.display = this.value == "cmd_drop_add" ? 'block' : 'none';
                        adds12.style.display = this.value == "cmd_drop_add" ? 'block' : 'none';
                        adds13.style.display = this.value == "cmd_drop_add" ? 'block' : 'none';
                        adds14.style.display = this.value == "cmd_drop_add" ? 'block' : 'none';
                        adds15.style.display = this.value == "cmd_drop_add" ? 'block' : 'none';
                        adds16.style.display = this.value == "cmd_drop_add" ? 'block' : 'none';
                        adds33.style.display = this.value == "cmd_drop_add" ? 'block' : 'none';
                        adds34.style.display = this.value == "cmd_drop_add" ? 'block' : 'none';
                        

                        //Edit
                        adds17.style.display = this.value == "cmd_drop_edit" ? 'block' : 'none';
                        adds18.style.display = this.value == "cmd_drop_edit" ? 'block' : 'none';
                        adds19.style.display = this.value == "cmd_drop_edit" ? 'block' : 'none';
                        adds20.style.display = this.value == "cmd_drop_edit" ? 'block' : 'none';
                        adds21.style.display = this.value == "cmd_drop_edit" ? 'block' : 'none';
                        adds22.style.display = this.value == "cmd_drop_edit" ? 'block' : 'none';
                        adds23.style.display = this.value == "cmd_drop_edit" ? 'block' : 'none';
                        adds24.style.display = this.value == "cmd_drop_edit" ? 'block' : 'none';
                        adds25.style.display = this.value == "cmd_drop_edit" ? 'block' : 'none';
                        adds26.style.display = this.value == "cmd_drop_edit" ? 'block' : 'none';
                        adds27.style.display = this.value == "cmd_drop_edit" ? 'block' : 'none';
                        adds28.style.display = this.value == "cmd_drop_edit" ? 'block' : 'none';
                        adds29.style.display = this.value == "cmd_drop_edit" ? 'block' : 'none';
                        adds30.style.display = this.value == "cmd_drop_edit" ? 'block' : 'none';
                        adds31.style.display = this.value == "cmd_drop_edit" ? 'block' : 'none';
                        adds32.style.display = this.value == "cmd_drop_edit" ? 'block' : 'none';
                        adds35.style.display = this.value == "cmd_drop_edit" ? 'block' : 'none';
                        adds36.style.display = this.value == "cmd_drop_edit" ? 'block' : 'none';
                    },
                        false);
                </script>
            </div>
        </div>
    </div>
</div>
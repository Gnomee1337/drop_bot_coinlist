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
                                echo ("<option selected='all'>ВСЕ ПОЛЬЗОВАТЕЛИ</option>");
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
                    <input id="add_drop_tgid" type="text" class="form-control form-control-sm   "
                        placeholder="Укажите Telegram ID" name="add_drop_tgid" style="display: none">
                    <input id="add_drop_username" type="text"
                        class="form-control form-control-sm   "
                        placeholder="Укажите Telegram Username" name="add_drop_username" style="display: none">
                    <input id="add_drop_fullname" type="text"
                        class="form-control form-control-sm   "
                        placeholder="Укажите ФИО пользователя" name="add_drop_fullname" style="display: none">
                    <input id="add_drop_country" type="text"
                        class="form-control form-control-sm   " placeholder="Укажите страну"
                        name="add_drop_country" style="display: none">
                    <input id="add_drop_region" type="text"
                        class="form-control form-control-sm   " placeholder="Укажите регион"
                        name="add_drop_region" style="display: none">
                    <input id="add_drop_city" type="text" class="form-control form-control-sm   "
                        placeholder="Укажите город" name="add_drop_city" style="display: none">
                    <input id="add_drop_address" type="text"
                        class="form-control form-control-sm   " placeholder="Укажите адресс"
                        name="add_drop_address" style="display: none">
                    <input id="add_drop_dateofbirth" type="text"
                        class="form-control form-control-sm   "
                        placeholder="Укажите дату рождения" name="add_drop_dateofbirth" style="display: none">
                    <input id="add_drop_documentid" type="text"
                        class="form-control form-control-sm   " placeholder="Укажите документы"
                        name="add_drop_documentid" style="display: none">
                    <input id="add_drop_phonenumber" type="text"
                        class="form-control form-control-sm   "
                        placeholder="Укажите номер телефона" name="add_drop_phonenumber" style="display: none">
                    <input id="add_drop_referral" type="number"
                        class="form-control form-control-sm   "
                        placeholder="Укажите реферальный ид" name="add_drop_referral" style="display: none">
                    <select id="add_drop_userstatus" class="form-control form-control-sm   "
                        name="add_drop_userstatus" style="display: none">
                        <option value="0" disabled selected>Укажите статус пользователя</option>
                        <option value="new">Пустой</option>
                        <option value="filled">Заполнен</option>
                        <option value="photo">Нужно Фото</option>
                        <option value="declined">Заблочен</option>
                        <option value="approved">Одобрен</option>
                    </select>
                    <select id="add_drop_language" class="form-control form-control-sm   "
                        placeholder="Укажите язык пользователя" name="add_drop_language" style="display: none">
                        <option value="ru" disabled selected>Укажите язык пользователя</option>
                        <option value="ru">ru</option>
                        <option value="en">en</option>
                    </select>
                </p>
                <!-- Edit drop -->
                <p>
                    <input id="edit_drop_tgid" type="text" class="form-control form-control-sm   "
                        placeholder="Укажите Telegram ID" name="edit_drop_tgid" style="display: none">
                    <input id="edit_drop_username" type="text"
                        class="form-control form-control-sm"
                        placeholder="Укажите Telegram Username" name="edit_drop_username" style="display: none">
                    <input id="edit_drop_fullname" type="text"
                        class="form-control form-control-sm   "
                        placeholder="Укажите ФИО пользователя" name="edit_drop_fullname" style="display: none">
                    <input id="edit_drop_country" type="text"
                        class="form-control form-control-sm   " placeholder="Укажите страну"
                        name="edit_drop_country" style="display: none">
                    <input id="edit_drop_region" type="text"
                        class="form-control form-control-sm   " placeholder="Укажите регион"
                        name="edit_drop_region" style="display: none">
                    <input id="edit_drop_city" type="text"
                        class="form-control form-control-sm   " placeholder="Укажите город"
                        name="edit_drop_city" style="display: none">
                    <input id="edit_drop_address" type="text"
                        class="form-control form-control-sm   " placeholder="Укажите адрес"
                        name="edit_drop_address" style="display: none">
                    <input id="edit_drop_dateofbirth" type="text"
                        class="form-control form-control-sm   "
                        placeholder="Укажите дату рождения" name="edit_drop_dateofbirth" style="display: none">
                    <input id="edit_drop_documentid" type="text"
                        class="form-control form-control-sm   " placeholder="Укажите документы"
                        name="edit_drop_documentid" style="display: none">
                    <input id="edit_drop_phonenumber" type="text"
                        class="form-control form-control-sm   "
                        placeholder="Укажите номер телефона" name="edit_drop_phonenumber" style="display: none">
                    <input id="edit_drop_referral" type="number"
                        class="form-control form-control-sm   "
                        placeholder="Укажите реферальный ид" name="edit_drop_referral" style="display: none">
                    <select id="edit_drop_userstatus" class="form-control form-control-sm   "
                        name="edit_drop_userstatus" style="display: none">
                        <option value="0" disabled selected>Укажите статус пользователя</option>
                        <option value="new">Пустой</option>
                        <option value="filled">Заполнен</option>
                        <option value="photo">Нужно Фото</option>
                        <option value="declined">Заблочен</option>
                        <option value="approved">Одобрен</option>
                    </select>
                    <select id="edit_drop_language" class="form-control form-control-sm   "
                        placeholder="Укажите язык пользователя" name="edit_drop_language" style="display: none">
                        <option value="ru" disabled selected>Укажите язык пользователя</option>
                        <option value="ru">ru</option>
                        <option value="en">en</option>
                    </select>
                </p>

                <!-- User options check -->
                <script type="text/javascript">
                    var doc = document,
                        sel = doc.getElementById('select1'),
                        //Add user
                        adds1 = doc.getElementById('add_drop_fullname'),
                        adds2 = doc.getElementById('add_drop_country'),
                        adds3 = doc.getElementById('add_drop_region'),
                        adds4 = doc.getElementById('add_drop_city'),
                        adds5 = doc.getElementById('add_drop_address'),
                        adds6 = doc.getElementById('add_drop_dateofbirth'),
                        adds7 = doc.getElementById('add_drop_documentid'),
                        adds8 = doc.getElementById('add_drop_phonenumber'),
                        adds9 = doc.getElementById('add_drop_referral'),
                        adds10 = doc.getElementById('add_drop_userstatus'),
                        adds11 = doc.getElementById('add_drop_language'),

                        //Edit user
                        adds12 = doc.getElementById('edit_drop_fullname'),
                        adds13 = doc.getElementById('edit_drop_country'),
                        adds14 = doc.getElementById('edit_drop_region'),
                        adds15 = doc.getElementById('edit_drop_city'),
                        adds16 = doc.getElementById('edit_drop_address'),
                        adds17 = doc.getElementById('edit_drop_dateofbirth'),
                        adds18 = doc.getElementById('edit_drop_documentid'),
                        adds19 = doc.getElementById('edit_drop_phonenumber'),
                        adds20 = doc.getElementById('edit_drop_referral'),
                        adds21 = doc.getElementById('edit_drop_userstatus'),
                        adds22 = doc.getElementById('edit_drop_language'),

                        //Add user
                        adds23 = doc.getElementById('add_drop_tgid'),
                        adds24 = doc.getElementById('add_drop_username'),
                        
                        //Edit user
                        adds25 = doc.getElementById('edit_drop_tgid'),
                        adds26 = doc.getElementById('edit_drop_username');
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
                        adds23.style.display = this.value == "cmd_drop_add" ? 'block' : 'none';
                        adds24.style.display = this.value == "cmd_drop_add" ? 'block' : 'none';


                        //Edit
                        adds12.style.display = this.value == "cmd_drop_edit" ? 'block' : 'none';
                        adds13.style.display = this.value == "cmd_drop_edit" ? 'block' : 'none';
                        adds14.style.display = this.value == "cmd_drop_edit" ? 'block' : 'none';
                        adds15.style.display = this.value == "cmd_drop_edit" ? 'block' : 'none';
                        adds16.style.display = this.value == "cmd_drop_edit" ? 'block' : 'none';
                        adds17.style.display = this.value == "cmd_drop_edit" ? 'block' : 'none';
                        adds18.style.display = this.value == "cmd_drop_edit" ? 'block' : 'none';
                        adds19.style.display = this.value == "cmd_drop_edit" ? 'block' : 'none';
                        adds20.style.display = this.value == "cmd_drop_edit" ? 'block' : 'none';
                        adds21.style.display = this.value == "cmd_drop_edit" ? 'block' : 'none';
                        adds22.style.display = this.value == "cmd_drop_edit" ? 'block' : 'none';
                        adds25.style.display = this.value == "cmd_drop_edit" ? 'block' : 'none';
                        adds26.style.display = this.value == "cmd_drop_edit" ? 'block' : 'none';
                    },
                        false);
                </script>
            </div>
        </div>
    </div>
</div>
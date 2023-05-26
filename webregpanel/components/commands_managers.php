<div class="col">
    <div class="card mb-3 ">
        <div class="card-header ">
            <i class="fas fa-wrench"></i>
            Команды для менеджеров
        </div>
        <div class="card-body">
            <div class="table-responsive pb-4 ">
                <table class="table table-bordered " width="100%" cellspacing="0">
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
                                        <option value="cmd_manager_add">Добавить менеджера</option>
                                        <option value="cmd_manager_edit">Изменить менеджера</option>
                                        <option value="cmd_manager_delete">Удалить менеджера</option>
                                    </optgroup>
                                </select>
                            </td>
                            <!-- User Number row -->
                            <td>
                                <?php
                                include("inc/config.php");
                                $statement = $db->prepare("SELECT `drop_manager_id` FROM drop_manager ORDER BY `drop_manager_id`");
                                $drop_manager = $statement->execute();

                                echo ('<select class="form-control" id="target_manager" name="target_manager" required="required">');
                                echo ("<option selected='all'>ВСЕ МЕНЕДЖЕРЫ</option>");
                                echo ("<option disabled selected>Выберите ID менеджера</option>");

                                #Output drop id
                                while ($manager_row = $drop_manager->fetchArray()) {
                                    echo ("<option>" . $manager_row[0] . "</option>");
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
                <!-- Manager options -->
                <!-- Create manager -->
                <p>
                    <input id="add_manager_tgid" type="number"
                        class="form-control form-control-sm"
                        placeholder="Укажите Telegram ID менеджера" name="add_manager_tgid" style="display: none">
                    <input id="add_manager_username" type="text"
                        class="form-control form-control-sm "
                        placeholder="Укажите Telegram username менеджера" name="add_manager_username"
                        style="display: none">
                </p>
                <!-- Edit manager -->
                <p>
                    <input id="edit_manager_tgid" type="text"
                        class="form-control form-control-sm " placeholder="Укажите Telegram ID"
                        name="edit_manager_tgid" style="display: none">
                    <input id="edit_manager_username" type="text"
                        class="form-control form-control-sm"
                        placeholder="Укажите Telegram Username" name="edit_manager_username" style="display: none">
                </p>
                <!-- User options check -->
                <script type="text/javascript">
                    var doc = document,
                        sel = doc.getElementById('select1'),
                        //Add user
                        adds1 = doc.getElementById('add_manager_tgid'),
                        adds2 = doc.getElementById('add_manager_username'),

                        //Edit user
                        adds3 = doc.getElementById('edit_manager_tgid'),
                        adds4 = doc.getElementById('edit_manager_username');
                    sel.addEventListener('change', function () {
                        //Add
                        adds1.style.display = this.value == "cmd_manager_add" ? 'block' : 'none';
                        adds2.style.display = this.value == "cmd_manager_add" ? 'block' : 'none';


                        //Edit
                        adds3.style.display = this.value == "cmd_manager_edit" ? 'block' : 'none';
                        adds4.style.display = this.value == "cmd_manager_edit" ? 'block' : 'none';
                    },
                        false);
                </script>
            </div>
        </div>
    </div>
</div>
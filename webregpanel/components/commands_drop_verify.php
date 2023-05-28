<div class="col">
    <div class="card mb-3 border-dark">
        <div class="card-header  ">
            <i class="fas fa-wrench"></i>
            Команды для верификации
        </div>
        <div class="card-body ">
            <div class="table-responsive pb-4 ">
                <table class="table table-bordered " width="100%" cellspacing="0">
                    <thead>
                        <tr>
                            <th>Команды</th>
                            <th>ID пользователя</th>
                            <th>Выполнить</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>
                                <!-- Commands row -->
                                <select class="form-control" id="select1" name="cmd">
                                    <option value="nocommand" selected>Выберите Команду</option>
                                    <optgroup label="Верификация">
                                        <option value="cmd_verify_drop">Верифицировать пользователя</option>
                                    </optgroup>
                                </select>
                            </td>
                            <!-- Verify Drops row -->
                            <td>
                                <?php
                                include("inc/config.php");
                                $statement = $db->prepare("SELECT `id_drop_accs` FROM drop_accs WHERE `user_status` != 'new' ORDER BY `id_drop_accs`");
                                $statement->execute();
                                $drop_accs = $statement->get_result();

                                echo ('<select class="form-control  " id="target_verify_drop" name="target_verify_drop" required="required">');
                                echo ("<option disabled selected>Выберите пользователя</option>");
                                // echo ("<option selected='all'>ВСЕМ ПОЛЬЗОВАТЕЛЯМ</option>");
                                
                                #Output users
                                while ($droprow = $drop_accs->fetch_array()) {
                                    echo ("<option>" . $droprow[0] . "</option>");
                                }
                                ?>
                            </td>
                            <!-- Execute row -->
                            <td>
                                <button type="submit" name="form_drop_verify" for="form_drop_verify"
                                    class="btn btn-block btn-primary">
                                    Изменить статус
                                </button>
                            </td>
                        </tr>
                    </tbody>
                </table>
                <!-- Drop options -->
                <p>
                    <select id="verify_status_input" class="form-control "
                        name="verify_status_input" style="display: none">
                        <option value="0" disabled selected>Укажите статус пользователя</option>
                        <option value="approved" class="form-control text-success font-weight-bold">Одобрен
                        </option>
                        <option value="photo" class="form-control text-warning font-weight-bold">Нужно фото
                        </option>
                        <option value="manual" class="form-control text-info font-weight-bold">Ручник
                        </option>
                        <option value="fail" class="form-control text-danger font-weight-bold">Отклонить
                        </option>
                    </select>
                </p>
                <!-- User options check -->
                <script type="text/javascript">
                    var doc = document,
                        sel = doc.getElementById('select1'),
                        adds1 = doc.getElementById('verify_status_input');
                    sel.addEventListener('change', function () {
                        adds1.style.display = this.value == "cmd_verify_drop" ? 'block' : 'none';
                    },
                        false);
                </script>
            </div>
        </div>
    </div>
</div>
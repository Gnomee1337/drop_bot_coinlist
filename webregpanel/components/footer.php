<footer class="my-sm-10 sticky bg-light">
  <div class="container my-auto bg-light">
    <div class="copyright text-center">
      <span>Панель</a> -
        <?php echo date('Y'); ?>
        <br>
      </span>
    </div>
  </div>
</footer>

<a class="scroll-to-top rounded" href="#page-top">
  <i class="fas fa-angle-up"></i>
</a>

<div class="modal fade" id="logoutModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel"
  aria-hidden="true">
  <div class="modal-dialog bg-secondary" role="document">
    <div class="modal-content bg-secondary">
      <div class="modal-header bg-secondary">
        <h5 class="modal-title text-white" id="exampleModalLabel">Готовы выйти из панели?</h5>
      </div>
      <div class="modal-body text-white">Вы действительно хотите закончить сессию?</div>
      <div class="modal-body text-warning">Все несохраненные данные будут утеряны!</div>
      <div class="modal-footer bg-secondary">
        <button class="btn btn-dark" type="button" data-dismiss="modal">Отменить</button>
        <a class="btn btn-danger" href="logout.php">Выйти</a>
      </div>
    </div>
  </div>
</div>
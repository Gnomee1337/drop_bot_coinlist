 <footer class="my-sm-10 sticky bg-dark">
          <div class="container my-auto bg-dark">
            <div class="copyright text-center text-success">
              <span>BotNet by Gnome</a> - <?php echo date('Y'); ?>
                <br></span>
            </div>
          </div>
        </footer>

        <a class="scroll-to-top rounded" href="#page-top">
          <i class="fas fa-angle-up"></i>
        </a>

        <div class="modal fade" id="logoutModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
          <div class="modal-dialog bg-secondary" role="document">
            <div class="modal-content bg-secondary">
              <div class="modal-header bg-secondary">
                <h5 class="modal-title text-success" id="exampleModalLabel">Ready to Leave?</h5>
              </div>
              <div class="modal-body text-success">Do you really ready to end your current session?</div>
              <div class="modal-body text-warning">Any unsynced data will be lost!</div>
              <div class="modal-footer bg-secondary">
                <button class="btn btn-dark" type="button" data-dismiss="modal">Cancel</button>
                <a class="btn btn-success" href="logout.php">Logout</a>
              </div>
            </div>
          </div>
        </div>
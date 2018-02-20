<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Elektronski dnevnik</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.6.2/css/bulma.min.css">
  </head>
  <body>
  <section class="section">
    <div class="container">
	<a href="/">
	<div class="button is-primary is-medium" style="position: fixed; top: 10px; right: 10px; z-index: 999999;">
		Odjavite se
	</div></a>

      <h1 class="title is-1">Elektronski dnevnik</h1>
      <h1 class="subtitle">Profesor</h1>


%if dalJeRazredni != "ne":
		  		<a href="/mojeodeljenje" target="_blank"><p class="is-1">Pogledajte svoje odeljenje</p></a>
		  		%end


<div class="tile is-ancestor">
      <div class="tile is-vertical is-4">
        <div class="tile">
          <div class="tile is-parent is-vertical">
              <p class="title notification">Upis za odeljenje</p><div class="content" style="max-height: 500px; overflow-y:auto;">
            <!-- TABELA PROFESORA -->
	<form action="/upisatiocenu" method="post"  autocomplete="off">
		    		<h3 class="title is-4">Upis ocene</h3>
		    		<input type="text" class="input" name="ime" placeholder="Prezime i ime ucenika" required=""><br><br>
					Ocena: <select name="ocena">
						<option value="1">1</option>
						<option value="2">2</option>
						<option value="3">3</option>
						<option value="4">4</option>
						<option value="5">5</option>
					</select><br><br>
					<textarea class="textarea" name="beleskaOcene" placeholder="Beleska za ocenu" required></textarea class="textarea"><br><br>
					<button type="submit" class="button">Potvrdi</button>
		    	</form>
		    	<hr>
		    	<form action="/upisatiizostanak" method="post" autocomplete="off">
		    		<h3 class="title is-4">Upis izostanaka</h3>
					<input type="text" class="input" name="ime" placeholder="Prezime i ime ucenika" required><br><br>
					<button type="submit" class="button">Potvrdi</button>
		    	</form>
		    	<hr>
		    	<form action="/upisatinapomenu" method="post" autocomplete="off">
		    		<h3 class="title is-4">Upis napomene</h3>

					<input type="text" class="input" name="ime" placeholder="Prezime i ime ucenika" required><br><br>
					<textarea class="textarea" name="zasto" placeholder="Razlog za napomenu" required></textarea class="textarea"><br><br>

					<button type="submit" class="button">Potvrdi</button>
		    	</form>
		    	<hr>
		    	<form action="/zakazikontrolni" method="post" autocomplete="off">
		    		<h3 class="title is-4">Zakazati kontrolni</h3>

					<input type="text" class="input" name="datum" placeholder="Upisite datum za kontrolni, format: 05.07." minlength="6" maxlength="6" required>
					<p>**Vazi za ovo odeljenjeu <br> u kojem ste trenutno: {{trenutnoOdeljenje}}</p>
					

					<button type="submit" class="button">Potvrdi</button>
		    	</form>
				<hr>
				<form action="/ponistavanjekontrolnog" method="post" autocomplete="off">
		    		<h3 class="title is-4">Ponistavanje kontrolnog</h3>

					<input type="text" class="input" name="sifraKontrolneVezbe" placeholder="Unesite sifru kontrolnog" minlength="10" maxlength="10" required><br><br>
					

					<button type="submit" class="button">Potvrdi</button>
		    	</form>


  </div>
          </div>
        </div>
      </div>
<div class="tile is-child is-vertical">
        <div class="tile">
          <div class="tile is-parent is-vertical">
              <p class="title is-3 notification">Pregled odeljenja</p><div class="content" style="overflow-y: auto; max-height: 500px; padding: 5px;">
<div class="block">
              <table class="table is-fullwidth is-hoverable">
      	<thead>
      		<tr>
      			<tr><th>Prezime i ime ucenika</th><th>Ocene</th></tr>
      		</tr>
      	</thead>
      	<tbody>
				%for ucenik, ocene in sve:
				<tr>
					<td>{{ucenik}}</td><td>{{ocene}}</td>
				</tr>

				%end
      	</tbody>
      </table>






		</div>
</div>
  </div>
</div>








</div></div>
<div class="block" style="margin-top: 30px;">
	<div class="columns is-mobile is-centered">

  <div class="column is-centered is-auto"><p class="title is-3 notification">Pregled vasih kontrolnih</p>
  	<div class="content" style="max-height: 450px; overflow-y: auto;">
  <table>
  	<thead>
  		<tr><th>Odeljenje</th><th>Datum</th><th>Sifra kontrolnog</th></tr>
  	</thead>
  	<tbody>
  		%for koje, kad, sifraKontrolne in kontrolniSvi:
				%if koje == "Nemate zakazanih kontrolnih":
				<td colspan="3">Nemate zakazane kontrolne</td>
				%break
				%end
				<tr>
					<td>{{koje}}</td><td>{{kad}}</td><td>{{sifraKontrolne}}</td>
				</tr>

				%end
  	</tbody>
  </table>


		</div>
</div>
  </div>
</div>




<br><br><br><br>

		</div>
    </section>
  </body>
</html>

				
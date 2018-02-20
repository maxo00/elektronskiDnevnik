<!DOCTYPE html>
<html>
<head>
	<meta name="author" content="Marko Maksimovic">
	<title>Pregled dnevnika</title>
	<link rel="stylesheet" type="text/css" href="../static/profesor.css">
</head>
<body>
	<a href="/">
	<div id="odjava">
		Odjavite se
	</div></a>
<div class="stranica">
		  <div class="vrh">
		  	<h1 id="glavniNaslov">Elektronski dnevnik, profesor</h1>

		  </div>

		  <div class="zaCas">
		  	%if dalJeRazredni != "ne":
		  	<a href="/mojeodeljenje" target="_blank">Pogledajte svoje odeljenje</a>
		  	%end
		    <div id="forme">
		    	<form action="/upisatiocenu" method="post"  autocomplete="off">
		    		<h3>Upis ocene</h3>
		    		<input type="text" name="ime" placeholder="Prezime i ime ucenika" required=""><br><br>
					Ocena: <select name="ocena">
						<option value="1">1</option>
						<option value="2">2</option>
						<option value="3">3</option>
						<option value="4">4</option>
						<option value="5">5</option>
					</select><br><br>
					<textarea name="beleskaOcene" placeholder="Beleska za ocenu" required></textarea><br><br>
					<button type="submit">Potvrdi</button>

		    	</form>
		    	<hr>
		    	<form action="/upisatiizostanak" method="post" autocomplete="off">
		    		<h3>Upis izostanaka</h3>
					<input type="text" name="ime" placeholder="Prezime i ime ucenika" required><br><br>
					<button type="submit">Potvrdi</button>
			


		    	</form>
		    	<hr>
		    	<form action="/upisatinapomenu" method="post" autocomplete="off">
		    		<h3>Upis napomene</h3>

					<input type="text" name="ime" placeholder="Prezime i ime ucenika" required><br><br>
					<textarea name="zasto" placeholder="Razlog za napomenu" required></textarea><br><br>

					<button type="submit">Potvrdi</button>



		    	</form>
		    	<hr>
		    	<form action="/zakazikontrolni" method="post" autocomplete="off">
		    		<h3>Zakazati kontrolni</h3>

					<input type="text" name="datum" placeholder="Upisite datum za kontrolni, format: 05.07." minlength="6" maxlength="6" required>
					<p>**Vazi za ovo odeljenjeu <br> u kojem ste trenutno: {{trenutnoOdeljenje}}</p>
					

					<button type="submit">Potvrdi</button>



		    	</form>
					<hr>
					<form action="/ponistavanjekontrolnog" method="post" autocomplete="off">
		    		<h3>Ponistavanje kontrolnog</h3>

					<input type="text" name="sifraKontrolneVezbe" placeholder="Unesite sifru kontrolnog" minlength="10" maxlength="10" required><br><br>
					

					<button type="submit">Potvrdi</button>



		    	</form>
		    </div>

		</div>


		  <div class="tabelaZaCas">
				<center><h2>Pregled vaseg predmeta</h2></center>
				<center><table>
					
				<tr><th>Prezime i ime ucenika</th><th>Ocene</th></tr>

				%for ucenik, ocene in sve:
				<tr>
					<td>{{ucenik}}</td><td>{{ocene}}</td>
				</tr>

				%end

				</table></center>
		 	
		</div>


  <div class="zakazaniKontrolniProfesor">
	<center><h2>Pregled vasih najavljenih kontrolnih, koji nisu odrzani</h2></center>
				<center><table>
					
				<tr><th>Odeljenje</th><th>Datum</th><th>Sifra kontrolnog</th></tr>
				%for koje, kad, sifraKontrolne in kontrolniSvi:
				%if koje == "Nemate zakazanih kontrolnih":
				<td colspan="3">Nemate zakazane kontrolne</td>
				%break
				%end
				<tr>
					<td>{{koje}}</td><td>{{kad}}</td><td>{{sifraKontrolne}}</td>
				</tr>

				%end
				</table></center>
	</div>



	
  	

    </div>
</body>
</html>
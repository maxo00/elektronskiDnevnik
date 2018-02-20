<!DOCTYPE html>

<html>
<head>
	<meta name="author" content="Marko Maksimovic">
	<title>Elektronski dnevnik, direktor</title>
	<link href="../static/direktor.css" rel="stylesheet" type="text/css">
</head>

<body>
	<a href="/">
	<div id="odjava">
		Odjavite se
	</div></a>

	<div class="stranica">
		<div class="vrh">
			<h1 id="glavniNaslov">Elektornski dnevnik, direktor skole</h1>
		</div>


		<div id="tabela">
			<center>
				<h1>Pregled profesora</h1>
			</center>


			<table>
				<tr>
					<th>Ime profesora</th>

					<th>Sifra profesora</th>

					<th>Predmet profesora</th>

					

					<th>Razredni odeljenju</th>
				</tr>
%for ime, predmet, sifra, razredni in podaciProfesora:
			 %if ime == "": 
			 %break 
			 
%end 
				<tr>
					<td>{{ime}}</td>

					<td>{{sifra}}</td>

					<td>{{predmet}}</td>

					<td>{{razredni}}</td>
				</tr>
				
			 %end
			</table>
		</div>


		<center>
			<h1>Upravljanje profesorima i odeljenjima</h1>
		</center>
		<br>
		<br>


		<center>
			<h2>Profesori</h2>
		</center>
		<br>


		<center>

			<div class="gornjeForme">
				<form action="/promenasifre" autocomplete="off" method="post">
					<h3>Promena sifre profesora</h3>
					<input maxlength="7" name="staraSifra" placeholder="Trenutna sifra profesora" required="" type="text"><br>
					<br>
					<button type="submit">Potvrdi</button>
				</form>
			</div>


			<div class="gornjeForme">
				<form action="/ispisprofesora" autocomplete="off" method="post">
					<h3>Ispis profesora</h3>
					<input maxlength="7" name="profesorSifra" placeholder="Sifra profesora" required="" type="text">

					<p class = potvrditi><input name="sigurno" required="" type="checkbox" style="width:auto;">Sigurno zelite da ovo uradite</p>
					<button type="submit">Potvrdi</button>
				</form>
			</div>


			<div class="gornjeForme">
				<form action="/stoprazredni" autocomplete="off" method="post">
					<h3>Prestanak razrednog</h3>
					<input maxlength="7" name="profesorSifra" placeholder="Sifra profesora" required="" type="text"><br>
					<br>
					<button type="submit">Potvrdi</button>
				</form>
			</div>
		</center>


		<center>

			<div class="formeDole">
				<form action="/novrazredni" autocomplete="off" method="post">
					<h3>Dodela razrednog</h3>
					<input maxlength="7" name="profesorSifra" placeholder="Sifra profesora" required="" type="text"><br>
					<br>
					<input maxlength="2" name="odeljenje" placeholder="Broj odeljenja: 15, 22, 36..." required="" type="text"><br>
					<br>
					<button type="submit">Potvrdi</button>
				</form>
			</div>


			<div class="formeDole">
				<form action="/dosaoprofesor" autocomplete="off" method="post">
					<h3>Upis novog profesora</h3>
					<input name="ime" placeholder="Prezime i ime profesora" required="" type="text"><br>
					<br>
					<input name="predmet" placeholder="Predmet profesora" required="" type="text"><br>
					<br>
					<button type="submit">Potvrdi</button>
				</form>
			</div>
		</center>
		<br>
		<br>

		<hr>
		<br>
		<br>


		<center>
			<h2>Odeljenja</h2>
		</center>
		<br>


		<center>
				<div class="formeOdeljenja">
					<form action="/upisatiocenu" method="post"  autocomplete="off">
		    		<h3>Upis ocene iz vladanja</h3>
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

				</div>
</center><center>
			<div class="formeOdeljenja">
				<form action="/upisatiucenika" autocomplete="off" method="post">
					<h3>Upis novog ucenika</h3>
					<input name="ime" placeholder="Prezime i ime ucenika" required="" type="text"><br>
					<br>
					<input maxlength="2" name="odeljenje" placeholder="Broj odeljenja: 15, 22, 36..." required="" type="text"><br>
					<br>
					<button type="submit">Potvrdi</button>
				</form>
			</div>
		</center>


		<center>
			<div class="formeOdeljenja">
				<form action="/doslonovoodeljenje" autocomplete="off" method="post">
					<h3>Upis novog odeljenja</h3>
					<input maxlength="2" name="odeljenje" placeholder="Broj odeljenja: 15,22,33..." required="" type="text"><br>
					<br>

					<textarea name="spisakPredmeta" placeholder="Predmet1, Predmet2, ... , Predmetn" required=""></textarea><br>
					<br>

					<textarea name="spisakUcenika" placeholder="Prezime i ime 1, Prezime i ime 2, ... , Prezime i ime n" required=""></textarea><br>
					<br>
					<input type="submit" value="Potvrdi">
				</form>
			</div>
		</center>


		<center>
			<div class="formeOdeljenja">
				<form action="/izracunajprossek" autocomplete="off" method="post">
					<h3>Racunajte prosek</h3>


					<p>**Brise sve ostale ocene i upisuje prosecnu na njihovo mesto</p>


					<p>Vazi za odeljenje sa kojim ste se prijavili kao direktor: {{kojeOdeljenje}}</p>
					<input name="sigurno" required="" type="checkbox" style="width:auto;"> POTVRDITE<br>
					<br>
					<input type="submit" value="Potvrdi">
				</form>
			</div>
		</center>


		<center>
			<div class="formeOdeljenja">
				<form action="/odeodeljenje" autocomplete="off" method="post">
					<h3>Brisanje odeljenja</h3>


					<p>**Vazi za odeljenje sa kojim ste se prijavili kao direktor: {{kojeOdeljenje}}</p>
					<input name="sigurno" required="" type="checkbox" style="width:auto;"> POTVRDITE<br>
					<br>
					<input type="submit" value="Potvrdi">
				</form>
			</div>
		</center>
	</div>
	<br>
	<br>
	<br>
</body>
</html>
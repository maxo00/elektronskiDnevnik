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
      <h1 class="subtitle ">Direktor</h1>




<div class="tile is-ancestor">
      <div class="tile is-vertical is-7">
        <div class="tile">
          <div class="tile is-parent is-vertical">
              <p class="title notification">Pregled profesora</p><div class="content" style="max-height: 500px; overflow-y:auto;">
            <!-- TABELA PROFESORA -->
	<table class="table is-fullwidth is-hoverable">
      	<thead>
      		<tr>
      			<th>Ime profesora</th>
      			<th>Sifra profesora</th>
      			<th>Predmet profesora</th>
      			<th>Razredni</th>
      		</tr>
      	</thead>
      	<tbody>
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
      	</tbody>
      </table>
  </div>
          </div>
        </div>
      </div>
<div class="tile is-child is-vertical">
        <div class="tile">
          <div class="tile is-parent is-vertical">
              <p class="title is-3 notification">Upravljanje profesorima</p><div class="content" style="overflow-y: auto; max-height: 500px; padding: 5px;">
<div class="block">
              <form action="/promenasifre" autocomplete="off" method="post">
					<h3 class="subtitle is-5">Promena sifre profesora</h3>
					<input maxlength="7" name="staraSifra" placeholder="Trenutna sifra profesora" required class="input" type="text"><br>
					<br>
					<button type="submit" class="button">Potvrdi</button>
				</form></div>
<hr>	
				<div class="block">
              <form action="/novrazredni" autocomplete="off" method="post">
					<h3>Dodela razrednog</h3>
					<input maxlength="7" name="profesorSifra" placeholder="Sifra profesora" required="" type="text" class="input"><br>
					<br>
					<input maxlength="2" name="odeljenje" placeholder="Broj odeljenja: 15, 22, 36..." required="" type="text" class="input"><br>
					<br>
					<button type="submit" class="button">Potvrdi</button>
				</form></div><hr>	
				<div class="block">
              <form action="/stoprazredni" autocomplete="off" method="post">
					<h3>Prestanak razrednog</h3>
					<input maxlength="7" name="profesorSifra" placeholder="Sifra profesora" required="" type="text" class="input"><br>
					<br>
					<button type="submit" class="button">Potvrdi</button>
				</form></div><hr>	
				<div class="block">
              <form action="/dosaoprofesor" autocomplete="off" method="post">
					<h3>Upis novog profesora</h3>
					<input name="ime" placeholder="Prezime i ime profesora" required="" type="text" class="input"><br>
					<br>
					<input name="predmet" placeholder="Predmet profesora" required="" type="text" class="input"><br>
					<br>
					<button type="submit" class="button">Potvrdi</button>
				</form></div><hr>	
				<div class="block">
              <form action="/ispisprofesora" autocomplete="off" method="post">
					<h3>Ispis profesora</h3>
					<input maxlength="7" name="profesorSifra" placeholder="Sifra profesora" required="" type="text" class="input">
		<br>	<br>	
					<label class="checkbox">
  						<input type="checkbox" required>  Sigurno zelite ovo da uradite 
  					</label><br>	<br>	
					<button type="submit" class="button">Potvrdi</button>
				</form></div>
            </div>
			</div>
        </div>
</div>
</div>
<div class="block" style="margin-top: 30px;">
	<div class="columns is-mobile is-centered">

  <div class="column is-half is-narrow"><p class="title is-3 notification">Upravljanje odeljenjima</p>
  	<div class="content" style="max-height: 450px; overflow-y: auto;">
   <form action="/upisatiocenu" method="post"  autocomplete="off">
		    		<h3>Upis ocene iz vladanja</h3>
		    		<input type="text" name="ime" placeholder="Prezime i ime ucenika" required="" class="input"><br><br>
					Ocena: <select name="ocena" class="select is-small">
						<option value="1">1</option>
						<option value="2">2</option>
						<option value="3">3</option>
						<option value="4">4</option>
						<option value="5">5</option>
					</select><br><br>
					<textarea name="beleskaOcene" placeholder="Beleska za ocenu" required class="textarea"></textarea><br><br>
					<button type="submit" class="button">Potvrdi</button>

		    	</form>
		<hr>
		<form action="/upisatiucenika" autocomplete="off" method="post">
					<h3>Upis novog ucenika</h3>
					<input name="ime" placeholder="Prezime i ime ucenika" required="" type="text" class="input"><br>
					<br>
					<input maxlength="2" name="odeljenje" placeholder="Broj odeljenja: 15, 22, 36..." required="" type="text" class="input"><br>
					<br>
					<button type="submit" class="button">Potvrdi</button>
				</form>
<hr>

<form action="/doslonovoodeljenje" autocomplete="off" method="post">
					<h3>Upis novog odeljenja</h3>
					<input maxlength="2" name="odeljenje" placeholder="Broj odeljenja: 15,22,33..." required="" type="text" class="input"><br>
					<br>

					<textarea name="spisakPredmeta" placeholder="Predmet1, Predmet2, ... , Predmetn" required="" class="textarea"></textarea><br>
					<br>

					<textarea name="spisakUcenika" placeholder="Prezime i ime 1, Prezime i ime 2, ... , Prezime i ime n" required="" class="textarea"></textarea><br>
					<br>
					<input type="submit" class="button" value="Potvrdi">
				</form>
<hr>

<form action="/izracunajprossek" autocomplete="off" method="post">
					<h3>Racunajte prosek</h3>


					<p>**Brise sve ostale ocene i upisuje prosecnu na njihovo mesto</p>


					<p>Vazi za odeljenje sa kojim ste se prijavili kao direktor: {{kojeOdeljenje}}</p>
					<input name="sigurno" required="" type="checkbox" class="checkbox"> POTVRDITE<br>
					<br>
					<input type="submit" value="Potvrdi" class="button">
				</form>

				<hr>

				<form action="/odeodeljenje" autocomplete="off" method="post">
					<h3>Brisanje odeljenja</h3>


					<p>**Vazi za odeljenje sa kojim ste se prijavili kao direktor: {{kojeOdeljenje}}</p>
					<input name="sigurno" required="" type="checkbox" class="checkbox" style="width:auto;"> POTVRDITE<br>
					<br>
					<input type="submit" value="Potvrdi" class="button">
				</form>




		</div>
</div>
  </div>
</div>








</div>



<br><br><br><br>

		</div>
    </section>
  </body>
</html>
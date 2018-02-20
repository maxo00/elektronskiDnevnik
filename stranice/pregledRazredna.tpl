<!DOCTYPE html>
<html>
<head>
	<meta name="author" content="Marko Maksimovic">
	<title>Elektronski dnenik</title>
	<link rel="stylesheet" type="text/css" href="../static/pregledRazredna.css">
	<script>
		function zatvoritiProzor() {
  if (confirm("Zatvorite stranicu")) {
    close();
  }
}
	</script>
</head>
<body>
	<a href="javascript:zatvoritiProzor();">
	<div id="odjava" >
		Zatvorite stranicu
	</div></a>

	<div class="stranica">
		<div class="vrh">
			<h1 id="glavniNaslov">Razredni staresina, pregled odeljenja</h1>
		</div>
<center><h1>Pregled vaseg odeljenja</h1></center>
<div id="pregledanje">
<table>
	<tr>
		%for predmet in predmeti:
		%if predmet == "":
		%continue
		%end
		%if predmet == "imeUcenika":
		<th>Ime ucenika</th>
		%continue
		%end
		%if predmet == "sifraUcenika":
		<th>Sifra ucenika</th>
		%continue
		%end
		%predmet = str(predmet.title())
		<th>{{predmet}}</th>
		%end
	</tr>
	%for ucenik in ucenici:
	<tr>
	%for podaci in ucenik:
	<td>
		%if podaci == "" or podaci is None:
		/
		%else: 
		{{podaci}}
		%end
	</td>
	%end
</tr>
	%end
</table>
</div>
<center><h2>Pregled izostanaka</h2></center>
<center>
<div class="tabela">
<table>
	<tr>
	<th>Ime ucenika</th>
	<th>Ime profesora</th>
	<th>Datum</th>
	<th>Opravdao</th>
	<th>Sifra izostanka</th>
</tr>
%for imeUcenika, imeProfesora, datum, opravdano, sifra in izostanciUcenika:
<tr>
	%if imeUcenika=="Odeljenje nema izostanke" or imeUcenika is None:
	<td colspan="5">Odeljenje nema izostanke</td>
	%break
	%end
	<td>{{imeUcenika.title()}}</td>
	<td>{{imeProfesora}}</td>
	<td>{{datum}}</td>
	<td>{{opravdano}}</td>
	<td>{{sifra}}</td>
	</tr>
	%end
</table>
</div>
</center>

<center><h2>Pregled napomena</h2></center>
<center>
	
<div class="tabela">
<table>
	<tr>
	<th>Ime ucenika</th>
	<th>Ime profesora</th>
	<th>Datum</th>
	<th>Razlog</th>
</tr>
	%for ime, profesor, datum, razlog in napomene:
	<tr>
	%if ime == "Odeljenje nema napomena":
	<td colspan="4">Odeljenje nema napomena</td>
	%break
	%end
	<td>{{ime.title()}}</td>
	<td>{{profesor.title()}}</td>
	<td>{{datum}}</td>
	<td>{{razlog}}</td>
</tr>
	%end

</table>
</div>



</center>

<br><br><hr><br><br>
<center><h2>Pravadanje izostanaka</h2></center><center><div class="forme">
<form action="/pravdanjedana" autocomplete="off" method="post">
	<h3>Pravdanje jednog dana</h3>
	<input maxlength="7" minlength="7" name="sifraUcenika" placeholder="Sifra ucenika" required type="text"><br>
					<br>
	<input maxlength="6" minlength="6" name="datum" placeholder="Datum, unesite u formatu: 25.04." required type="text"><br>
					<br>
					<button type="submit">Potvrdi</button>

</form></center></div><center><div class="forme">
<form action="/pravdanjejedan" autocomplete="off" method="post">
	<h3>Pravdanje jednog izostanka</h3>
	
	<input maxlength="10" minlength="10" name="sifraIzostanka" placeholder="Sifra izostanka" required type="text"><br>
					<br>
					<button type="submit">Potvrdi</button>
</form>
</div>
</center>


<br>
<br>
<br>
<br>
<br>
</body>
</html>
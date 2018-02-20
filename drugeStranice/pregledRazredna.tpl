<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Elektronski dnevnik</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.6.2/css/bulma.min.css">
    <script>
		function zatvoritiProzor() {
  if (confirm("Zatvorite stranicu")) {
    close();
  }
}
	</script>
  </head>
  <body>
  <section class="section">
    <div class="container">
	<a href="/">
	<a href="javascript:zatvoritiProzor();">
	<div class="button is-primary is-medium" style="position: fixed; top: 10px; right: 10px; z-index: 99999;">
		Zatvorite stranicu
	</div></a>

      <h1 class="title is-1">Elektronski dnevnik</h1>
      <h1 class="subtitle ">Razredni staresina</h1>




<div class="tile is-ancestor">
      <div class="tile is-vertical is-12">
        <div class="tile">
          <div class="tile is-parent is-vertical" style="overflow-x: auto;">
              <p class="title notification">Pregled svog odeljenja</p><div class="content" style="max-height: 500px; overflow-y:auto;">
            <!-- TABELA PROFESORA -->
	<table class="table is-fullwidth is-hoverable">
      	<thead>
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
      	</thead>
      	<tbody>
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
      	</tbody>
      </table>
  </div>
          </div>
        </div>
      </div>
</div>

<div class="tile is-ancestor">
      <div class="tile is-vertical is-12">
        <div class="tile">
          <div class="tile is-parent is-vertical" style="overflow-x: auto;">
              <p class="title notification">Pregled napomena</p><div class="content" style="max-height: 500px; overflow-y:auto;">
            <!-- TABELA PROFESORA -->
	<table class="table is-fullwidth is-hoverable">
      	<thead>
      		<tr>
	<th>Ime ucenika</th>
	<th>Ime profesora</th>
	<th>Datum</th>
	<th>Razlog</th>
</tr>

      	</thead>
      	<tbody>	
<tr>
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
      	</tbody>
      </table>
  </div>
          </div>
        </div>
      </div>
</div>

<div class="tile is-ancestor">
      <div class="tile is-vertical is-12">
        <div class="tile">
          <div class="tile is-parent is-vertical" style="overflow-x: auto;">
              <p class="title notification">Pregled izostanaka</p><div class="content" style="max-height: 500px; overflow-y:auto;">
            <!-- TABELA PROFESORA -->
	<table class="table is-fullwidth is-hoverable">
      	<thead>
      		<tr>
      			<th>Ime ucenika</th>
	<th>Ime profesora</th>
	<th>Datum</th>
	<th>Opravdao</th>
	<th>Sifra izostanka</th>
</tr>

      	</thead>
      	<tbody>	
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
      	</tbody>
      </table>
  </div>
          </div>
        </div>
      </div>
</div>






</div>


<div class="block" style="margin-top: 30px;">
	<div class="columns is-mobile is-centered">

  <div class="column is-centered is-auto is-4"><p class="title is-3 notification">Pravdanje izostanaka</p>
  	<div class="content" style="max-height: 450px; overflow-y: auto;">
  <form action="/pravdanjedana" autocomplete="off" method="post">
	<h3 class="is-3">Pravdanje jednog dana</h3>
	<input maxlength="7" minlength="7" name="sifraUcenika" placeholder="Sifra ucenika" required type="text" class="input"><br>
					<br>
	<input maxlength="6" minlength="6" name="datum" placeholder="Datum, unesite u formatu: 25.04." required type="text" class="input"><br>
					<br>
					<button type="submit" class="button">Potvrdi</button>

</form>
<hr>
<form action="/pravdanjejedan" autocomplete="off" method="post">
	<h3 class="is-3">Pravdanje jednog izostanka</h3>
	
	<input maxlength="10" minlength="10" name="sifraIzostanka" placeholder="Sifra izostanka" required type="text" class="input"><br>
					<br>
					<button type="submit" class="button">Potvrdi</button>
</form>


		</div>
</div>
  </div>
</div>



<br><br><br><br>

		</div>
    </section>
  </body>
</html>
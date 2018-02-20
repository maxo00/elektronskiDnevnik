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
      <h1 class="subtitle ">Ucenik</h1>


     
<div class="tile is-ancestor">
      <div class="tile is-vertical is-7">
        <div class="tile">
          <div class="tile is-parent is-vertical">
              <p class="title notification">Pregled ucenika</p><div class="content" style="max-height: 500px; overflow-y:auto; padding: 10px;">

	
				%for predmet, ocena in pregleanjeOcena:
					  <p><i>
					  	{{predmet}}: </i> {{ocena}}
					  </p>
					%end

  </div>
          </div>
        </div>
      </div>
<div class="tile is-child is-vertical">
        <div class="tile">
          <div class="tile is-parent is-vertical">
              <p class="title is-3 notification">Pregled kontrolnih</p><div class="content" style="overflow-y: auto; max-height: 500px; padding: 5px;">
%for predmet, datum in kontrolni:
					%if predmet=="Nema zakazanih kontrolnih":
					<p>Nema zakazanih kontrolnih</p>
					%break
					%end
					  <p>
					  Predmet: {{predmet}}<br>Datum: {{datum}} 
					  </p><hr>
					%end

            </div>
			</div>
        </div>
</div>




		</div>
		<div class="tile is-ancestor">
      <div class="tile is-vertical is-5">
        <div class="tile">
          <div class="tile is-parent is-vertical">
              <p class="title notification">Poslednje ocene</p><div class="content" style="max-height: 500px; overflow-y:auto; padding: 10px;">

	%for beleska, ocena, ime, profesor, predmet, datum in gledanjeBeleski:
					%if beleska=="":
					<p>Ucenik nema unetih ocena</p>
					%break
					%end
					  <p>
					  {{predmet}}, {{ocena}}	<br>	{{beleska}} <br> {{ime}} , {{profesor}} <br>{{datum}} 
					  </p><hr>
					%end

  </div>
          </div>
        </div>
      </div>
<div class="tile is-child is-vertical">
        <div class="tile">
          <div class="tile is-parent is-vertical">
              <p class="title is-3 notification">Pregled izostanaka</p><div class="content" style="overflow-y: auto; max-height: 500px; padding: 5px;">
%for imeUcenika, imeProfesora, datum, opravdano in izostanciUcenika:
	%if imeUcenika=="Ucenik nema izostanke":
	<p>Ucenik nema izostanke</p>
	%break
	%end
	<p>
		{{imeProfesora}}<br>{{opravdano}}<br>{{datum}}
		<hr>
		  	</p>
		  	%end

            </div>
			</div>
        </div>
</div>
		</div>
		<div class="tile is-ancestor">
      <div class="tile is-vertical is-fullwidth">
        <div class="tile">
          <div class="tile is-parent is-vertical">
              <p class="title notification">Pregled napomena</p><div class="content" style="max-height: 500px; overflow-y:auto; padding: 10px;">
%for imeUcenika, imeProfesora, razlog, datum in listaNapomeni:
	%if imeUcenika=="Ucenik nije u napomenama":
	<p>Ucenik nije upisivan u napomene</p>
	%break
	%end
	<p>
		{{imeProfesora}}<br>{{razlog}}<br>{{datum}}
		<hr>
		  	</p>
	%end

  </div>
          </div>
        </div>
      </div>
		</div>

</div>


	</div>
    </section>
  </body>
</html>
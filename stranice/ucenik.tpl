<!DOCTYPE html>
<html>
<head>
	<meta name="author" content="Marko Maksimovic">
	<title>Pregled dnevnika</title>
	<link rel="stylesheet" type="text/css" href="../static/ucenik.css">
</head>
<body>

<div class="stranica">


		  <div class="vrh">
		  	<h1 id="glavniNaslov">Pregled elektronskog dnevnika</h1>

		  </div>


		  <div class="stranaZaPredmete">
		    <h2>Pregled predmeta</h2>
	
				%for predmet, ocena in pregleanjeOcena:
					  <p><i>
					  	{{predmet}}: </i> {{ocena}}
					  </p>
					%end
		</div>


		  <div class="upisaneOcene">
		 	<h2>Pregled poslednjih ocena</h2>
			<div class="deliGore">
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
		<hr>
		 	<h2>Najavljenji kontrolni</h2>
		 	<div class="deliDole">
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


	<div class="napomeneIzostanci">
    <h2>Pregled izostanaka</h2>
<div class="deliGore">
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


<hr>

	<h2>Pregled napomena</h2>
	<div class="deliDole">
	%for imeUcenika, imeProfesora, razlog, datum in listaNapomeni:
	%if imeUcenika=="Ucenik nije u napomenama":
	<p>Ucenik nije upisivan u napomene</p>
	%break
	%end
	<p>
		{{imeProfesora}}<br>Razlog: {{razlog}}<br>{{datum}}
		<hr>
		  	</p>
		  	%end

		</div>

</div>
</div>
		


</body>
</html>
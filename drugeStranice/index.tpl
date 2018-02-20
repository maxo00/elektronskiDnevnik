<!DOCTYPE html>
<html>
<head>
	<meta name="author" content="Marko Maksimovic">
	<title>Sajt skole</title>
	<link href="..\static\index.css" rel="stylesheet" type="text/css">
	<link href="..\static\bulma.css" rel="stylesheet" type="text/css">
</head>
<body>

	<div class="deljenje levaStrana">
	  <div class="sredinaDela">
	    
	    <form action="/ucenik" method="post" autocomplete="off">
	    	<h2 class="title is-3">Ucenici</h2>
	    	<input type="text" name="sifraUcenika" placeholder="Sifra ucenika" minlength="7" maxlength="7" class="input"><br><br>
	    	<input type="text" name="odeljenje" placeholder="Broj odeljenja: 11, 36, 55..."  minlength="2" maxlength="2" class="input"><br><br>
	    	<button type="submit" class="button">Potvrdi</button>
	    </form>
	  </div>
	</div>

	<div class="deljenje desnaStrana">
	  <div class="sredinaDela">
	   
	    <form action="/profesorProvera" method="post" autocomplete="off">
	    	 <h2 class="title is-3">Profesori</h2>
	    	<input type="password" name="sifraProfesora" placeholder="Sifra profesora" minlength="7" maxlength="7" class="input"><br><br>
	    	<input type="text" name="odeljenje" placeholder="Broj odeljenja: 11, 36, 55..." minlength="2" maxlength="2" class="input"><br><br>
	    	<button type="submit" class="button">Potvrdi</button>

	    </form>
	  </div>
	</div>

</body>
</html>
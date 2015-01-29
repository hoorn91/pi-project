<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset=utf8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
  <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
    <title>ROMS</title>
</head>

<body>
    <h3>ROMS</h3>
    <hr>
<?php
function files($dir){
	$dh  = opendir($dir);
	while (false !== ($filename = readdir($dh))) {
	    $files[] = $filename;
	}
	while (false !== ($filename = readdir($dh))) {
	    $files[] = $filename;
	}

	foreach($files as $file) {
	    if(strpos($file, '.') !== (int) 0) {
	        echo $file;
	        echo"<br>";
	    }
	}
}
?>


<ul class="nav nav-tabs">
  <li class="active"><a href="#home" data-toggle="tab">Home</a></li>
  <li><a href="#NES" data-toggle="tab">NES</a></li>
  <li><a href="#SNES" data-toggle="tab">SNES</a></li>
</ul>
<div id="myTabContent" class="tab-content">
  <div class="tab-pane fade active in" id="home">
    <p>Navigate through the different consoles</p>
  </div>
  <div class="tab-pane fade" id="NES">
  	<p>
    <?php
	$path = "/home/pi/RetroPie/roms/nes";
	files($path);
	$files = "";
	?>
	</p>
  </div>
  <div class="tab-pane fade" id="SNES">
    <p>
    <?php
	$path = "/home/pi/RetroPie/roms/snes";
	files($path);
	$files = "";
	?>
	</p>
  </div>
</div>

</body>

</html>

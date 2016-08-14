<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>Gallary</title>
		<link href="gallary.css" rel="stylesheet" type="text/css"  media="all" />
	</head>
	<body>

		<h2>HearthStone</h2>

		<?php
			include 'db.php';
			$conn = dbConnect();

			$sql = "SELECT * FROM HearthStones WHERE view > 100 ORDER BY view DESC;";
			$result = $conn->query($sql);
			while($row = $result->fetch_assoc()) {			
		?> 		
		
		<div class="responsive">
		  <div class="img">
		    <a target="_blank" href=<?= $row['link']?>>
		      <img src=<?= $row['img_url']?>>
		    </a>
		    <div class="desc"><?= $row['title']?></div>
		  </div>
		</div>

		<?php
			}//while end
		?>

	</body>
</html>
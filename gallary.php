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
		 	<div class="content">
		    	<a target="_blank" href=<?= $row['link']?>>
		     		<img src=<?= $row['img_url']?>>
		    		<div class="text">
						<div class="title"><?= $row['title']?></div>
					    <div class="cate"><?= $row['web']?></div>
					</div>
					<div class="text">
						<div class="zhubo"><?= $row['zhubo']?></div>
					    <div class="view"><?= $row['view']?></div>
					</div>		     		
		   		</a>
			</div>
		</div>

		<?php
			}//while end
		?>

	</body>
</html>
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>直播信息汇总（测试版）</title>
		<link href="style.css" rel="stylesheet" type="text/css"  media="all" />
	</head>
	<body>
		<h2>炉石传说直播汇总</h2>

		<?php
			include 'db.php';
			$conn = dbConnect();
		?> 
		<!-- 显示直播信息 -->
		<div class="right-content">
			<?php
				$sql = "SELECT * FROM HearthStones ORDER BY view DESC;";
				$result = $conn->query($sql);
				while($row = $result->fetch_assoc()) {
			?>
		    <div class="content-grid">
		    	<a href=<?= $row['link']?> target="_blank" title="name">
		    		<img src=<?= $row['img_url']?>/>
					<div class="title">
				        <?= $row['title']?>
				    </div>
				    <div class="cate">
				        炉石传说
				    </div>
					<div class="zhubo">
				        <?= $row['zhubo']?>
				    </div>
				    <div class="view">
				        <?= $row['view']?>
				    </div> 
			    </a>
		    </div>
			<?php
				}//while end
			?>
		</div>
		
	</body>
</html>
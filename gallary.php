<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>直播信息汇总（测试版）</title>
		<link href="gallary.css" rel="stylesheet" type="text/css"  media="all" />
	</head>
	<body>
		<!---start-header-->
		<div class="header">
			<!---start-logo-->
			<div class="logo">
				<a href="gallary.php"><img src="images/logo_a.png" title="Live is on"></a>
			</div>
			<!---End-logo-->
			<!---start-top-menu-search-->
			<div class="top-menu">
				<div class="top-nav">
					<ul>
						<li><a href="gallary.php">首页</a></li>
						<li><a href="#">全部直播</a></li>
						<li><a href="#">分类</a></li>
						<li><a href="#">联系我们</a></li>
					</ul>
				</div>
			</div>
			<!---End-top-menu-search-->
		</div>
		<!---End-header-->
		



		<!-- google translate -->
<!-- 		<div id="google_translate_element"></div><script type="text/javascript">
		function googleTranslateElementInit() {
		  new google.translate.TranslateElement({pageLanguage: 'zh-CN', includedLanguages: 'en,es,ja,ko,zh-CN,zh-TW', layout: google.translate.TranslateElement.InlineLayout.SIMPLE}, 'google_translate_element');
		}
		</script><script type="text/javascript" src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>
 -->
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
		    		<div class="image-container">
		     			<img src=<?= $row['img_url']?>>
		     		</div>	
		    		<div class="text">
						<div class="title"><?= $row['title']?></div>
					    <div class="web"><?= $row['web']?></div>
					</div>
					<div class="text">
						<div class="zhubo"><?= $row['zhubo']?></div>
					    <div class="view">
					    	<?php 
			                    $i = $row['view'];
			                    if ($i >= 10000) {
			                        echo round(($i/10000),1).'万';
			                    } else {
			                        echo $i;
			                    }
					    	?>
					    </div>
					</div>		     		
		   		</a>
			</div>
		</div>

		<?php
			}//while end
		?>

	</body>
</html>
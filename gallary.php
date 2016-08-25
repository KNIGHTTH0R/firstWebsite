<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>直播信息汇总（测试版）</title>
		<link href="gallary.css" rel="stylesheet" type="text/css"  media="all" />
	</head>
	<body>
		<!-- initial -->
		<?php
			include 'db.php';
			$conn = dbConnect();
			$cate = $_GET["cate"];
			// default value
			if ($cate == "") {
				$cate = "hs";
			}
		?>		
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
						<li><a href="#">首页</a></li>
						<li><a href="#">全部直播</a></li>
						<li><a href="#">分类</a></li>
						<li><a href="#">联系我们</a></li>
					</ul>
				</div>
			</div>
			<!---End-top-menu-search-->
			<!-- google translate -->
	        <div class="translate">
		        <div id="google_translate_element"></div><script type="text/javascript">
				function googleTranslateElementInit() {
				  new google.translate.TranslateElement({pageLanguage: 'zh-CN'}, 'google_translate_element');
				}
				</script><script type="text/javascript" src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script> 
		    </div>
		</div>
		<!---End-header-->
		<div class="top-blank"></div>

		<!-- Left sidebar -->
 		<div class="sidebar">
	    	<ul>
		        <li><a href="?cate=hs"
		        	<?php
		        		if ($cate == "hs") {
		        			echo " style='background-color:#555;'"
		        		}
		        	?>
		        	>炉石传说</a></li>
		        <li><a href="?cate=lol">LOL</a></li>
		        <li><a href="?cate=dota">Dota</a></li>
		        <li><a href="?cate=ow">守望先锋</a></li>
		        <li><a href="?cate=sc">星际争霸</a></li>
		        <li><a href="?cate=dnf">DNF</a></li>
		        <li><a href=""><?= $cate?></a></li>
		    </ul>
 		</div>

 		<!-- Right main page -->
 		<div class="main">

		<?php
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
		</div>
		<!--End main page-->

	</body>
</html>
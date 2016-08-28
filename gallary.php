<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>直播信息汇总（测试版）</title>
		<link href="gallary.css" rel="stylesheet" type="text/css"  media="all" />
		<link rel="shortcut icon" href="favicon.ico">
	</head>
	<body>
		<!-- initial -->
		<?php
			// google analytics
			include_once("analyticstracking.php");
			include 'db.php';
			$conn = dbConnect();
			$cate = $_GET["cate"];
			// default value
			if ($cate == "") {
				$cate = "hs";
			}
			$cates=array("hs","lol","dota","ow","sc","dnf");
			$names=array("炉石传说","LOL","Dota","守望先锋","星际争霸","DNF");
			$webs=array("douyu"=>"斗鱼","huya"=>"虎牙","panda"=>"熊猫","zhanqi"=>"战旗","quanmin"=>"全民","huomao"=>"火猫","longzhu"=>"龙珠");
		?>		
		<!---start-header-->
		<div class="header">
			<!---start-logo-->
			<div class="logo">
				<a href=""><img src="images/logo_a.png" title="Live is on"></a>
			</div>
			<!---End-logo-->
			<!---start-top-menu-search-->
			<div class="top-menu">
				<div class="top-nav">
					<ul>
						<li><a href="">首页</a></li>
						<li><a href="?cate='hot'">热门直播</a></li>
						<li><a href="about.html">关于本站</a></li>
						<li><a href="contact.html">联系我们</a></li>
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
	    		<!-- use php to write a list -->
	    		<?php
		    		for ($i=0; $i<count($cates); $i++) {  
		    			echo '<li><a href="?cate='.$cates[$i].'"';
		        		if ($cate == $cates[$i]) {
		        			echo " style='color:#eee; background-color:#2a5caa;'";
		        		}
		        		echo '>'.$names[$i].'</a></li>';
		        	}
		        ?>
		    </ul>
 		</div>

 		<!-- Right main page -->
 		<div class="main">

		<?php
			$sql = "";
			if ($cate == "hot") {
				$sql = "SELECT * FROM HearthStones WHERE view > 50000 ORDER BY view DESC;";
			}
			else {
				$sql = "SELECT * FROM HearthStones WHERE cate ='".$cate."' ORDER BY view DESC;";
			}			
			$result = $conn->query($sql);
			while($row = $result->fetch_assoc()) {			
		?>

		<div class="responsive">
		 	<div class="content">
		    	<a target="_blank" href=<?= $row['link']?> title=<?='"'.$row['title'].'"'?>>
		    		<div class="image-container">
		     			<img src=<?= $row['img_url']?> onerror="this.src='images/blank.png'">
		     		</div>	
		    		<div class="text">
						<div class="title"><?= $row['title']?></div>
					    <div class="web"><?= $webs[$row['web']]?></div>
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
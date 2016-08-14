<?php
function dbConnect() {
	$conn = new mysqli("localhost", "root", "root");
	if ($conn->connect_error) {
	    die("Connection failed: " . $conn->connect_error);
	    return false;
	}
	// echo "Server connected successfully<br>";

	mysqli_set_charset($conn,"utf8");

	$sql = "USE zhibo";
	if ($conn->query($sql) == TRUE) {
	    // echo "Database connected successfully<br>";
	} else {
	    echo "Error connecting database: " . $conn->error . "<br>";
	    return false;
	}
	return $conn;
}

// function createTableAlbum($conn) {
// 	$sql = "CREATE TABLE album (
// 		id INT(6) UNSIGNED AUTO_INCREMENT, 
// 		name VARCHAR(25) NOT NULL,
// 		createTime TIMESTAMP,
// 		lastModifyTime TIMESTAMP,
// 		PRIMARY KEY (id)
// 	)";

// 	if ($conn->query($sql) == TRUE) {
// 	    echo "Table album created successfully<br>";
// 	} else {
// 	    echo "Error creating table: " . $conn->error . "<br>";
// 	}
// }

// function createTableImage($conn) {
// 	$sql = "CREATE TABLE image (
// 		imageID INT UNSIGNED AUTO_INCREMENT,
// 		albumID INT(6) UNSIGNED NOT NULL,
// 		name VARCHAR(25) NOT NULL,
// 		paths VARCHAR(50) NOT NULL,
// 		local BOOLEAN,
// 		time TIMESTAMP,
// 		PRIMARY KEY (imageID),
// 		FOREIGN KEY (albumID) REFERENCES album(id)
// 	)";

// 	if ($conn->query($sql) == TRUE) {
// 	    echo "Table image created successfully<br>";
// 	} else {
// 	    echo "Error creating table: " . $conn->error . "<br>";
// 	}
// }

// function insertAlbum($conn, $albumName) {
// 	$sql = "INSERT INTO album (name)
// 	VALUES ('$albumName');";
// 	if ($conn->query($sql) == TRUE) {
// 	    echo "New album created successfully<br>";
// 	} else {
// 	    echo "Error: " . $sql . "<br>" . $conn->error . "<br>";
// 	}
// }

// function insertImage($conn, $albumID, $imageName, $paths, $local) {
// 	$sql = "INSERT INTO image (albumID, name, paths, local)
// 	VALUES ($albumID, '$imageName', '$paths', $local);";
// 	if ($conn->query($sql) == TRUE) {
// 	    echo "New image inserted successfully<br>";
// 	} else {
// 	    echo "Error: " . $sql . "<br>" . $conn->error . "<br>";
// 	}
// }
?>
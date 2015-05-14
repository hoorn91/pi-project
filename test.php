<?php
$servername = "192.168.0.11";
$username = "root";
$password = "dr4g0000nball";

// Create connection
$conn = new mysqli($servername, $username, $password);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 
echo "Connected successfully";
?>
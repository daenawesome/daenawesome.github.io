<?php

function phpmotorsConnect() {
    $server = 'localhost';
    $dbname = 'phpmotors';
    $username = 'iClient';
    $password = 'E5yqy@Wx.CljnvRH';  
    $dsn= "mysql:host=$server;dbname=$dbname";
    $options = array(PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION);

    try {
        $link = new PDO($dsn, $username, $password, $options); 
        return $link;
    } catch (PDOException $e) {
        header('Location: /phpmotors/view/500.php');
        exit;
    }
}
//phpmotorsConnect();

// passwrds
// E5yqy@Wx.CljnvRH
// [vtEkQ@Z[74A9Iql
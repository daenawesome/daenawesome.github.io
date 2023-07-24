<?php
if (isset($_SESSION['loggedin']) && $_SESSION['loggedin'] === FALSE) {
    header('Location: /phpmotors');
}
?><!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP Motors Admin Page</title>
    <link href="/phpmotors/css/small.css" type="text/css" rel="stylesheet" media="screen">
    <link href="/phpmotors/css/large.css" type="text/css" rel="stylesheet" media="screen">
    <link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap" rel="stylesheet">
</head>

<body>
    <div id="wrapper">

    <header>
        <?php require $_SERVER['DOCUMENT_ROOT'] . '/phpmotors/common/header.php'; ?>
    </header>

    <nav>
        <?php echo $navList; ?>
    </nav>

    <main>
        <h1>Hello there <?php echo $_SESSION['clientData']['clientFirstname']; ?>!</h1>
        <?php if (isset($_SESSION['message'])) {
            echo $_SESSION['message'];} ?> 
        
        <p>You are logged in.</p>  
        
        <ul>
            <li>First Name: <?php echo $_SESSION['clientData']['clientFirstname']; ?></li>
            <li>Last Name: <?php echo $_SESSION['clientData']['clientLastname']; ?></li>
            <li>Email: <?php echo $_SESSION['clientData']['clientEmail']; ?></li>
        </ul>
        
        <h2>Account Management</h2>
        <p>Use this link to update account information.</p>
        <p><a href="/phpmotors/accounts/?action=update-page">Account Management</a></p>

        <?php if ($_SESSION['clientData']['clientLevel'] > 1) {echo '<h2>Inventory Management</h2>
                                                        <p>Use this link to manage the inventory.</p>
                                                        <p><a href="/phpmotors/vehicles">Vehicle Management</a></p>';} ?> 

        

    </main>
<?php require $_SERVER['DOCUMENT_ROOT'] . '/phpmotors/common/footer.php'; ?>
<?php unset($_SESSION['message']); ?>
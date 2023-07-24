<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home | PHP Motors</title>
    <link href="/phpmotors/css/small.css" type="text/css" rel="stylesheet" media="screen">
    <link href="/phpmotors/css/large.css" type="text/css" rel="stylesheet" media="screen">
    <link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap" rel="stylesheet">
</head>

<body>
    <div id="wrapper">

    <header>
        <?php include $_SERVER['DOCUMENT_ROOT'] . '/phpmotors/common/header.php'; ?>
    </header>

    <nav>
        <?php echo $navList; ?>
    </nav>

    <main>
        <div class="reg">
            <h1>Register</h1>
            

            <?php
            if (isset($message)) {
            echo $message;
            }
            ?>

        </div> 

        <form method="post" action="/phpmotors/accounts/index.php">
        <p>All fields are required.</p>
        <div class="acctname">
            <label for="fname">First Name</label><br>
            <input required type="text" name="clientFirstname" id="fname" <?php if(isset($clientFirstname)){echo "value='$clientFirstname'";}  ?> ><br>
            <label for="lname">Last Name</label><br>
            <input required type="text" name="clientLastname" id="lname" <?php if(isset($clientLastname)){echo "value='$clientLastname'";}  ?> ><br>
        </div>
        <div class="acctmail">
            <label for="email">Email</label><br>
            <input required type="email" name="clientEmail" id="email" <?php if(isset($clientEmail)){echo "value='$clientEmail'";}  ?> ><br>
        </div>
        <div class="acctpass">
            <label for="password">Password</label><br>
            <span>(Passwords must be at least 8 characters and contain at least 1 number, 1 capital letter and 1 special character.)</span><br>
            <input required type="password" name="clientPassword" id="password" pattern="(?=^.{8,}$)(?=.*\d)(?=.*\W+)(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$" ><br>
        </div>
            <br>
            <input type="submit" name="submit" id="regbtn" value="Register">
            <input type="hidden" name="action" value="register">
        </form>

    </main>

<?php include $_SERVER['DOCUMENT_ROOT'] . '/phpmotors/common/footer.php'; ?>

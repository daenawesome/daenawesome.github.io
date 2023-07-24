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
        <h1>Add A Classification</h1>  
             
        <form action="phpmotors/vehicles/index.php" method="post">
            <label for="classificationName">Enter a new classification:</label><br>
            <?php if (isset($message)) {echo $message;} ?>       
            <input  type="text" name="classificationName" id="classificationName"><br>
            <input type="submit" name="submit" id="clsbtn" value="Submit Classification">
            <input type="hidden" name="action" value="addclassificationtodb">
        </form>
        
    </main>

<?php include $_SERVER['DOCUMENT_ROOT'] . '/phpmotors/common/footer.php'; ?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?php echo $classificationName; ?> vehicles | PHP Motors, Inc.</title>
    <link href="../css/small.css" type="text/css" rel="stylesheet" media="screen">
    <link href="../css/large.css" type="text/css" rel="stylesheet" media="screen">
    <link href="../css/inventory.css" type="text/css" rel="stylesheet" media="screen">
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

        <h1>
            <?php echo $classificationName; ?> vehicles
        </h1>

            <?php if(isset($message)){echo $message; } ?>
            <?php if(isset($vehicleDisplay)){echo $vehicleDisplay;} ?>

    </main>

<?php require $_SERVER['DOCUMENT_ROOT'] . '/phpmotors/common/footer.php'; ?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP Motors Vehicle Detail</title>
    <link href="../css/small.css" type="text/css" rel="stylesheet" media="screen">
    <link href="../css/large.css" type="text/css" rel="stylesheet" media="screen">
    <link href="../css/details.css" type="text/css" rel="stylesheet" media="screen">
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

            <?php echo $vehicle; ?>

    </main>

<?php require $_SERVER['DOCUMENT_ROOT'] . '/phpmotors/common/footer.php'; ?>
<?php unset($_SESSION['message']); ?>
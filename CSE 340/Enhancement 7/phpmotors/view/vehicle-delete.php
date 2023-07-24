<?php
if($_SESSION['clientData']['clientLevel'] < 2){
 header('location: /phpmotors/');
 exit;
}
?><!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?php if(isset($invInfo['invMake'])){ 
	echo "Delete $invInfo[invMake] $invInfo[invModel]";} ?> | PHP Motors</title>
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

    <h1>
        <?php if(isset($invInfo['invMake'])){ 
	    echo "Delete $invInfo[invMake] $invInfo[invModel]";} ?> in PHP Motors?
    </h1>  

        <form action="/phpmotors/vehicles/index.php" method="post">
        <p>Confirm Vehicle Deletion.</p><p>Please Note: The delete is permanent.</p>
        

        <fieldset> 

            <label for="invMake">Make</label><br>
            <input readonly type="text" name="invMake" id="invMake" <?php
            if(isset($invInfo['invMake'])) {echo "value='$invInfo[invMake]'"; }?>><br>
            
            <label for="invModel">Model</label><br>
            <input readonly type="text" name="invModel" id="invModel" <?php
            if(isset($invInfo['invModel'])) {echo "value='$invInfo[invModel]'"; }?>><br>
           
            <label for="invDescription">Description</label><br>
            <textarea  name="invDescription" id="invDescription" readonly><?php
            if(isset($invInfo['invDescription'])) {echo $invInfo['invDescription']; }
            ?></textarea><br>
            

            <input type="submit" name="submit" id="regbtn" value="Delete Vehicle">
            
            <input type="hidden" name="action" value="deleteVehicle">
            <input type="hidden" name="invId" value="<?php if(isset($invInfo['invId'])){
            echo $invInfo['invId'];} ?>">
            
        </fieldset>
        </form>
    </main>

<?php require $_SERVER['DOCUMENT_ROOT'] . '/phpmotors/common/footer.php'; ?>
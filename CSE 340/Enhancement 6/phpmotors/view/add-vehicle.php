<?php
if (isset($_SESSION['loggedin']) && $_SESSION['loggedin'] === TRUE && $_SESSION['clientData']['clientLevel'] > 1) {
    $continue = "continue";
} else {
    header('Location: /phpmotors');
}
?><?php
//redirect if not logged in
if (isset($_SESSION['loggedin']) && $_SESSION['loggedin'] === FALSE) {
    header('Location: /phpmotors');
}

//create drop list
// $dropList = '<select name="classificationId" id="classificationId">';
// foreach ($classifications as $classification) {
//     $dropList .= "<option value='$classification[classificationId]'";
//     if(isset($classificationId)) {
//         if($classification['classificationId'] === $classificationId) {
//             $dropList .= ' selected ';
//         }
//     }
//     $dropList .= ">$classification[classificationName]</option>";
// }
// $dropList .= "</select>";


//new create drop list
$dropList = '<select name="classificationId" id="classificationId">';
$dropList .= "<option>Choose a Classification</option>";
    foreach ($classifications as $classification) {
        $dropList .= "<option value='$classification[classificationId]'";
        if (isset($classificationId) && $classification['classificationId'] === (int)$classificationId) {
                $dropList .= " selected";
            }
        $dropList .= ">$classification[classificationName]</option>";
}
$dropList .= '</select>';

?><!DOCTYPE html>
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

        <h1>Add A Vehicle</h1>  

        <form action="phpmotors/vehicles/index.php" method="post">
        <p>Note: all fields are required.</p><br>
        <?php if (isset($message)) {echo $message;} ?><br>     
            <label>Classification</label><br>
            <?php echo $dropList; ?><br>
            <label for="invMake">Make</label><br>
            <input required type="text" name="invMake" id="invMake" <?php if(isset($invMake)){echo "value='$invMake'";}  ?> ><br>
            <label for="invModel">Model</label><br>
            <input required type="text" name="invModel" id="invModel" <?php if(isset($invModel)){echo "value='$invModel'";}  ?> ><br>
            <label for="invDescription">Description</label><br>
            <textarea  name="invDescription" id="invDescription"><?php if(isset($invDescription)){echo $invDescription;}?></textarea><br>
            <label for="invImage">Image Path</label><br>        
            <input required type="text" name="invImage" value="C:\xampp\htdocs\phpmotors\images\no-image.png" id="invImage" <?php if(isset($invImage)){echo "value='$invImage'";}  ?> ><br>
            <label for="invThumbnail">Thumbnail Path</label><br>
            <input required type="text" name="invThumbnail" value="C:\xampp\htdocs\phpmotors\images\no-image.png" id="invThumbnail" <?php if(isset($invThumbnail)){echo "value='$invThumbnail'";}  ?> ><br>
            <label for="invPrice">Price</label><br>        
            <input required type="text" name="invPrice" id="invPrice" pattern="\d+(\.\d{2})?" <?php if(isset($invPrice)){echo "value='$invPrice'";}  ?> ><br>
            <label for="invStock">Quantity in Stock</label><br>
            <input required type="number" name="invStock" id="invStock" <?php if(isset($invStock)){echo "value='$invStock'";}  ?> ><br>
            <label for="invColor">Color</label><br>        
            <input required type="text" name="invColor" id="invColor" <?php if(isset($invColor)){echo "value='$invColor'";}  ?> ><br>

            <input type="submit" name="submit" id="regbtn" value="Add Vehicle">
            <input type="hidden" name="action" value="addvehicletodb">
        </form>
    </main>

<?php include $_SERVER['DOCUMENT_ROOT'] . '/phpmotors/common/footer.php'; ?>
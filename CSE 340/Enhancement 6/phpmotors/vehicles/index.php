<?php

//This is the Vehicle controller

// Create or access a Session
session_start();


// Get the database connection file
require_once '../library/connections.php';
// Get the PHP Motors model for use as needed
require_once '../model/main-model.php';
// Get the accounts model
require_once '../model/accounts-model.php';
// Get the accounts model
require_once '../model/vehicles-model.php';
// Get the functions library
require_once '../library/functions.php';

// Get the array of classifications
$classifications = getClassifications();
$navList = navBarPopulate($classifications);


// $navList = '<ul>';
// $navList .= "<li><a href='/phpmotors/index.php' title='View the PHP Motors home page'>Home</a></li>";
// foreach ($classifications as $classification) {
//  $navList .= "<li><a href='/phpmotors/index.php?action=".urlencode($classification['classificationName'])."' title='View our $classification[classificationName] product line'>$classification[classificationName]</a></li>";
// }
// $navList .= '</ul>';

//Build a drop down list using the $classifications array
// $dropList = '<select name="classificationId" id="classificationId">';
// foreach ($classifications as $classification) {
//     $dropList .= "<option value='$classification[classificationId]'>$classification[classificationName]</option>";
// }
// $dropList .= "</select>";

// Get the value from the action name - value pair
$action = filter_input(INPUT_POST, 'action');
 if ($action == NULL){
  $action = filter_input(INPUT_GET, 'action');
}

switch ($action) {
    case 'addclassification':
        include '../view/add-classification.php';
        break;

    case 'addvehicle':
        include '../view/add-vehicle.php';
        break;

    case 'addclassificationtodb':
        $classificationName = filter_input(INPUT_POST, 'classificationName');

        if (empty($classificationName)) {
            $message = '<p style="color: red;">Please provide the new class name.</p>';
            include '../view/add-classification.php';
            exit; 
        }
        $newClass = addClassification($classificationName);
        if ($newClass === 1) {
            header("location: /phpmotors/vehicles/index.php");
            exit;
        }
        else {
            $message="<p>We ran into an issue. Try again.</p>";
            include '../view/add-classification.php';
            exit;
        }
        break;

    case 'addvehicletodb':
        $invMake = filter_input(INPUT_POST, 'invMake', FILTER_SANITIZE_FULL_SPECIAL_CHARS);
        $invModel = filter_input(INPUT_POST, 'invModel', FILTER_SANITIZE_FULL_SPECIAL_CHARS);
        $invDescription = filter_input(INPUT_POST, 'invDescription', FILTER_SANITIZE_FULL_SPECIAL_CHARS);
        $invImage = filter_input(INPUT_POST, 'invImage', FILTER_SANITIZE_FULL_SPECIAL_CHARS);
        $invThumbnail = filter_input(INPUT_POST, 'invThumbnail', FILTER_SANITIZE_FULL_SPECIAL_CHARS);
        $invPrice = filter_input(INPUT_POST, 'invPrice', FILTER_SANITIZE_NUMBER_FLOAT, FILTER_FLAG_ALLOW_FRACTION);
        $invStock = filter_input(INPUT_POST, 'invStock', FILTER_SANITIZE_NUMBER_INT);
        $invColor = filter_input(INPUT_POST, 'invColor', FILTER_SANITIZE_FULL_SPECIAL_CHARS);
        $classificationId = filter_input(INPUT_POST, 'classificationId', FILTER_SANITIZE_NUMBER_INT);

        if(empty($invMake) || empty($invModel) || empty($invDescription) || empty($invImage) || empty($invThumbnail) || empty($invPrice) || empty($invStock) || empty($invColor) || empty($classificationId)){
            $message = '<br><p style="color: red";>Please provide information for all empty form fields.</p><br>';
            include '../view/add-vehicle.php';
            exit; 
        }

    // Send the data to the model
    $newVehicle = addVehicle($invMake, $invModel, $invDescription, $invImage, $invThumbnail, $invPrice, $invStock, $invColor, $classificationId);

    // Check and report the result
    if($newVehicle === 1){
        $message = "<p>Thanks for addding your vehicle. &#128515</p>";
        include '../view/add-vehicle.php';
        exit;
    } else {
        $message = "<p>Sorry, but the vehicle registration failed. Please try again.</p>";
        include '../view/add-vehicle.php';
        exit;
    }
    break; 

    default:
        include '../view/vehicle-man.php';
        break;

 }
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
        <?php require $_SERVER['DOCUMENT_ROOT'] . '/phpmotors/common/header.php'; ?>
    </header>

    <nav>
        <?php echo $navList; ?>
    </nav>

    <main>
        <h1>Welcome to PHP Motors!</h1>
        <div class="delorean">
            <img src = "/phpmotors/images/delorean.jpg" alt = "delorean picture">
                <div class="features">    
                    <h2>DMC Delorean</h2>
                    <p>3 Cup holders</p>
                    <p>Superman doors</p>
                    <p>Fuzzy dice!</p>
                </div>
            <img class = "btn" src = "/phpmotors/images/site/own_today.png" alt = "own today button">
        </div>

        <div class="content">
                <section class = "upgrades">
                    <h3>Delorean Upgrades</h3>
                    <div class="minigrid">    
                            <div class="box">
                            <div class="box1"><img src = "/phpmotors/images/upgrades/flux-cap.png" alt = "flux capaciter"></div>
                                <a href="">Flux Capacitor</a></div>
                            <div class="box">
                            <div class="box1"><img src = "/phpmotors/images/upgrades/flame.jpg" alt = "flame upgrade"></div>
                                <a href="">Flame Decals</a></div>
                            <div class="box">
                            <div class="box1"><img  src = "/phpmotors/images/upgrades/bumper_sticker.jpg" alt = "bumper sticker"></div>
                                <a href="">Bumper Stickers</a></div>
                            <div class="box">
                            <div class="box1"><img src = "/phpmotors/images/upgrades/hub-cap.jpg" alt = "hub cap"></div>
                                <a href="">Hub Caps</a></div>
                    </div> 
                </section>

                <section class = "reviews">
                    <h3>DMC Delorean Reviews</h3>
                    <ul>
                        <li>"So fast its like traveling in time." (4/5)</li>
                        <li>"Coolest ride on the road." (4/5)</li>
                        <li>"I'm feeling Marty Mcfly!" (5/5)</li>
                        <li>"The most futuristic ride of our day." (4.5/5)</li>
                        <li>"80's livin and I love it!" (5/5)</li>
                    </ul>
                </section>
        </div>
    </main>

<?php require $_SERVER['DOCUMENT_ROOT'] . '/phpmotors/common/footer.php'; ?>


            <div id="top-header">
                <img src="/phpmotors/images/site/logo.png" alt="PHP Motors Logo" id="logo">

                <!-- <?php if(isset($cookieFirstname)){
                echo "<p>&#128075 &#127942 Welcome: $cookieFirstname &#127942 &#128075</p>";
                } ?> -->


                <!-- <a href="/phpmotors/accounts?action=login-page" title="Login or Register with PHP Motors" id="acct">My Account</a> -->


                <?php if(isset($_SESSION['loggedin'])) {
                    $firstName =  $_SESSION['clientData']['clientFirstname'];
                        if ($_SESSION['loggedin'] === TRUE) 
                        {echo '<span id="acct"><a href="/phpmotors/accounts/" >&#128075; '.$firstName.'</a> | <a href="/phpmotors/accounts/index.php/?action=Logout">Logout</a></span>';}
                        } else {echo '<a id="acct" href="/phpmotors/accounts/index.php/?action=login-page">My Account</a>';
                        } ?> 

            </div>
            
            <hr>


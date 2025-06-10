<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>php</title>
</head>
<body>
    <?php
        
        $a=($_POST['ch']);
        $b=($_POST['val1']);
        $c=($_POST['val2']);
        
        switch ($a)
        {
            case 1:
                $sum=$b+$c;
                echo"the sum is: $sum";
                break;

            case 2:
                $sub=$b-$c;
                echo"the subtraction is: $sub";
                break;
            
            case 3:
                $mult=$b*$c;
                echo"the multiplication is: $mult";
                break;
     
            case 4:
                 $div=$b/$c;
                 echo"the divsion is: $div";
                 break;
            
            default:
                
                echo"invalid choice";
        }
    ?>
    
</body>
</html>
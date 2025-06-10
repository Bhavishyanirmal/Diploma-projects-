<?php
$num=($_POST['number']);
echo"multiplication table of $num:<br><bR>";
for($i=1;$i<11;$i++)
{
    $ans= $num*$i;
    echo"$num x $i =$ans<br>";
}
?>
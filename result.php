<?php
$x = $_GET['x'];
$y = $_GET['y'];
$z = $_GET['z'];

$command = escapeshellcmd("python3 process_input.py $x $y $z");
$output = shell_exec($command);
?>

<!DOCTYPE html>
<html>
<head><title>Assignment3#</title>
    <style>
        body{
            background-color: beige;
        }
    </style>
</head>
<body>
    <h1>Assignment3#</h1>
    <h2>Python Script Result</h2>
    <pre><?php echo $output; ?></pre>
</body>
</html>

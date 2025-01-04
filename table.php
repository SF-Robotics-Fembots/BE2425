<?php
$file = fopen("pressure_test.txt", "rb");

if(!$file){
	echo "file cant open";
	exit;
}

echo <<<EOF
<style>
table, td, th{
	table-layout: fixed;
	width: 100%;
	border-collapse: collapse;
	border: 3px solid black;
	text-align: center;
}
</style>
EOF;

$count = 0;
$cols = 3;
echo '<table>';

echo '<tr><th>TIME</th><th>PRESSURE</th><th>DEPTH</th></tr>';
echo '<tr>';

while(!feof($file)){
	if($count < $cols){
		$info = fgets($file);
		$parts = explode(' : ', $info);
		echo "<td>$parts[0]</td><td>$parts[1]</td><td>$parts[2]</td>";
		$count++;
	}
	else{
		$count = 0;
		echo '</tr><tr>';
	}
}
echo "</tr></table>";
fclose($file);
?>

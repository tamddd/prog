<?php
$n = (int)trim(fgets(STDIN));
$l = array_map('intval', explode(' ', trim(fgets(STDIN))));
$avg = array_sum($l) / $n;

foreach ($l as $key => $val) {
    if ($val >= $avg) {
        echo($key . "\n");
    }
}
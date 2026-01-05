<?php
$n = fgets(STDIN);

function trib($n) {
    static $memo = [];
    if (isset($memo[$n])) {
        return $memo[$n];
    }
    if ($n < 3) {
        return 1;
    } else {
        $memo[$n] = (trib($n-1) + trib($n-2) + trib($n-3)) % 10 ** 6;
        return $memo[$n];
    }
}

echo trib($n);
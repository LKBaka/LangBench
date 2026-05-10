<?php
function binomial($n, $k) {
    if ($k == 0 || $k == $n) {
        return 1;
    }
    return binomial($n-1, $k-1) + binomial($n-1, $k);
}

function bernoulli($n) {
    if ($n == 0) {
        return 1.0;
    }
    if ($n == 1) {
        return -0.5;
    }
    if ($n % 2 == 1 && $n > 1) {
        return 0.0;
    }
    
    $sum = 0.0;
    for ($k = 0; $k < $n; $k++) {
        $sum += binomial($n, $k) * bernoulli($k) / ($n - $k + 1);
    }
    return -$sum;
}

echo bernoulli(30) . "\n";
?>
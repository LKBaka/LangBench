function fib($n) {
    if ($n <= 1) return $n;
    return fib($n - 1) + fib($n - 2);
}

$n = 42;
$result = fib($n);
echo $result . "\n";

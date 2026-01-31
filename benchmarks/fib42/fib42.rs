fn fib(n: u64) -> u64 {
    if n <= 1 {
        return n;
    }
    fib(n - 1) + fib(n - 2)
}

fn main() {
    let n: u64 = 42;
    let result = fib(n);
    println!("{}", result);
}

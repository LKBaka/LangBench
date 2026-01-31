pub fn fib(n: u64) u64 {
    if (n <= 1) {
        return n;
    }
    return fib(n - 1) + fib(n - 2);
}

pub fn main() void {
    const n: u64 = 30;
    const result = fib(n);
    std.debug.print("{}\n", .{result});
}

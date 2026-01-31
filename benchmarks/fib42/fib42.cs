using System;

class Program {
    static long fib(int n) {
        if (n <= 1) return n;
        return fib(n - 1) + fib(n - 2);
    }

    static void Main() {
        int n = 42;
        long result = fib(n);
        Console.WriteLine(result);
    }
}

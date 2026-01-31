package main

func fib(n int64) int64 {
    if n <= 1 {
        return n
    }
    return fib(n-1) + fib(n-2)
}

func main() {
    n := int64(42)
    result := fib(n)
    println(result)
}

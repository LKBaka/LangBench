fun fib(n: Int): Long {
    if (n <= 1) {
        return n.toLong()
    }
    return fib(n - 1) + fib(n - 2)
}

fun main() {
    val n = 30
    val result = fib(n)
    println(result)
}

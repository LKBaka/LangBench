#include <iostream>

long long fib(int n) {
    if (n <= 1) return n;
    return fib(n - 1) + fib(n - 2);
}

int main() {
    int n = 42;
    long long result = fib(n);
    std::cout << result << std::endl;
    return 0;
}

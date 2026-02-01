int fib(int n) {
  if (n <= 1) {
    return n;
  }
  return fib(n - 1) + fib(n - 2);
}

void main() {
  int n = 30;
  int result = fib(n);
  print(result);
}

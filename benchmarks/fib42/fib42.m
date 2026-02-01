#import <Foundation/Foundation.h>

long long fib(int n) {
    if (n <= 1) {
        return n;
    }
    return fib(n - 1) + fib(n - 2);
}

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        int n = 42;
        long long result = fib(n);
        NSLog(@"%lld", result);
    }
    return 0;
}

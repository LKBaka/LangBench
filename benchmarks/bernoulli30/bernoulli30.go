package main

import "fmt"

func binomial(n, k int) int64 {
    if k == 0 || k == n {
        return 1
    }
    return binomial(n-1, k-1) + binomial(n-1, k)
}

func bernoulli(n int) float64 {
    if n == 0 {
        return 1.0
    }
    if n == 1 {
        return -0.5
    }
    if n%2 == 1 && n > 1 {
        return 0.0
    }
    
    sum := 0.0
    for k := 0; k < n; k++ {
        sum += float64(binomial(n, k)) * bernoulli(k) / float64(n-k+1)
    }
    return -sum
}

func main() {
    fmt.Println(bernoulli(30))
}
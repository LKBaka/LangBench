fn binomial(n: u32, k: u32) -> u64 {
    if k == 0 || k == n {
        return 1;
    }
    binomial(n-1, k-1) + binomial(n-1, k)
}

fn bernoulli(n: u32) -> f64 {
    if n == 0 {
        return 1.0;
    }
    if n == 1 {
        return -0.5;
    }
    if n % 2 == 1 && n > 1 {
        return 0.0;
    }
    
    let mut sum = 0.0;
    for k in 0..n {
        sum += binomial(n, k) as f64 * bernoulli(k) / (n - k + 1) as f64;
    }
    -sum
}

fn main() {
    println!("{}", bernoulli(30));
}
function binomial(n, k)
    if k == 0 or k == n then
        return 1
    end
    return binomial(n-1, k-1) + binomial(n-1, k)
end

function bernoulli(n)
    if n == 0 then
        return 1.0
    end
    if n == 1 then
        return -0.5
    end
    if n % 2 == 1 and n > 1 then
        return 0.0
    end
    
    local sum = 0.0
    for k = 0, n-1 do
        sum = sum + binomial(n, k) * bernoulli(k) / (n - k + 1)
    end
    return -sum
end

print(bernoulli(30))
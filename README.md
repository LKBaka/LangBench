# LangBench 测试报告

## 性能图表

### 性能对比

![性能对比](report/comparison.png)

### 性能趋势

![性能趋势](report/trend.png)

## fib30

| 语言 | 平均时间(μs) | 最小时间(μs) | 最大时间(μs) | 标准差(μs) | 成功率 |
|------|------------------|------------------|------------------|-----------------|--------|
| c | 2215.8 | 2141.5 | 2979.3 | 114.1 | 100.0% |
| cpp | 2701.1 | 2634.8 | 2834.8 | 40.5 | 100.0% |
| clang-c | 2746.8 | 2700.3 | 2826.2 | 28.5 | 100.0% |
| clang-cpp | 3278.0 | 3229.9 | 3351.4 | 32.4 | 100.0% |
| rust | 3349.1 | 3308.8 | 3433.0 | 27.5 | 100.0% |
| asm | 4225.2 | 4172.8 | 4555.0 | 68.3 | 100.0% |
| zig | 4398.2 | 4262.9 | 5392.1 | 207.1 | 100.0% |
| go | 5832.1 | 5428.3 | 6249.9 | 131.1 | 100.0% |
| dart | 9428.3 | 9334.1 | 9628.3 | 60.7 | 100.0% |
| luajit | 12115.9 | 8192.8 | 20448.7 | 2619.7 | 100.0% |
| java | 32082.9 | 30794.6 | 34063.6 | 749.1 | 100.0% |
| js | 35793.0 | 34890.2 | 37453.4 | 581.0 | 100.0% |
| php | 45985.7 | 43519.3 | 49146.2 | 1396.7 | 100.0% |
| lua | 105055.1 | 101466.7 | 132291.8 | 4915.4 | 100.0% |
| python | 138747.3 | 134691.5 | 231344.0 | 13761.0 | 100.0% |

## fib42

| 语言 | 平均时间(μs) | 最小时间(μs) | 最大时间(μs) | 标准差(μs) | 成功率 |
|------|------------------|------------------|------------------|-----------------|--------|
| asm | 289.1 | 267.0 | 341.7 | 22.1 | 100.0% |
| php | 40621.9 | 38785.0 | 45460.5 | 1501.2 | 100.0% |
| cpp | 442684.6 | 441699.0 | 448244.8 | 1404.3 | 100.0% |
| c | 476552.5 | 474167.3 | 480251.6 | 1757.4 | 100.0% |
| clang-c | 681043.1 | 679631.5 | 689034.7 | 2497.2 | 100.0% |
| clang-cpp | 721376.3 | 719914.2 | 726655.2 | 1479.8 | 100.0% |
| rust | 815702.3 | 814163.0 | 820544.2 | 1654.7 | 100.0% |
| java | 954814.2 | 876614.3 | 979078.5 | 22364.8 | 100.0% |
| zig | 1255528.4 | 1250077.5 | 1303072.2 | 12998.2 | 100.0% |
| go | 1563220.1 | 1557364.7 | 1576444.6 | 4084.8 | 100.0% |
| dart | 2117418.5 | 2108285.2 | 2169528.2 | 14876.7 | 100.0% |
| js | 2634412.3 | 2615875.2 | 2677445.2 | 17319.4 | 100.0% |
| luajit | 3129008.3 | 2712710.9 | 3450002.4 | 223394.5 | 100.0% |

## 总结

- **fib30**: 最快语言是 c (平均 2.2158ms)
- **fib42**: 最快语言是 asm (平均 289.1064μs)

## 失败测试详情

### fib42 - 失败

#### rust
**错误信息**: `All runs failed`

**失败详情**:
```
尝试 1: unknown
尝试 2: unknown
尝试 3: unknown
```

- 总运行次数: 50.0
- 成功次数: 0
- 失败率: 100%

#### objc
**错误信息**: `Compilation failed: gcc: error: unrecognized command-line option ‘-fobjc-arc’; did you mean ‘-fobjc-gc’?
`

#### csharp
**错误信息**: `Compilation failed: `

#### vb
**错误信息**: `Compilation failed: /bin/sh: 1: vbnc: not found
`

#### kotlin
**错误信息**: `All runs failed`

**失败详情**:
```
尝试 1: [Errno 2] No such file or directory: '/tmp/langbench/benchmark_fib42'
尝试 2: [Errno 2] No such file or directory: '/tmp/langbench/benchmark_fib42'
尝试 3: [Errno 2] No such file or directory: '/tmp/langbench/benchmark_fib42'
```

- 总运行次数: 20.0
- 成功次数: 0
- 失败率: 100%

---

### fib30 - 失败

#### csharp
**错误信息**: `Compilation failed: `

#### kotlin
**错误信息**: `All runs failed`

**失败详情**:
```
尝试 1: [Errno 2] No such file or directory: '/tmp/langbench/benchmark_fib30'
尝试 2: [Errno 2] No such file or directory: '/tmp/langbench/benchmark_fib30'
尝试 3: [Errno 2] No such file or directory: '/tmp/langbench/benchmark_fib30'
```

- 总运行次数: 50.0
- 成功次数: 0
- 失败率: 100%

#### objc
**错误信息**: `Compilation failed: gcc: error: unrecognized command-line option ‘-fobjc-arc’; did you mean ‘-fobjc-gc’?
`

#### vb
**错误信息**: `Compilation failed: /bin/sh: 1: vbnc: not found
`

---


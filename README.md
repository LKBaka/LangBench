# LangBench 测试报告

## 性能图表

### 性能对比

![性能对比](report/comparison.png)

### 性能趋势

![性能趋势](report/trend.png)

## fib30

| 语言 | 平均时间(μs) | 最小时间(μs) | 最大时间(μs) | 标准差(μs) | 成功率 |
|------|------------------|------------------|------------------|-----------------|--------|
| c | 2405.6 | 2265.2 | 2609.0 | 88.4 | 100.0% |
| cpp | 2867.2 | 2804.3 | 2956.9 | 42.0 | 100.0% |
| clang-c | 2928.5 | 2784.7 | 3757.5 | 154.2 | 100.0% |
| clang-cpp | 3429.5 | 3313.3 | 3935.1 | 131.1 | 100.0% |
| rust | 3498.3 | 3394.4 | 3911.3 | 99.2 | 100.0% |
| zig | 4330.6 | 4280.1 | 4467.7 | 33.3 | 100.0% |
| asm | 4445.9 | 4281.5 | 4676.6 | 104.8 | 100.0% |
| go | 6214.6 | 5972.9 | 6700.0 | 269.8 | 100.0% |
| typed_ant | 7118.5 | 7085.3 | 7212.2 | 30.7 | 100.0% |
| dart | 9553.8 | 9490.5 | 9649.0 | 41.2 | 100.0% |
| luajit | 12572.0 | 8163.7 | 17974.4 | 2496.4 | 100.0% |
| js | 35262.2 | 34557.8 | 39286.6 | 1048.6 | 100.0% |
| java | 36684.2 | 34912.3 | 42429.7 | 1654.3 | 100.0% |
| php | 42315.7 | 40226.2 | 45547.2 | 1364.0 | 100.0% |
| lua | 104236.9 | 99880.5 | 114744.9 | 2956.0 | 100.0% |
| python | 137370.0 | 133519.4 | 197425.6 | 8832.1 | 100.0% |

## fib42

| 语言 | 平均时间(μs) | 最小时间(μs) | 最大时间(μs) | 标准差(μs) | 成功率 |
|------|------------------|------------------|------------------|-----------------|--------|
| asm | 306.0 | 295.4 | 333.8 | 11.5 | 100.0% |
| php | 41792.5 | 40688.0 | 43981.3 | 923.5 | 100.0% |
| c | 476685.4 | 473386.3 | 479929.2 | 1654.9 | 100.0% |
| cpp | 484931.6 | 482100.0 | 489647.6 | 1593.0 | 100.0% |
| clang-c | 681449.5 | 680341.7 | 687389.6 | 1673.1 | 100.0% |
| rust | 681727.4 | 680605.9 | 684682.8 | 1231.1 | 100.0% |
| clang-cpp | 682065.7 | 681100.8 | 687694.3 | 1661.0 | 100.0% |
| java | 947494.8 | 878347.4 | 976945.2 | 24161.9 | 100.0% |
| zig | 1142644.3 | 1138476.8 | 1168911.2 | 7810.0 | 100.0% |
| go | 1433437.9 | 1431322.3 | 1439421.9 | 1884.1 | 100.0% |
| dart | 1576385.4 | 1567071.2 | 1583177.3 | 4632.0 | 100.0% |
| typed_ant | 2122054.5 | 2115150.5 | 2155890.7 | 10476.9 | 100.0% |
| luajit | 2581791.0 | 2215966.0 | 2864331.5 | 245696.3 | 100.0% |
| js | 2657718.1 | 2637782.1 | 2725523.7 | 23008.9 | 100.0% |

## bernoulli30

| 语言 | 平均时间(μs) | 最小时间(μs) | 最大时间(μs) | 标准差(μs) | 成功率 |
|------|------------------|------------------|------------------|-----------------|--------|
| asm | 308.7 | 280.1 | 406.7 | 29.8 | 100.0% |
| python | 17108.4 | 16140.0 | 22842.9 | 1278.4 | 100.0% |
| c | 2221731.1 | 2216123.3 | 2253901.5 | 6751.1 | 100.0% |
| cpp | 2279567.4 | 2272337.0 | 2305229.7 | 5094.2 | 100.0% |
| clang-cpp | 3284187.0 | 3273977.0 | 3428504.0 | 25415.5 | 100.0% |
| clang-c | 3287277.0 | 3272718.4 | 3432815.6 | 30886.5 | 100.0% |
| java | 3642430.3 | 3544955.3 | 3782007.5 | 52074.4 | 100.0% |
| rust | 3704955.4 | 3700092.6 | 3722395.4 | 4366.6 | 100.0% |
| go | 6562747.8 | 6550999.2 | 6579462.5 | 5312.0 | 100.0% |
| dart | 7641202.0 | 7630232.8 | 7678075.6 | 11058.0 | 100.0% |
| js | 12821327.6 | 12374750.9 | 15572232.7 | 653499.9 | 100.0% |
| luajit | 21227752.5 | 21184232.2 | 21387350.3 | 44947.2 | 100.0% |

## 总结

- **fib30**: 最快语言是 c (平均 2.4056ms)
- **fib42**: 最快语言是 asm (平均 305.9506μs)
- **bernoulli30**: 最快语言是 asm (平均 308.7044μs)

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

#### objc
**错误信息**: `Compilation failed: gcc: error: unrecognized command-line option ‘-fobjc-arc’; did you mean ‘-fobjc-gc’?
`

---

### fib30 - 失败

#### objc
**错误信息**: `Compilation failed: gcc: error: unrecognized command-line option ‘-fobjc-arc’; did you mean ‘-fobjc-gc’?
`

#### vb
**错误信息**: `Compilation failed: /bin/sh: 1: vbnc: not found
`

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

---

### bernoulli30 - 失败

#### vb
**错误信息**: `Compilation failed: /bin/sh: 1: vbnc: not found
`

#### php
**错误信息**: `All runs failed`

**失败详情**:
```
尝试 1: timeout
尝试 2: timeout
尝试 3: timeout
```

- 总运行次数: 4.0
- 成功次数: 0
- 失败率: 100%

#### zig
**错误信息**: `Compilation failed: benchmarks/bernoulli30/bernoulli30.zig:23:51: error: expected 1 argument, found 2
`

#### kotlin
**错误信息**: `All runs failed`

**失败详情**:
```
尝试 1: [Errno 2] No such file or directory: '/tmp/langbench/benchmark_bernoulli30'
尝试 2: [Errno 2] No such file or directory: '/tmp/langbench/benchmark_bernoulli30'
尝试 3: [Errno 2] No such file or directory: '/tmp/langbench/benchmark_bernoulli30'
```

- 总运行次数: 50.0
- 成功次数: 0
- 失败率: 100%

#### lua
**错误信息**: `All runs failed`

**失败详情**:
```
尝试 1: timeout
尝试 2: timeout
尝试 3: timeout
```

- 总运行次数: 4.0
- 成功次数: 0
- 失败率: 100%

#### csharp
**错误信息**: `Compilation failed: `

---


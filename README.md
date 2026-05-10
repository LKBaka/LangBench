# LangBench 测试报告

## 性能图表

### 性能对比

![性能对比](report/comparison.png)

### 性能趋势

![性能趋势](report/trend.png)

## fib30

| 语言 | 平均时间(μs) | 最小时间(μs) | 最大时间(μs) | 标准差(μs) | 成功率 |
|------|------------------|------------------|------------------|-----------------|--------|
| cpp | 2705.9 | 2634.0 | 2786.9 | 35.2 | 100.0% |
| clang-c | 2764.2 | 2719.9 | 2889.4 | 31.0 | 100.0% |
| c | 2872.4 | 2242.3 | 5217.6 | 825.9 | 100.0% |
| rust | 2952.3 | 2891.5 | 3403.4 | 75.4 | 100.0% |
| clang-cpp | 3348.7 | 3221.5 | 4704.0 | 209.1 | 100.0% |
| asm | 4242.2 | 4183.8 | 4362.6 | 33.7 | 100.0% |
| zig | 4734.4 | 4689.2 | 4842.5 | 26.5 | 100.0% |
| go | 5815.7 | 5635.0 | 6143.8 | 160.5 | 100.0% |
| dart | 9649.7 | 9497.4 | 9818.6 | 79.7 | 100.0% |
| luajit | 10554.0 | 7263.4 | 14203.5 | 2117.2 | 100.0% |
| java | 33756.5 | 32344.8 | 35067.3 | 586.6 | 100.0% |
| js | 37890.0 | 35926.6 | 41974.8 | 1186.7 | 100.0% |
| php | 39017.3 | 37107.0 | 40428.2 | 784.4 | 100.0% |
| python | 104560.0 | 102834.5 | 114380.8 | 1761.5 | 100.0% |
| lua | 105211.7 | 100397.3 | 109898.1 | 2591.9 | 100.0% |

## bernoulli30

| 语言 | 平均时间(μs) | 最小时间(μs) | 最大时间(μs) | 标准差(μs) | 成功率 |
|------|------------------|------------------|------------------|-----------------|--------|
| asm | 279.8 | 253.2 | 369.8 | 22.5 | 100.0% |
| python | 16434.0 | 15831.9 | 21071.9 | 748.6 | 100.0% |
| cpp | 2210761.5 | 2203973.5 | 2245495.8 | 6848.1 | 100.0% |
| c | 2223374.2 | 2215509.2 | 2262358.0 | 7930.8 | 100.0% |
| clang-c | 3295202.0 | 3272982.1 | 3484530.7 | 46828.4 | 100.0% |
| clang-cpp | 3306629.1 | 3274451.7 | 3508768.1 | 61019.3 | 100.0% |
| java | 3675809.3 | 3610393.8 | 3818502.7 | 69773.4 | 100.0% |
| rust | 3715854.0 | 3709345.8 | 3766984.5 | 9687.4 | 100.0% |
| go | 6561717.0 | 6509585.1 | 6691079.6 | 31389.0 | 100.0% |
| dart | 7648537.9 | 7637381.6 | 7689572.3 | 12373.7 | 100.0% |
| js | 12683378.6 | 12377643.1 | 13498679.4 | 226506.0 | 100.0% |
| luajit | 21261459.1 | 21214427.2 | 21375040.8 | 43772.2 | 100.0% |

## fib42

| 语言 | 平均时间(μs) | 最小时间(μs) | 最大时间(μs) | 标准差(μs) | 成功率 |
|------|------------------|------------------|------------------|-----------------|--------|
| asm | 273.7 | 258.7 | 315.7 | 16.1 | 100.0% |
| php | 38093.9 | 37049.5 | 41137.0 | 929.6 | 100.0% |
| c | 443520.7 | 442249.3 | 445068.6 | 791.4 | 100.0% |
| cpp | 463834.6 | 463227.7 | 468114.4 | 1030.2 | 100.0% |
| clang-c | 680939.2 | 680338.6 | 684820.7 | 968.7 | 100.0% |
| clang-cpp | 682505.7 | 681520.0 | 685952.2 | 1161.6 | 100.0% |
| rust | 757623.9 | 756984.7 | 759814.3 | 786.8 | 100.0% |
| java | 1136134.6 | 1134061.8 | 1144172.9 | 2615.3 | 100.0% |
| zig | 1403409.9 | 1399993.7 | 1422301.1 | 5727.8 | 100.0% |
| go | 1563092.6 | 1558663.6 | 1568274.7 | 2413.5 | 100.0% |
| dart | 2397429.0 | 2394574.6 | 2409403.6 | 4166.6 | 100.0% |
| js | 3252387.7 | 3239228.0 | 3279497.9 | 13166.5 | 100.0% |
| luajit | 3513080.2 | 3212891.3 | 3988519.0 | 281794.0 | 100.0% |

## 总结

- **fib30**: 最快语言是 cpp (平均 2.7059ms)
- **bernoulli30**: 最快语言是 asm (平均 279.7604μs)
- **fib42**: 最快语言是 asm (平均 273.6926μs)

## 失败测试详情

### fib30 - 失败

#### typed_ant
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

#### csharp
**错误信息**: `Compilation failed: `

#### objc
**错误信息**: `Compilation failed: gcc: error: unrecognized command-line option ‘-fobjc-arc’; did you mean ‘-fobjc-gc’?
`

#### vb
**错误信息**: `Compilation failed: /bin/sh: 1: vbnc: not found
`

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

#### typed_ant
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

#### vb
**错误信息**: `Compilation failed: /bin/sh: 1: vbnc: not found
`

#### objc
**错误信息**: `Compilation failed: gcc: error: unrecognized command-line option ‘-fobjc-arc’; did you mean ‘-fobjc-gc’?
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

#### csharp
**错误信息**: `Compilation failed: `

---

### bernoulli30 - 失败

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

#### vb
**错误信息**: `Compilation failed: /bin/sh: 1: vbnc: not found
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

#### csharp
**错误信息**: `Compilation failed: `

#### zig
**错误信息**: `Compilation failed: benchmarks/bernoulli30/bernoulli30.zig:23:51: error: expected 1 argument, found 2
`

---


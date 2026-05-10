# LangBench 测试报告

## 性能图表

### 性能对比

![性能对比](report/comparison.png)

### 性能趋势

![性能趋势](report/trend.png)

## fib30

| 语言 | 平均时间(μs) | 最小时间(μs) | 最大时间(μs) | 标准差(μs) | 成功率 |
|------|------------------|------------------|------------------|-----------------|--------|
| c | 2218.1 | 2152.7 | 2317.2 | 34.5 | 100.0% |
| cpp | 2715.2 | 2663.9 | 2911.8 | 41.3 | 100.0% |
| clang-c | 3051.8 | 2991.0 | 3135.2 | 34.8 | 100.0% |
| clang-cpp | 3289.7 | 3228.9 | 3475.4 | 44.3 | 100.0% |
| rust | 3299.9 | 3195.0 | 3831.1 | 136.9 | 100.0% |
| zig | 3777.7 | 3736.3 | 3868.6 | 26.7 | 100.0% |
| asm | 4278.6 | 4196.4 | 4482.3 | 66.3 | 100.0% |
| go | 6710.7 | 6406.3 | 8920.2 | 432.4 | 100.0% |
| dart | 9216.1 | 9131.7 | 9377.7 | 54.1 | 100.0% |
| luajit | 12611.2 | 8153.9 | 16565.6 | 2333.1 | 100.0% |
| java | 33187.3 | 31284.3 | 34472.5 | 721.1 | 100.0% |
| js | 39523.2 | 37903.8 | 46763.7 | 1603.8 | 100.0% |
| php | 41566.5 | 39712.4 | 44414.5 | 1029.0 | 100.0% |
| lua | 79650.6 | 77479.8 | 84365.4 | 1175.1 | 100.0% |
| python | 133972.1 | 132322.1 | 139972.9 | 1318.8 | 100.0% |

## bernoulli30

| 语言 | 平均时间(μs) | 最小时间(μs) | 最大时间(μs) | 标准差(μs) | 成功率 |
|------|------------------|------------------|------------------|-----------------|--------|
| asm | 268.1 | 249.4 | 323.3 | 15.0 | 100.0% |
| python | 16900.1 | 16554.4 | 17566.4 | 224.9 | 100.0% |
| c | 2223744.9 | 2216676.7 | 2249864.6 | 7063.3 | 100.0% |
| cpp | 2282445.5 | 2273595.1 | 2298445.2 | 4331.6 | 100.0% |
| clang-cpp | 3301683.9 | 3275206.3 | 3488140.1 | 52170.3 | 100.0% |
| clang-c | 3309816.0 | 3273304.9 | 3480759.4 | 63934.6 | 100.0% |
| java | 3655442.2 | 3545129.3 | 3778341.1 | 48475.5 | 100.0% |
| rust | 3719498.0 | 3710023.2 | 3784117.9 | 16804.4 | 100.0% |
| go | 5665103.3 | 5647844.8 | 5688055.3 | 8861.4 | 100.0% |
| dart | 7645244.9 | 7634743.9 | 7723708.4 | 13463.9 | 100.0% |
| js | 13204817.9 | 13063588.9 | 15681440.8 | 414065.4 | 100.0% |
| luajit | 21268446.2 | 21210748.0 | 21438663.5 | 50898.3 | 100.0% |

## fib42

| 语言 | 平均时间(μs) | 最小时间(μs) | 最大时间(μs) | 标准差(μs) | 成功率 |
|------|------------------|------------------|------------------|-----------------|--------|
| asm | 282.2 | 258.9 | 336.4 | 16.5 | 100.0% |
| php | 45878.6 | 44880.6 | 47480.3 | 745.2 | 100.0% |
| c | 462049.1 | 461743.6 | 462572.1 | 239.1 | 100.0% |
| cpp | 485195.6 | 483613.0 | 487399.6 | 907.4 | 100.0% |
| clang-cpp | 684679.9 | 681184.3 | 708540.2 | 6448.9 | 100.0% |
| rust | 692203.8 | 690084.7 | 707460.4 | 3794.1 | 100.0% |
| clang-c | 721421.2 | 719949.2 | 726437.6 | 1800.7 | 100.0% |
| java | 964450.1 | 879020.2 | 1001120.3 | 24182.6 | 100.0% |
| zig | 1255339.4 | 1251247.6 | 1285138.4 | 8955.7 | 100.0% |
| go | 1735197.3 | 1730885.3 | 1743938.7 | 2909.8 | 100.0% |
| dart | 2396687.9 | 2394804.0 | 2408021.9 | 2949.5 | 100.0% |
| js | 2644655.1 | 2619058.4 | 2731782.2 | 31278.0 | 100.0% |
| luajit | 3080684.2 | 2712672.0 | 3433206.8 | 224136.2 | 100.0% |

## 总结

- **fib30**: 最快语言是 c (平均 2.2181ms)
- **bernoulli30**: 最快语言是 asm (平均 268.0874μs)
- **fib42**: 最快语言是 asm (平均 282.1803μs)

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


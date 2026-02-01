# LangBench 测试报告

## 性能图表

### 性能对比

![性能对比](report/comparison.png)

### 性能趋势

![性能趋势](report/trend.png)

## fib30

| 语言 | 平均时间(μs) | 最小时间(μs) | 最大时间(μs) | 标准差(μs) | 成功率 |
|------|------------------|------------------|------------------|-----------------|--------|
| c | 2206.6 | 2159.8 | 2290.0 | 27.0 | 100.0% |
| clang-c | 2755.6 | 2706.1 | 2844.1 | 27.0 | 100.0% |
| cpp | 2817.8 | 2670.3 | 3874.8 | 172.4 | 100.0% |
| clang-cpp | 3278.4 | 3228.9 | 3377.2 | 37.0 | 100.0% |
| rust | 3486.9 | 3358.1 | 3697.9 | 75.1 | 100.0% |
| asm | 4296.6 | 4232.2 | 4607.4 | 68.5 | 100.0% |
| zig | 4308.8 | 4208.3 | 5258.1 | 196.4 | 100.0% |
| go | 6069.4 | 5874.4 | 6718.6 | 180.1 | 100.0% |
| dart | 7573.4 | 7466.6 | 7782.0 | 88.2 | 100.0% |
| luajit | 10453.8 | 7183.6 | 14226.2 | 2105.2 | 100.0% |
| java | 33297.0 | 31453.8 | 35394.0 | 952.6 | 100.0% |
| js | 37065.0 | 35655.3 | 43925.5 | 1200.8 | 100.0% |
| php | 39800.4 | 38260.9 | 43802.5 | 1085.5 | 100.0% |
| lua | 103741.4 | 99849.5 | 107152.7 | 1608.1 | 100.0% |
| python | 136671.2 | 134868.6 | 142062.2 | 1640.2 | 100.0% |

## fib42

| 语言 | 平均时间(μs) | 最小时间(μs) | 最大时间(μs) | 标准差(μs) | 成功率 |
|------|------------------|------------------|------------------|-----------------|--------|
| asm | 300.2 | 269.9 | 373.6 | 31.5 | 100.0% |
| php | 40795.7 | 38939.0 | 43119.7 | 1218.9 | 100.0% |
| c | 476717.8 | 473480.2 | 483798.0 | 2738.4 | 100.0% |
| cpp | 485070.6 | 482466.7 | 497174.5 | 3016.8 | 100.0% |
| clang-c | 680450.4 | 679822.4 | 682570.2 | 734.0 | 100.0% |
| clang-cpp | 681491.1 | 680552.0 | 688269.9 | 1631.1 | 100.0% |
| rust | 815331.9 | 814267.6 | 821084.7 | 1975.1 | 100.0% |
| java | 969377.9 | 946668.1 | 991608.9 | 13640.5 | 100.0% |
| zig | 1252991.5 | 1250401.0 | 1274678.7 | 5490.5 | 100.0% |
| go | 1562075.9 | 1558113.6 | 1567132.0 | 2054.6 | 100.0% |
| dart | 2112938.2 | 2108585.1 | 2154286.9 | 10797.3 | 100.0% |
| js | 3049985.8 | 3023765.8 | 3214339.7 | 43638.8 | 100.0% |
| luajit | 3121588.7 | 2716260.9 | 3421487.6 | 244586.0 | 100.0% |

## 总结

- **fib30**: 最快语言是 c (平均 2.2066ms)
- **fib42**: 最快语言是 asm (平均 300.1928μs)

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


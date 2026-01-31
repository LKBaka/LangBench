section .data
    n dq 42

section .text
    global _start

; 迭代计算 fibonacci(n)
; 参数: RDI = n
; 返回: RAX = fib(n)
fib:
    cmp rdi, 1
    jle .base_case

    xor rax, rax                ; fib(0) = 0
    mov rbx, 1                  ; fib(1) = 1
    mov rcx, rdi
    sub rcx, 1                  ; 循环 n-1 次

.loop:
    add rax, rbx                ; fib(i) = fib(i-2) + fib(i-1)
    xchg rax, rbx               ; 交换: rbx=新fib, rax=旧fib
    loop .loop

    mov rax, rbx                ; 返回 fib(n)
    ret

.base_case:
    mov rax, rdi
    ret

_start:
    mov rdi, [n]
    call fib

    ; 打印结果
    call print_number

    ; 退出程序
    mov rax, 60                 ; sys_exit
    xor rdi, rdi
    syscall

; 打印数字到 stdout
; 参数: RAX = 要打印的数字
print_number:
    mov r8, 10
    xor rcx, rcx                ; 数字位数计数器
    mov rbx, rsp                ; 保存原始栈指针

.divide_loop:
    xor rdx, rdx
    div r8
    add dl, '0'
    dec rsp
    mov byte [rsp], dl
    inc rcx
    test rax, rax
    jnz .divide_loop

    ; 打印字符串
    mov rax, 1                  ; sys_write
    mov rdi, 1                  ; stdout
    mov rsi, rsp
    mov rdx, rcx
    syscall

    mov rsp, rbx                ; 恢复栈指针
    ret

section .data
    n dq 30

section .text
    global _start

; 递归计算 fibonacci(n)
; 参数: RDI = n
; 返回: RAX = fib(n)
fib:
    cmp rdi, 1
    jle .base_case

    ; 计算 fib(n-1)
    push rdi                    ; 保存当前 n
    dec rdi
    call fib                    ; RAX = fib(n-1)
    pop rsi                     ; 恢复 n

    ; 计算 fib(n-2)
    push rax                    ; 保存 fib(n-1)
    mov rdi, rsi
    sub rdi, 2
    call fib                    ; RAX = fib(n-2)

    ; 返回 fib(n-1) + fib(n-2)
    add rax, [rsp]              ; 加上保存的 fib(n-1)
    add rsp, 8                  ; 清除栈上保存的 fib(n-1)
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

section .data
    n db 30
    result_format db "%ld", 10, 0

section .bss
    result resq 1

section .text
    global _start

; 递归计算 fibonacci(n)
; 参数: RDI = n
; 返回: RAX = fib(n)
fib:
    cmp rdi, 1
    jle .base_case
    push rbx                    ; 保存调用者寄存器
    mov rbx, rdi

    ; 计算 fib(n-1)
    dec rdi
    call fib
    push rax                    ; 保存 fib(n-1)

    ; 计算 fib(n-2)
    mov rdi, rbx
    sub rdi, 2
    call fib

    ; 返回 fib(n-1) + fib(n-2)
    pop rbx
    add rax, rbx
    pop rbx
    ret

.base_case:
    mov rax, rdi
    ret

_start:
    mov rdi, [n]
    call fib
    mov [result], rax

    ; 打印结果 (转换十进制)
    mov rdi, [result]
    call print_number

    ; 退出程序
    mov rax, 60                 ; sys_exit
    xor rdi, rdi
    syscall

; 打印数字到 stdout
; 参数: RDI = 要打印的数字
print_number:
    mov rax, rdi
    mov r8, 10
    xor rcx, rcx                ; 数字位数计数器

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

    add rsp, rcx                ; 恢复栈指针
    ret

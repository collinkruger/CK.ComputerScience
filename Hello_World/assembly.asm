global _start ; Tell the linker the name of our entry point

section .data ; Define constants
	msg: db	"Hello, World! From Assembly.", 10 ; Create the Hello World string, with a linefeed at the end (LF is 10 in ASCII).
	.len: equ $ - msg ; Calculate the length of our hello world string

section .bss ; Define variables (none in this case)

section .text ; Code
	_start: ; Our entry point
		mov	rax, 1       ; System call for write
		mov	rdi, 1       ; stdout file description
		mov	rsi, msg     ; Point to our string
		mov	rdx, msg.len ; Specify the size our string
		syscall          ; Invoke the system call

		mov rax, 60 ; System call for exit
		mov rdi, 0  ; Success status code
		syscall     ; Invoke the system call


; To compile run the following commands
; nasm -f elf64 -o _hello_world_assembly.o assembly.asm
; ld -o _hello_world_assembly _hello_world_assembly.o
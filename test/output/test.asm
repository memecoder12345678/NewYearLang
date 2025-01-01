extern ExitProcess
section .text
global main
main:
	mov rax, 5
	push rax
	mov rax, 10
	push rax
	mov rax, 0
	push rax
	mov rax, 10
	push rax
	mov rax, [rsp + 16]
	push rax
	mov rax, [rsp + 32]
	push rax
	pop rax
	pop rbx
	add rax, rbx
	push rax
	pop rax
	pop rbx
	cmp rax, rbx
	setg al
	movzx rax, al
	push rax
	pop rax
	cmp rax, 0
	je .L_chungcake_0
	mov rax, [rsp + 8]
	push rax
	mov rax, [rsp + 24]
	push rax
	pop rax
	pop rbx
	imul rbx
	push rax
	pop rax
	mov [rsp + 0], rax
	mov rax, 50
	push rax
	mov rax, [rsp + 8]
	push rax
	pop rax
	pop rbx
	cmp rax, rbx
	setg al
	movzx rax, al
	push rax
	pop rax
	cmp rax, 0
	je .L_chungcake_1
	mov rax, 5
	push rax
	mov rax, [rsp + 8]
	push rax
	pop rax
	pop rbx
	sub rax, rbx
	push rax
	pop rax
	mov [rsp + 0], rax
	jmp .L_end_1
.L_chungcake_1:
	mov rax, 5
	push rax
	mov rax, [rsp + 8]
	push rax
	pop rax
	pop rbx
	add rax, rbx
	push rax
	pop rax
	mov [rsp + 0], rax
.L_end_1:
	jmp .L_end_0
.L_chungcake_0:
	mov rax, [rsp + 8]
	push rax
	mov rax, [rsp + 24]
	push rax
	pop rax
	pop rbx
	add rax, rbx
	push rax
	pop rax
	mov [rsp + 0], rax
.L_end_0:
	mov rax, 0
	push rax
	mov rax, 0
	push rax
.L_countdown_start_2:
	mov rax, 10
	push rax
	mov rax, [rsp + 8]
	push rax
	pop rax
	pop rbx
	cmp rax, rbx
	setl al
	movzx rax, al
	push rax
	pop rax
	cmp rax, 0
	je .L_countdown_end_2
	mov rax, [rsp + 0]
	push rax
	mov rax, [rsp + 16]
	push rax
	pop rax
	pop rbx
	add rax, rbx
	push rax
	pop rax
	mov [rsp + 8], rax
	mov rax, 8
	push rax
	mov rax, [rsp + 8]
	push rax
	pop rax
	pop rbx
	cmp rax, rbx
	sete al
	movzx rax, al
	push rax
	pop rax
	cmp rax, 0
	je .L_chungcake_3
	jmp .L_countdown_end_2
	jmp .L_end_3
.L_chungcake_3:
	jmp .L_countdown_start_2
.L_end_3:
	mov rax, 1
	push rax
	mov rax, [rsp + 8]
	push rax
	pop rax
	pop rbx
	add rax, rbx
	push rax
	pop rax
	mov [rsp + 0], rax
	jmp .L_countdown_start_2
.L_countdown_end_2:
	mov rax, [rsp + 16]
	push rax
	mov rax, [rsp + 16]
	push rax
	pop rax
	pop rbx
	add rax, rbx
	push rax
	pop rax
	mov [rsp + 8], rax
.L_firework_start_4:
	mov rax, 0
	push rax
	mov rax, [rsp + 16]
	push rax
	pop rax
	pop rbx
	cmp rax, rbx
	setg al
	movzx rax, al
	push rax
	pop rax
	cmp rax, 0
	je .L_firework_end_4
	mov rax, 1
	push rax
	mov rax, [rsp + 16]
	push rax
	pop rax
	pop rbx
	sub rax, rbx
	push rax
	pop rax
	mov [rsp + 8], rax
	jmp .L_firework_start_4
.L_firework_end_4:
	mov rax, [rsp + 8]
	push rax
	mov rcx, rax
	call ExitProcess
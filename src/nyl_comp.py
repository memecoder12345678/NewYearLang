# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                      NewYearLang                      #
#       Author: MemeCoder (memecoder17@gmail.com)       #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import os
import platform
import subprocess
import sys
from typing import List, Optional, Union

import click
import colorama

colorama.init(autoreset=True)
RED = colorama.Fore.LIGHTRED_EX
GREEN = colorama.Fore.LIGHTGREEN_EX
CYAN = colorama.Fore.LIGHTCYAN_EX
RESET = colorama.Fore.RESET
optimize = False


class Node:
    pass


class NodeTerm(Node):
    pass


class NodeStmt(Node):
    pass


class NodeExpr(Node):
    pass


class NodeTermIntLit(NodeTerm):
    def __init__(self, value: int):
        self.value = value


class NodeTermIdent(NodeTerm):
    def __init__(self, value: str):
        self.value = value


class NodeTermParen(NodeTerm):
    def __init__(self, expr: NodeExpr):
        self.expr = expr


class NodeBinExpr(NodeExpr):
    def __init__(self, lhs: NodeExpr, rhs: NodeExpr):
        self.lhs = lhs
        self.rhs = rhs


class NodeBinExprAdd(NodeBinExpr):
    pass


class NodeBinExprSub(NodeBinExpr):
    pass


class NodeBinExprMulti(NodeBinExpr):
    pass


class NodeBinExprDiv(NodeBinExpr):
    pass


class NodeBinExprAnd(NodeBinExpr):
    pass


class NodeBinExprOr(NodeBinExpr):
    pass


class NodeBinExprEq(NodeBinExpr):
    pass


class NodeBinExprNeq(NodeBinExpr):
    pass


class NodeBinExprLt(NodeBinExpr):
    pass


class NodeBinExprGt(NodeBinExpr):
    pass


class NodeBinExprLte(NodeBinExpr):
    pass


class NodeBinExprGte(NodeBinExpr):
    pass


class NodeStmtHappynewyear(NodeStmt):
    def __init__(self, expr: NodeExpr):
        self.expr = expr


class NodeStmtPeachblossom(NodeStmt):
    def __init__(self, ident: str, expr: NodeExpr):
        self.ident = ident
        self.expr = expr


class NodeStmtComment(NodeStmt):
    def __init__(self, content: str):
        self.content = content


class NodeStmtCaramelizedporkandeggs(NodeStmt):
    def __init__(
        self,
        condition: NodeExpr,
        true_block: List[NodeStmt],
        false_block: Optional[List[NodeStmt]] = None,
    ):
        self.condition = condition
        self.true_block = true_block
        self.false_block = false_block


class NodeStmtFirework(NodeStmt):
    def __init__(self, condition: NodeExpr, block: List[NodeStmt]):
        self.condition = condition
        self.block = block


class NodeStmtCountdown(NodeStmt):
    def __init__(
        self,
        init: NodeStmt,
        condition: NodeExpr,
        update: NodeStmt,
        block: List[NodeStmt],
    ):
        self.init = init
        self.condition = condition
        self.update = update
        self.block = block


class NodeScope:
    def __init__(self, stmts: List[NodeStmt]):
        self.stmts = stmts


class NodeProg:
    def __init__(self, stmts: List[NodeStmt]):
        self.stmts = stmts


# --- Token Definitions ---
class TokenType:
    HAPPYNEWYEAR = "Happynewyear"
    INT_LIT = "int_lit"
    SEMI = ";"
    IDENT = "ident"
    PEACHBLOSSOM = "Peachblossom"
    EQ = "="
    PLUS = "+"
    STAR = "*"
    MINUS = "-"
    FSLASH = "/"
    OPEN_PAREN = "("
    CLOSE_PAREN = ")"
    COMMENT = "comment"
    CARAMELIZEDPORKANDEGGS = "Caramelizedporkandeggs"
    CHUNGCAKE = "Chungcake"
    FIREWORK = "Firework"
    COUNTDOWN = "Countdown"
    OPEN_BRACE = "{"
    CLOSE_BRACE = "}"
    EQEQ = "=="
    NEQ = "!="
    LT = "<"
    GT = ">"
    LTE = "<="
    GTE = ">="


class Token:
    def __init__(self, type: str, line: int, value: Optional[Union[int, str]] = None):
        self.type = type
        self.line = line
        self.value = value


# --- Tokenizer ---
class Tokenizer:
    def __init__(self, src: str):
        self.src = src
        self.index = 0

    def peek(self, offset: int = 0) -> Optional[str]:
        if self.index + offset >= len(self.src):
            return None
        return self.src[self.index + offset]

    def consume(self) -> str:
        char = self.src[self.index]
        self.index += 1
        return char

    def tokenize(self) -> List[Token]:
        tokens = []
        line_count = 1

        while self.index < len(self.src):
            char = self.peek()

            if char == "#":
                self.consume()
                char = self.peek()
                while char and char in " \t":
                    self.consume()
                    char = self.peek()
                comment = ""
                while char and char != "\n":
                    comment += self.consume()
                    char = self.peek()
                tokens.append(Token(TokenType.COMMENT, line_count, comment))

            elif char.isalpha():
                buffer = ""
                while char and char.isalnum():
                    buffer += self.consume()
                    char = self.peek()
                if buffer == "Happynewyear":
                    tokens.append(Token(TokenType.HAPPYNEWYEAR, line_count))
                elif buffer == "Peachblossom":
                    tokens.append(Token(TokenType.PEACHBLOSSOM, line_count))
                elif buffer == "Caramelizedporkandeggs":
                    tokens.append(Token(TokenType.CARAMELIZEDPORKANDEGGS, line_count))
                elif buffer == "Chungcake":
                    tokens.append(Token(TokenType.CHUNGCAKE, line_count))
                elif buffer == "Firework":
                    tokens.append(Token(TokenType.FIREWORK, line_count))
                elif buffer == "Countdown":
                    tokens.append(Token(TokenType.COUNTDOWN, line_count))
                else:
                    tokens.append(Token(TokenType.IDENT, line_count, buffer))

            elif char.isdigit():
                buffer = ""
                while char and char.isdigit():
                    buffer += self.consume()
                    char = self.peek()
                tokens.append(Token(TokenType.INT_LIT, line_count, int(buffer)))

            elif char == "=" and self.peek(1) == "=":
                tokens.append(Token(TokenType.EQEQ, line_count))
                self.consume()
                self.consume()

            elif char in ";=+-*/(){},":
                tokens.append(
                    Token(
                        getattr(
                            TokenType,
                            {
                                ";": "SEMI",
                                "=": "EQ",
                                "+": "PLUS",
                                "-": "MINUS",
                                "*": "STAR",
                                "/": "FSLASH",
                                "(": "OPEN_PAREN",
                                ")": "CLOSE_PAREN",
                                "{": "OPEN_BRACE",
                                "}": "CLOSE_BRACE",
                            }[char],
                        ),
                        line_count,
                    )
                )
                self.consume()

            elif char == "!" and self.peek(1) == "=":
                tokens.append(Token(TokenType.NEQ, line_count))
                self.consume()
                self.consume()

            elif char == "<":
                if self.peek(1) == "=":
                    tokens.append(Token(TokenType.LTE, line_count))
                    self.consume()
                    self.consume()
                else:
                    tokens.append(Token(TokenType.LT, line_count))
                    self.consume()

            elif char == ">":
                if self.peek(1) == "=":
                    tokens.append(Token(TokenType.GTE, line_count))
                    self.consume()
                    self.consume()
                else:
                    tokens.append(Token(TokenType.GT, line_count))
                    self.consume()

            elif char.isspace():
                if char == "\n":
                    line_count += 1
                self.consume()
            else:
                print(
                    f"{RED}ERROR: Unexpected character - '{char}' at line {line_count}{RESET}"
                )
                sys.exit(1)

        return tokens


# --- Parser ---
class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.index = 0
        self.in_loop = 0

    def peek(self, offset: int = 0) -> Optional[Token]:
        if self.index + offset >= len(self.tokens):
            return None
        return self.tokens[self.index + offset]

    def consume(self) -> Token:
        if self.index >= len(self.tokens):
            print(f"{RED}ERROR: Unexpected end of input - expected more tokens{RESET}")
            sys.exit(1)
        token = self.tokens[self.index]
        self.index += 1
        return token

    def parse_term(self) -> NodeTerm:
        token = self.consume()
        if token.type == TokenType.INT_LIT:
            return NodeTermIntLit(token.value)
        elif token.type == TokenType.IDENT:
            return NodeTermIdent(token.value)
        elif token.type == TokenType.OPEN_PAREN:
            expr = self.parse_expr()
            if self.consume().type != TokenType.CLOSE_PAREN:
                print(
                    f"{RED}ERROR: Expected closing parenthesis at line {token.line}{RESET}"
                )
                sys.exit(1)
            return NodeTermParen(expr)
        else:
            print(f"{RED}ERROR: Unexpected token in term at line {token.line}{RESET}")
            sys.exit(1)

    def parse_expr(self) -> NodeExpr:
        lhs = self.parse_term()
        while True:
            token = self.peek()
            if token and token.type in {
                TokenType.PLUS,
                TokenType.MINUS,
                TokenType.STAR,
                TokenType.FSLASH,
                TokenType.GTE,
                TokenType.EQEQ,
                TokenType.NEQ,
                TokenType.LT,
                TokenType.GT,
                TokenType.LTE,
            }:
                op = self.consume().type
                rhs = self.parse_term()
                if op == TokenType.PLUS:
                    lhs = NodeBinExprAdd(lhs, rhs)
                elif op == TokenType.MINUS:
                    lhs = NodeBinExprSub(lhs, rhs)
                elif op == TokenType.STAR:
                    lhs = NodeBinExprMulti(lhs, rhs)
                elif op == TokenType.FSLASH:
                    lhs = NodeBinExprDiv(lhs, rhs)
                elif op == TokenType.EQEQ:
                    lhs = NodeBinExprEq(lhs, rhs)
                elif op == TokenType.NEQ:
                    lhs = NodeBinExprNeq(lhs, rhs)
                elif op == TokenType.LT:
                    lhs = NodeBinExprLt(lhs, rhs)
                elif op == TokenType.GT:
                    lhs = NodeBinExprGt(lhs, rhs)
                elif op == TokenType.LTE:
                    lhs = NodeBinExprLte(lhs, rhs)
                elif op == TokenType.GTE:
                    lhs = NodeBinExprGte(lhs, rhs)
            else:
                break
        return lhs

    def parse_block(self) -> List[NodeStmt]:
        stmts = []
        if self.peek() is None or self.peek().type != TokenType.OPEN_BRACE:
            print(
                f"{RED}ERROR: Expected opening brace at line {self.peek().line if self.peek() else 'EOF'}{RESET}"
            )
            sys.exit(1)
        self.consume()
        while self.peek() is not None and self.peek().type != TokenType.CLOSE_BRACE:
            stmts.append(self.parse_stmt())
        if self.peek() is None:
            print(f"{RED}ERROR: Unexpected end of file - Expected closing brace{RESET}")
            sys.exit(1)
        self.consume()
        return stmts

    def parse_stmt(self) -> NodeStmt:
        token = self.peek()
        if token is None:
            print(f"{RED}ERROR: Unexpected end of file while parsing statement{RESET}")
            sys.exit(1)
        if token.type == TokenType.COMMENT:
            return NodeStmtComment(self.consume().value)
        elif token.type == TokenType.PEACHBLOSSOM:
            self.consume()
            ident = self.consume()
            if ident.type != TokenType.IDENT:
                print(
                    f"{RED}ERROR: Expected identifier after 'Peachblossom' at line {ident.line}{RESET}"
                )
                sys.exit(1)
            if self.consume().type != TokenType.EQ:
                print(
                    f"{RED}ERROR: Expected '=' after identifier at line {ident.line}{RESET}"
                )
                sys.exit(1)
            expr = self.parse_expr()
            if self.consume().type != TokenType.SEMI:
                print(
                    f"{RED}ERROR: Expected ';' at the end of statement at line {ident.line}{RESET}"
                )
                sys.exit(1)
            return NodeStmtPeachblossom(ident.value, expr)
        elif token.type == TokenType.HAPPYNEWYEAR:
            if self.in_loop > 0:
                print(
                    f"{RED}LIMITED FEATURES: 'Happynewyear' statement is not allowed inside loops at line {token.line}{RESET}"
                )
                sys.exit(1)
            self.consume()
            expr = self.parse_expr()
            if self.consume().type != TokenType.SEMI:
                print(
                    f"{RED}ERROR: Expected ';' at the end of statement at line {token.line}{RESET}"
                )
                sys.exit(1)
            return NodeStmtHappynewyear(expr)
        elif token.type == TokenType.IDENT:
            ident = self.consume().value
            if self.consume().type != TokenType.EQ:
                print(
                    f"{RED}ERROR: Expected '=' after identifier at line {token.line}{RESET}"
                )
                sys.exit(1)
            expr = self.parse_expr()
            if self.consume().type != TokenType.SEMI:
                print(
                    f"{RED}ERROR: Expected ';' at the end of statement at line {token.line}{RESET}"
                )
                sys.exit(1)
            return NodeStmtPeachblossom(ident, expr)
        elif token.type == TokenType.CARAMELIZEDPORKANDEGGS:
            self.consume()
            condition = self.parse_expr()
            true_block = self.parse_block()
            false_block = None
            if self.peek() and self.peek().type == TokenType.CHUNGCAKE:
                self.consume()
                false_block = self.parse_block()
            return NodeStmtCaramelizedporkandeggs(condition, true_block, false_block)
        elif token.type == TokenType.FIREWORK:
            self.consume()
            self.in_loop += 1
            condition = self.parse_expr()
            block = self.parse_block()
            self.in_loop -= 1
            return NodeStmtFirework(condition, block)
        elif token.type == TokenType.COUNTDOWN:
            self.consume()
            self.in_loop += 1
            init = self.parse_stmt()
            condition = self.parse_expr()
            if self.consume().type != TokenType.SEMI:
                print(
                    f"{RED}ERROR: Expected ';' after 'Countdown' loop condition at line {token.line}{RESET}"
                )
                sys.exit(1)
            update = self.parse_stmt()
            block = self.parse_block()
            self.in_loop -= 1
            return NodeStmtCountdown(init, condition, update, block)
        else:
            print(f"{RED}ERROR: Unexpected statement at line {token.line}{RESET}")
            sys.exit(1)

    def parse_prog(self) -> NodeProg:
        stmts = []
        while self.index < len(self.tokens):
            stmts.append(self.parse_stmt())
        return NodeProg(stmts)


# --- Generator ---
class Generator:
    def __init__(self, prog: NodeProg):
        self.m_prog = prog
        self.m_output = []
        self.m_stack_size = 0
        self.m_vars = []
        self.m_scopes = []
        self.m_label_count = 0

    def push(self, reg: str):
        self.m_output.append(f"\tpush {reg}")
        self.m_stack_size += 1

    def pop(self, reg: str):
        self.m_output.append(f"\tpop {reg}")
        self.m_stack_size -= 1

    def begin_scope(self):
        self.m_scopes.append(len(self.m_vars))

    def end_scope(self):
        pop_count = len(self.m_vars) - self.m_scopes.pop()
        if pop_count != 0:
            self.m_output.append(f"\tadd rsp, {pop_count * 8}")
        self.m_stack_size -= pop_count
        self.m_vars = self.m_vars[: len(self.m_vars) - pop_count]

    def gen_term(self, term: NodeTerm):
        if isinstance(term, NodeTermIntLit):
            self.m_output.append(f"\tmov rax, {term.value}")
            self.push("rax")
        elif isinstance(term, NodeTermIdent):
            for var in self.m_vars:
                if var["name"] == term.value:
                    offset = f"[rsp + {(self.m_stack_size - var['stack_loc'] - 1) * 8}]"
                    self.m_output.append(f"\tmov rax, {offset}")
                    self.push("rax")
                    return
            print(f"{RED}ERROR: Undeclared identifier - '{term.value}'{RESET}")
            sys.exit(1)
        elif isinstance(term, NodeTermParen):
            self.gen_expr(term.expr)

    def gen_bin_expr(self, bin_expr: NodeBinExpr):
        self.gen_expr(bin_expr.rhs)
        self.gen_expr(bin_expr.lhs)
        self.pop("rax")
        self.pop("rbx")
        if isinstance(bin_expr, NodeBinExprAdd):
            self.m_output.append("\tadd rax, rbx")
        elif isinstance(bin_expr, NodeBinExprSub):
            self.m_output.append("\tsub rax, rbx")
        elif isinstance(bin_expr, NodeBinExprMulti):
            self.m_output.append("\timul rbx")
        elif isinstance(bin_expr, NodeBinExprDiv):
            self.m_output.append("\txor rdx, rdx")
            self.m_output.append("\tidiv rbx")
        elif isinstance(bin_expr, NodeBinExprEq):
            self.m_output.append("\tcmp rax, rbx")
            self.m_output.append("\tsete al")
            self.m_output.append("\tmovzx rax, al")
        elif isinstance(bin_expr, NodeBinExprNeq):
            self.m_output.append("\tcmp rax, rbx")
            self.m_output.append("\tsetne al")
            self.m_output.append("\tmovzx rax, al")
        elif isinstance(bin_expr, NodeBinExprLt):
            self.m_output.append("\tcmp rax, rbx")
            self.m_output.append("\tsetl al")
            self.m_output.append("\tmovzx rax, al")
        elif isinstance(bin_expr, NodeBinExprGt):
            self.m_output.append("\tcmp rax, rbx")
            self.m_output.append("\tsetg al")
            self.m_output.append("\tmovzx rax, al")
        elif isinstance(bin_expr, NodeBinExprLte):
            self.m_output.append("\tcmp rax, rbx")
            self.m_output.append("\tsetle al")
            self.m_output.append("\tmovzx rax, al")
        elif isinstance(bin_expr, NodeBinExprGte):
            self.m_output.append("\tcmp rax, rbx")
            self.m_output.append("\tsetge al")
            self.m_output.append("\tmovzx rax, al")
        self.push("rax")

    def gen_expr(self, expr: NodeExpr):
        if isinstance(expr, NodeTerm):
            self.gen_term(expr)
        elif isinstance(expr, NodeBinExpr):
            self.gen_bin_expr(expr)

    def gen_stmt(self, stmt: NodeStmt):
        if isinstance(stmt, NodeStmtComment) and not optimize:
            self.m_output.append(f"\t; {stmt.content}")
        elif isinstance(stmt, NodeStmtHappynewyear):
            self.gen_expr(stmt.expr)
            self.pop("rdx")
            self.m_output.append("\tlea rcx, [rel fmt]")
            self.m_output.append("\tsub rsp, 8")
            self.m_output.append("\tcall printf")
            self.m_output.append("\tadd rsp, 8")
        elif isinstance(stmt, NodeStmtPeachblossom):
            self.gen_expr(stmt.expr)
            for var in self.m_vars:
                if var["name"] == stmt.ident:
                    self.pop("rax")
                    offset = f"[rsp + {(self.m_stack_size - var['stack_loc'] - 1) * 8}]"
                    self.m_output.append(f"\tmov {offset}, rax")
                    return
            self.m_vars.append({"name": stmt.ident, "stack_loc": self.m_stack_size - 1})
        elif isinstance(stmt, NodeStmtCaramelizedporkandeggs):
            self.gen_expr(stmt.condition)
            self.pop("rax")
            self.m_output.append("\tcmp rax, 0")
            label_chungcake = f".L_chungcake_{self.m_label_count}"
            label_end = f".L_end_{self.m_label_count}"
            self.m_label_count += 1
            self.m_output.append(f"\tje {label_chungcake}")
            self.begin_scope()
            for s in stmt.true_block:
                self.gen_stmt(s)
            self.end_scope()
            self.m_output.append(f"\tjmp {label_end}")
            self.m_output.append(f"{label_chungcake}:")
            if stmt.false_block:
                self.begin_scope()
                for s in stmt.false_block:
                    self.gen_stmt(s)
                self.end_scope()
            self.m_output.append(f"{label_end}:")
        elif isinstance(stmt, NodeStmtFirework):
            label_start = f".L_firework_start_{self.m_label_count}"
            label_end = f".L_firework_end_{self.m_label_count}"
            self.m_label_count += 1
            self.m_output.append(f"{label_start}:")
            self.gen_expr(stmt.condition)
            self.pop("rax")
            self.m_output.append("\tcmp rax, 0")
            self.m_output.append(f"\tje {label_end}")
            self.begin_scope()
            for s in stmt.block:
                self.gen_stmt(s)
            self.end_scope()
            self.m_output.append(f"\tjmp {label_start}")
            self.m_output.append(f"{label_end}:")
        elif isinstance(stmt, NodeStmtCountdown):
            self.gen_stmt(stmt.init)
            label_start = f".L_countdown_start_{self.m_label_count}"
            label_end = f".L_countdown_end_{self.m_label_count}"
            self.m_label_count += 1
            self.m_output.append(f"{label_start}:")
            self.gen_expr(stmt.condition)
            self.pop("rax")
            self.m_output.append("\tcmp rax, 0")
            self.m_output.append(f"\tje {label_end}")
            self.begin_scope()
            for s in stmt.block:
                self.gen_stmt(s)
            self.end_scope()
            self.gen_stmt(stmt.update)
            self.m_output.append(f"\tjmp {label_start}")
            self.m_output.append(f"{label_end}:")

    def optimize_assembly(self, assembly_code: str) -> str:
        lines = assembly_code.split("\n")
        used_labels = set()
        tab_info = []
        for line in lines:
            tab_count = len(line) - len(line.lstrip("\t"))
            tab_info.append(tab_count)
            line = line.strip()
            if any(
                x in line
                for x in ["jmp", "je", "jne", "jg", "jl", "jge", "jle", "call"]
            ):
                parts = line.split()
                if len(parts) > 1:
                    label = parts[-1]
                    used_labels.add(label)
        optimized = []
        last_line = None
        for i, line in enumerate(lines):
            tab_count = tab_info[i]
            line = line.strip()
            if not line:
                continue
            if line.endswith(":"):
                label = line[:-1]
                if label != "main" and label not in used_labels:
                    continue
            if last_line and (
                (
                    "push" in last_line
                    and "pop" in line
                    and len(last_line.split()) > 1
                    and len(line.split()) > 1
                    and last_line.split()[-1] == line.split()[-1]
                )
            ):
                optimized.pop()
                last_line = None
                continue
            if last_line and "mov" in last_line and "mov" in line:
                try:
                    src1, dst1 = map(str.strip, last_line.split(None, 1)[1].split(","))
                    src2, dst2 = map(str.strip, line.split(None, 1)[1].split(","))
                    if src1 == dst2 and dst1 == src2:
                        optimized.pop()
                        last_line = None
                        continue
                except (IndexError, ValueError):
                    pass
            try:
                parts = line.split()
                if len(parts) > 1:
                    instruction = parts[0]
                    operands = parts[1]
                    if instruction in ["xor", "and", "or"]:
                        if "," in operands:
                            reg1, reg2 = map(str.strip, operands.split(","))
                            if reg1 == reg2:
                                continue
                    if instruction in ["add", "sub", "mul", "div", "imul", "idiv"]:
                        if "," in operands:
                            reg, val = map(str.strip, operands.split(","))
                            if val in ["0", "1"]:
                                continue
                            elif val == "1":
                                optimized.append(
                                    f"{instruction.replace("add", "inc").replace("sub", "dec")} {reg}"
                                )
                                last_line = None
                                continue
            except (IndexError, ValueError):
                pass
            optimized.append("\t" * tab_count + line)
            last_line = line
        return "\n".join(optimized)

    def gen_prog(self) -> str:
        global optimize
        self.m_output.append("bits 64")
        self.m_output.append("default rel")
        self.m_output.append("section .data")
        self.m_output.append('\tfmt db "%d", 10, 0')
        self.m_output.append("section .text")
        self.m_output.append("\tglobal main")
        self.m_output.append("\textern ExitProcess")
        self.m_output.append("\textern printf")
        self.m_output.append("main:")
        for stmt in self.m_prog.stmts:
            self.gen_stmt(stmt)
        self.m_output.append("\txor rcx, rcx")
        self.m_output.append("\tcall ExitProcess\n")
        return (
            self.optimize_assembly("\n".join(self.m_output))
            if optimize
            else "\n".join(self.m_output)
        )


# --- Main Program ---
@click.command()
@click.argument("source_file", required=False)
@click.option("--asm", is_flag=True, help="Generates assembly code from the source")
@click.option(
    "--fast", is_flag=True, help="Optimize assembly code before generating executable"
)
@click.option("--version", is_flag=True, help="Displays the version of the compiler")
def main(source_file, asm, fast, version):
    global optimize
    if platform.system() != "Windows":
        click.echo(f"{RED}ERROR: This program is intended to run on Windows{RESET}")
        sys.exit(1)
    if platform.machine().lower() != "amd64":
        click.echo(
            f"{RED}ERROR: This program is intended to run on 64-bit Windows{RESET}"
        )
        sys.exit(1)
    if version:
        click.echo(f"{CYAN}NewYearLang Compiler version 2.2.9{RESET}")
        return
    if not source_file:
        click.echo(f"{RED}ERROR: No source file provided{RESET}")
        sys.exit(1)
    path = os.path.dirname(source_file)
    filename = os.path.basename(source_file).rsplit(".", 1)[0]
    try:
        with open(source_file, "r", encoding="utf-8") as f:
            source_code = f.read()
    except FileNotFoundError:
        click.echo(f"{RED}ERROR: File not found - '{source_file}'{RESET}")
        return
    except IOError as e:
        click.echo(f"{RED}ERROR: Unable to read file '{source_file}' - {e}{RESET}")
        return
    output_dir = os.path.join(path, "output")
    os.makedirs(output_dir, exist_ok=True)
    try:
        tokenizer = Tokenizer(source_code)
        tokens = tokenizer.tokenize()
        parser = Parser(tokens)
        prog = parser.parse_prog()
    except Exception as e:
        click.echo(f"{RED}COMPILER ERROR: Failed to parse source code - {e}{RESET}")
        return
    if fast:
        click.echo(
            f"{colorama.Fore.LIGHTYELLOW_EX}WARNING: Optimizing assembly code may cause errors. Proceeding...{RESET}"
        )
        optimize = True
    try:
        generator = Generator(prog)
        assembly_code = generator.gen_prog()
        asm_path = os.path.join(output_dir, filename + ".asm")
        with open(asm_path, "w", encoding="utf-8") as f:
            f.write(assembly_code)
        if asm:
            click.echo(f"{CYAN}Assembly code generated at {asm_path}{RESET}")
            return
        subprocess.run(
            ["nasm", "-Ox", "-f", "win64", asm_path], check=True, cwd=output_dir
        )
        subprocess.run(
            [
                "gcc",
                "-o",
                os.path.join(output_dir, filename + ".exe"),
                filename + ".obj",
            ],
            check=True,
            cwd=output_dir,
        )

        exe_path = os.path.join(output_dir, filename + ".exe")
        os.system(f'"{exe_path}"')
    except subprocess.CalledProcessError as e:
        click.echo(
            f"{RED}COMPILER ERROR: Command '{e.cmd}' failed with return code {e.returncode}{RESET}"
        )
    except FileNotFoundError as e:
        click.echo(f"{RED}COMPILER ERROR: File not found - '{e.filename}'{RESET}")
    except Exception as e:
        click.echo(f"{RED}COMPILER ERROR: {e}{RESET}")


if __name__ == "__main__":
    main()

# NewYear-Lang
```plain text
<Prog> ::= <Stmt>*

<Stmt> ::= 
    "Happynewyear" <Ident>                                         // return
    | "Peachblossom" <Ident> "=" <Expr>                            // var
    | "Caramelizedporkandeggs" <Expr> "{" <Scope> "}"              // if
    | "Firework" <Expr> "{" <Scope> "}"                            // while
    | "Countdown" <ForInit> <Expr> ";" <ForUpdate> "{" <Scope> "}" // for

<ForInit> ::= "Peachblossom" <Ident> "=" <Expr> ";"

<ForUpdate> ::= "Peachblossom" <Ident> "=" <Expr> ";"

<Scope> ::= <Stmt>*

<IfPred> ::= 
    "Chungcake" "{" <Scope> "}"                                    // else
    | ε
                                                          
<Expr> ::= <Term> 
    | <BinExpr>

<BinExpr> ::= <Expr> "*" <Expr>        {prec = 1}
    | <Expr> "/" <Expr>        {prec = 1}
    | <Expr> "+" <Expr>        {prec = 0}
    | <Expr> "-" <Expr>        {prec = 0}

<Term> ::= <IntLit> 
    | <Ident> 
    | "(" <Expr> ")"

<IntLit> ::= [0-9]+

<Ident> ::= [a-zA-Z_][a-zA-Z0-9_]*
```
The `Happynewyear` statement returns the value as an exit code. These exit codes can be accessed through system commands such as `echo $LASTEXITCODE` or `echo %errorlevel%`.

Requirement: `Python`, `Nasm`, `Gcc`

**🎆 Happy New Year 2025 🎇**

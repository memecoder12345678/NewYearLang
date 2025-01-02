# NewYearLang
```plain text
<Prog> ::= <Stmt>* 

<Stmt> ::= 
    "Happynewyear" <Ident> ";"                                     // print out the value of the variable
    | "Peachblossom" <Ident> "=" <Expr> ";"                        // var
    | "Caramelizedporkandeggs" <Expr> "{" <Scope> "}"              // if
    | "Firework" <Expr> "{" <Scope> "}"                            // while
    | "Countdown" <ForInit> <Expr> ";" <ForUpdate> "{" <Scope> "}" // for
    | "#" <Comment>                                                // comment

<ForInit> ::= "Peachblossom" <Ident> "=" <Expr> ";"

<ForUpdate> ::= "Peachblossom" <Ident> "=" <Expr> ";"

<Scope> ::= <Stmt>*

<Comment> ::= .*

<Expr> ::= <Term> 
    | <BinExpr>

<BinExpr> ::= <Expr> "*" <Expr>        {prec = 1}
    | <Expr> "/" <Expr>        {prec = 1}
    | <Expr> "+" <Expr>        {prec = 0}
    | <Expr> "-" <Expr>        {prec = 0}
    | <Expr> "==" <Expr>       {prec = 2}
    | <Expr> "!=" <Expr>       {prec = 2}
    | <Expr> "<" <Expr>        {prec = 2}
    | <Expr> ">" <Expr>        {prec = 2}
    | <Expr> "<=" <Expr>       {prec = 2}
    | <Expr> ">=" <Expr>       {prec = 2}

<Term> ::= <IntLit> 
    | <Ident> 
    | "(" <Expr> ")"

<IntLit> ::= [0-9]+

<Ident> ::= [a-zA-Z_][a-zA-Z0-9_]*
```
Requirement: `Python`, `Nasm`, `Gcc`

**🎆 Happy New Year 2025 🎇**

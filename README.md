# NewYearLang
**Syntax**:
```plain text
<Prog> ::= <Stmt>* 

<Stmt> ::= 
    "Happynewyear" <Expr> ";"                                      // print (cannot be used in loops)
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
**Result**:
```plain text
Python:
Days              : 0
Hours             : 0
Minutes           : 0
Seconds           : 45
Milliseconds      : 594
Ticks             : 455940774
TotalDays         : 0.000527709229166667
TotalHours        : 0.0126650215
TotalMinutes      : 0.75990129
TotalSeconds      : 45.5940774
TotalMilliseconds : 45594.0774

C:
Days              : 0
Hours             : 0
Minutes           : 0
Seconds           : 1
Milliseconds      : 443
Ticks             : 14437017
TotalDays         : 1.67095104166667E-05
TotalHours        : 0.00040102825
TotalMinutes      : 0.024061695
TotalSeconds      : 1.4437017
TotalMilliseconds : 1443.7017

C (-Ofast):
Days              : 0
Hours             : 0
Minutes           : 0
Seconds           : 0
Milliseconds      : 467
Ticks             : 4676065
TotalDays         : 5.41211226851852E-06
TotalHours        : 0.000129890694444444
TotalMinutes      : 0.00779344166666667
TotalSeconds      : 0.4676065
TotalMilliseconds : 467.6065

NewYearLang:
Days              : 0
Hours             : 0
Minutes           : 0
Seconds           : 4
Milliseconds      : 176
Ticks             : 41764280
TotalDays         : 4.8338287037037E-05
TotalHours        : 0.00116011888888889
TotalMinutes      : 0.0696071333333333
TotalSeconds      : 4.176428
TotalMilliseconds : 4176.428

NewYearLang (--fast):
Days              : 0
Hours             : 0
Minutes           : 0
Seconds           : 3
Milliseconds      : 509
Ticks             : 35094874
TotalDays         : 4.06190671296296E-05
TotalHours        : 0.000974857611111111
TotalMinutes      : 0.0584914566666667
TotalSeconds      : 3.5094874
TotalMilliseconds : 3509.4874
```
Requirement: `Python`, `Nasm`, `Gcc`

**🎆 Happy New Year 2025 🎇**

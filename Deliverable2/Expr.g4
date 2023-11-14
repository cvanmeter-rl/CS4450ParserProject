grammar Expr;

prog:   statement* EOF
    ;

statement:  expr
    | if_statement
    ;

if_statement
    : 'if' expr (condition_operator? expr)* ':' (INDENT statement)+ (elif_statement)* (else_statement)?
    ;

elif_statement
    : 'elif' expr (condition_operator? expr)* ':' INDENT statement+ 
    ;
else_statement
    : 'else' ':' (INDENT statement)+
    ;

expr:   ID assignment_operator operation          
    |   ID assignment_operator ID
    |   ID condition_operator ID
    |   ID condition_operator operation
    |   operation condition_operator ID
    |   '(' condition_operator ID ')'                                                  
    ;

operation
    :   operation arithmetic_operator operation
    |   INT
    |   FLOAT
    |   STRING
    |   LIST
    |   ID
    ;

arithmetic_operator
    :   '*'
    |   '/'
    |   '%'
    |   '+'
    |   '-'
    ;

assignment_operator
    :   '='
    |   '+='
    |   '-='
    |   '*='
    |   '/='
    ;
condition_operator
    :   '<'
    |   '<='
    |   '>'
    |   '>='
    |   '=='
    |   '!='
    |   'and'
    |   'or'
    |   'not'
    ;

ID  :   [a-zA-Z_] [a-zA-Z_0-9]* ;
INT :   '-'?[0-9]+ ;
FLOAT : [0-9]+ '.' [0-9]+ ;
STRING : ('"' | '\'') ( ~["\r\n] )* ('"' | '\'');
LIST : '[' (INT | FLOAT | STRING) (', ' (INT | FLOAT | STRING))* ']';

INDENT : '\t'; 
NEWLINE : '\r' ? '\n' -> skip;
WS :   [ \t]+ -> skip;
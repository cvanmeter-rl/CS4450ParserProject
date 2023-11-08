grammar Expr;

prog:   expr* EOF
    ;

expr:   ID assignment_operator operation          
    |   ID assignment_operator ID                                                   
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

ID  :   [a-zA-Z_] [a-zA-Z_0-9]* ;
INT :   [0-9]+ ;
FLOAT : [0-9]+ '.' [0-9]+ ;
STRING : ('"' | '\'') ( ~["\r\n] )* ('"' | '\'');
LIST : '[' (INT | FLOAT | STRING) (', ' (INT | FLOAT | STRING))* ']';

NEWLINE : '\r'? '\n' -> skip ;

WS  :   [ \t]+ -> skip ;
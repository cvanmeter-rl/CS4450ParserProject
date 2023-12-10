grammar Expr;

prog:   statement* EOF
    ;

statement: expr
    | MULTILINE_COMMENT
    | if_statement
    | while_statement
    | for_statement
    ;

for_statement
    : INDENT* 'for' ID 'in' iterable ':' (INDENT statement)+
    ;

while_statement
    : INDENT* 'while' expr (condition_operator? expr)* ':' (INDENT* statement)+
    ;

if_statement
    : INDENT* 'if' expr (condition_operator? expr)* ':' (INDENT* statement)+ (elif_statement)* (else_statement)?
    ;

elif_statement
    : INDENT* 'elif' expr (condition_operator? expr)* ':' INDENT* statement+ 
    ;
else_statement
    : INDENT* 'else' ':' (INDENT* statement)+
    ;

iterable
    : ID
    | RANGE
    ;

expr:   ID assignment_operator operation          
    |   ID assignment_operator ID
    |   ID condition_operator ID
    |   ID condition_operator operation
    |   operation condition_operator ID
    |   '(' expr ')'   
    |   condition_operator ID   
    |   BOOLEAN_LITERAL                                          
    ;

operation
    :   operation arithmetic_operator operation
    |   INT
    |   FLOAT
    |   STRINGD
    |   STRINGS
    |   LIST
    |   ID
    |   BOOLEAN_LITERAL 
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

BOOLEAN_LITERAL
    :   'True'
    |   'False'
    ;

ID  :   [a-zA-Z_] [a-zA-Z_0-9]* ;
INT :   '-'?[0-9]+ ;
FLOAT : [0-9]+ '.' [0-9]+ ;
STRINGD : (('"') ( ~["\r\n] )* ('"'));
STRINGS : (('\'') (~['\r\n])* ('\''));
LIST : '[' (INT | FLOAT | STRINGD | STRINGS) (', ' (INT | FLOAT | STRINGD | STRINGS))* ']';
RANGE : 'range(' INT ',' INT ')';

COMMENT
    :   '#' ~[\r\n]* -> skip
    ;

MULTILINE_COMMENT
    :   '\'\'\'' ID*.*? '\'\'\''
    ;

INDENT : '\t'; 
NEWLINE : '\r' ? '\n' -> skip;
WS :   [ \t]+ -> skip;
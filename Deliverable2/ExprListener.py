# Generated from Expr.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#prog.
    def enterProg(self, ctx:ExprParser.ProgContext):
        pass

    # Exit a parse tree produced by ExprParser#prog.
    def exitProg(self, ctx:ExprParser.ProgContext):
        pass


    # Enter a parse tree produced by ExprParser#statement.
    def enterStatement(self, ctx:ExprParser.StatementContext):
        pass

    # Exit a parse tree produced by ExprParser#statement.
    def exitStatement(self, ctx:ExprParser.StatementContext):
        pass


    # Enter a parse tree produced by ExprParser#if_statement.
    def enterIf_statement(self, ctx:ExprParser.If_statementContext):
        pass

    # Exit a parse tree produced by ExprParser#if_statement.
    def exitIf_statement(self, ctx:ExprParser.If_statementContext):
        pass


    # Enter a parse tree produced by ExprParser#elif_statement.
    def enterElif_statement(self, ctx:ExprParser.Elif_statementContext):
        pass

    # Exit a parse tree produced by ExprParser#elif_statement.
    def exitElif_statement(self, ctx:ExprParser.Elif_statementContext):
        pass


    # Enter a parse tree produced by ExprParser#else_statement.
    def enterElse_statement(self, ctx:ExprParser.Else_statementContext):
        pass

    # Exit a parse tree produced by ExprParser#else_statement.
    def exitElse_statement(self, ctx:ExprParser.Else_statementContext):
        pass


    # Enter a parse tree produced by ExprParser#expr.
    def enterExpr(self, ctx:ExprParser.ExprContext):
        pass

    # Exit a parse tree produced by ExprParser#expr.
    def exitExpr(self, ctx:ExprParser.ExprContext):
        pass


    # Enter a parse tree produced by ExprParser#operation.
    def enterOperation(self, ctx:ExprParser.OperationContext):
        pass

    # Exit a parse tree produced by ExprParser#operation.
    def exitOperation(self, ctx:ExprParser.OperationContext):
        pass


    # Enter a parse tree produced by ExprParser#arithmetic_operator.
    def enterArithmetic_operator(self, ctx:ExprParser.Arithmetic_operatorContext):
        pass

    # Exit a parse tree produced by ExprParser#arithmetic_operator.
    def exitArithmetic_operator(self, ctx:ExprParser.Arithmetic_operatorContext):
        pass


    # Enter a parse tree produced by ExprParser#assignment_operator.
    def enterAssignment_operator(self, ctx:ExprParser.Assignment_operatorContext):
        pass

    # Exit a parse tree produced by ExprParser#assignment_operator.
    def exitAssignment_operator(self, ctx:ExprParser.Assignment_operatorContext):
        pass


    # Enter a parse tree produced by ExprParser#condition_operator.
    def enterCondition_operator(self, ctx:ExprParser.Condition_operatorContext):
        pass

    # Exit a parse tree produced by ExprParser#condition_operator.
    def exitCondition_operator(self, ctx:ExprParser.Condition_operatorContext):
        pass



del ExprParser
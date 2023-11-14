# Generated from Expr.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,33,136,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,5,0,22,8,0,10,0,12,0,25,9,0,1,0,1,
        0,1,1,1,1,3,1,31,8,1,1,2,1,2,1,2,3,2,36,8,2,1,2,5,2,39,8,2,10,2,
        12,2,42,9,2,1,2,1,2,1,2,4,2,47,8,2,11,2,12,2,48,1,2,5,2,52,8,2,10,
        2,12,2,55,9,2,1,2,3,2,58,8,2,1,3,1,3,1,3,3,3,63,8,3,1,3,5,3,66,8,
        3,10,3,12,3,69,9,3,1,3,1,3,1,3,4,3,74,8,3,11,3,12,3,75,1,4,1,4,1,
        4,1,4,4,4,82,8,4,11,4,12,4,83,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,3,5,111,8,5,1,6,1,6,1,6,1,6,1,6,1,6,3,6,119,8,6,1,6,1,6,1,6,1,
        6,5,6,125,8,6,10,6,12,6,128,9,6,1,7,1,7,1,8,1,8,1,9,1,9,1,9,0,1,
        12,10,0,2,4,6,8,10,12,14,16,18,0,3,1,0,7,11,1,0,12,16,1,0,17,25,
        146,0,23,1,0,0,0,2,30,1,0,0,0,4,32,1,0,0,0,6,59,1,0,0,0,8,77,1,0,
        0,0,10,110,1,0,0,0,12,118,1,0,0,0,14,129,1,0,0,0,16,131,1,0,0,0,
        18,133,1,0,0,0,20,22,3,2,1,0,21,20,1,0,0,0,22,25,1,0,0,0,23,21,1,
        0,0,0,23,24,1,0,0,0,24,26,1,0,0,0,25,23,1,0,0,0,26,27,5,0,0,1,27,
        1,1,0,0,0,28,31,3,10,5,0,29,31,3,4,2,0,30,28,1,0,0,0,30,29,1,0,0,
        0,31,3,1,0,0,0,32,33,5,1,0,0,33,40,3,10,5,0,34,36,3,18,9,0,35,34,
        1,0,0,0,35,36,1,0,0,0,36,37,1,0,0,0,37,39,3,10,5,0,38,35,1,0,0,0,
        39,42,1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,43,1,0,0,0,42,40,1,
        0,0,0,43,46,5,2,0,0,44,45,5,31,0,0,45,47,3,2,1,0,46,44,1,0,0,0,47,
        48,1,0,0,0,48,46,1,0,0,0,48,49,1,0,0,0,49,53,1,0,0,0,50,52,3,6,3,
        0,51,50,1,0,0,0,52,55,1,0,0,0,53,51,1,0,0,0,53,54,1,0,0,0,54,57,
        1,0,0,0,55,53,1,0,0,0,56,58,3,8,4,0,57,56,1,0,0,0,57,58,1,0,0,0,
        58,5,1,0,0,0,59,60,5,3,0,0,60,67,3,10,5,0,61,63,3,18,9,0,62,61,1,
        0,0,0,62,63,1,0,0,0,63,64,1,0,0,0,64,66,3,10,5,0,65,62,1,0,0,0,66,
        69,1,0,0,0,67,65,1,0,0,0,67,68,1,0,0,0,68,70,1,0,0,0,69,67,1,0,0,
        0,70,71,5,2,0,0,71,73,5,31,0,0,72,74,3,2,1,0,73,72,1,0,0,0,74,75,
        1,0,0,0,75,73,1,0,0,0,75,76,1,0,0,0,76,7,1,0,0,0,77,78,5,4,0,0,78,
        81,5,2,0,0,79,80,5,31,0,0,80,82,3,2,1,0,81,79,1,0,0,0,82,83,1,0,
        0,0,83,81,1,0,0,0,83,84,1,0,0,0,84,9,1,0,0,0,85,86,5,26,0,0,86,87,
        3,16,8,0,87,88,3,12,6,0,88,111,1,0,0,0,89,90,5,26,0,0,90,91,3,16,
        8,0,91,92,5,26,0,0,92,111,1,0,0,0,93,94,5,26,0,0,94,95,3,18,9,0,
        95,96,5,26,0,0,96,111,1,0,0,0,97,98,5,26,0,0,98,99,3,18,9,0,99,100,
        3,12,6,0,100,111,1,0,0,0,101,102,3,12,6,0,102,103,3,18,9,0,103,104,
        5,26,0,0,104,111,1,0,0,0,105,106,5,5,0,0,106,107,3,18,9,0,107,108,
        5,26,0,0,108,109,5,6,0,0,109,111,1,0,0,0,110,85,1,0,0,0,110,89,1,
        0,0,0,110,93,1,0,0,0,110,97,1,0,0,0,110,101,1,0,0,0,110,105,1,0,
        0,0,111,11,1,0,0,0,112,113,6,6,-1,0,113,119,5,27,0,0,114,119,5,28,
        0,0,115,119,5,29,0,0,116,119,5,30,0,0,117,119,5,26,0,0,118,112,1,
        0,0,0,118,114,1,0,0,0,118,115,1,0,0,0,118,116,1,0,0,0,118,117,1,
        0,0,0,119,126,1,0,0,0,120,121,10,6,0,0,121,122,3,14,7,0,122,123,
        3,12,6,7,123,125,1,0,0,0,124,120,1,0,0,0,125,128,1,0,0,0,126,124,
        1,0,0,0,126,127,1,0,0,0,127,13,1,0,0,0,128,126,1,0,0,0,129,130,7,
        0,0,0,130,15,1,0,0,0,131,132,7,1,0,0,132,17,1,0,0,0,133,134,7,2,
        0,0,134,19,1,0,0,0,14,23,30,35,40,48,53,57,62,67,75,83,110,118,126
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "':'", "'elif'", "'else'", "'('", 
                     "')'", "'*'", "'/'", "'%'", "'+'", "'-'", "'='", "'+='", 
                     "'-='", "'*='", "'/='", "'<'", "'<='", "'>'", "'>='", 
                     "'=='", "'!='", "'and'", "'or'", "'not'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'\\t'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID", "INT", "FLOAT", "STRING", 
                      "LIST", "INDENT", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_statement = 1
    RULE_if_statement = 2
    RULE_elif_statement = 3
    RULE_else_statement = 4
    RULE_expr = 5
    RULE_operation = 6
    RULE_arithmetic_operator = 7
    RULE_assignment_operator = 8
    RULE_condition_operator = 9

    ruleNames =  [ "prog", "statement", "if_statement", "elif_statement", 
                   "else_statement", "expr", "operation", "arithmetic_operator", 
                   "assignment_operator", "condition_operator" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    ID=26
    INT=27
    FLOAT=28
    STRING=29
    LIST=30
    INDENT=31
    NEWLINE=32
    WS=33

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatementContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatementContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = ExprParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2080374818) != 0):
                self.state = 20
                self.statement()
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 26
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(ExprParser.If_statementContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = ExprParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 30
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 26, 27, 28, 29, 30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.expr()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.if_statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def INDENT(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.INDENT)
            else:
                return self.getToken(ExprParser.INDENT, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatementContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatementContext,i)


        def elif_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.Elif_statementContext)
            else:
                return self.getTypedRuleContext(ExprParser.Elif_statementContext,i)


        def else_statement(self):
            return self.getTypedRuleContext(ExprParser.Else_statementContext,0)


        def condition_operator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.Condition_operatorContext)
            else:
                return self.getTypedRuleContext(ExprParser.Condition_operatorContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_if_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_statement" ):
                listener.enterIf_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_statement" ):
                listener.exitIf_statement(self)




    def if_statement(self):

        localctx = ExprParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(ExprParser.T__0)
            self.state = 33
            self.expr()
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2147352608) != 0):
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 66977792) != 0):
                    self.state = 34
                    self.condition_operator()


                self.state = 37
                self.expr()
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 43
            self.match(ExprParser.T__1)
            self.state = 46 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 44
                    self.match(ExprParser.INDENT)
                    self.state = 45
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 48 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 53
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 50
                    self.elif_statement() 
                self.state = 55
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

            self.state = 57
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 56
                self.else_statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elif_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def INDENT(self):
            return self.getToken(ExprParser.INDENT, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatementContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatementContext,i)


        def condition_operator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.Condition_operatorContext)
            else:
                return self.getTypedRuleContext(ExprParser.Condition_operatorContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_elif_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElif_statement" ):
                listener.enterElif_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElif_statement" ):
                listener.exitElif_statement(self)




    def elif_statement(self):

        localctx = ExprParser.Elif_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_elif_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(ExprParser.T__2)
            self.state = 60
            self.expr()
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2147352608) != 0):
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 66977792) != 0):
                    self.state = 61
                    self.condition_operator()


                self.state = 64
                self.expr()
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 70
            self.match(ExprParser.T__1)
            self.state = 71
            self.match(ExprParser.INDENT)
            self.state = 73 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 72
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 75 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INDENT(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.INDENT)
            else:
                return self.getToken(ExprParser.INDENT, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatementContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatementContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_else_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElse_statement" ):
                listener.enterElse_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElse_statement" ):
                listener.exitElse_statement(self)




    def else_statement(self):

        localctx = ExprParser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(ExprParser.T__3)
            self.state = 78
            self.match(ExprParser.T__1)
            self.state = 81 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 79
                    self.match(ExprParser.INDENT)
                    self.state = 80
                    self.statement()

                else:
                    raise NoViableAltException(self)
                self.state = 83 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.ID)
            else:
                return self.getToken(ExprParser.ID, i)

        def assignment_operator(self):
            return self.getTypedRuleContext(ExprParser.Assignment_operatorContext,0)


        def operation(self):
            return self.getTypedRuleContext(ExprParser.OperationContext,0)


        def condition_operator(self):
            return self.getTypedRuleContext(ExprParser.Condition_operatorContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = ExprParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expr)
        try:
            self.state = 110
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.match(ExprParser.ID)
                self.state = 86
                self.assignment_operator()
                self.state = 87
                self.operation(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 89
                self.match(ExprParser.ID)
                self.state = 90
                self.assignment_operator()
                self.state = 91
                self.match(ExprParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 93
                self.match(ExprParser.ID)
                self.state = 94
                self.condition_operator()
                self.state = 95
                self.match(ExprParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 97
                self.match(ExprParser.ID)
                self.state = 98
                self.condition_operator()
                self.state = 99
                self.operation(0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 101
                self.operation(0)
                self.state = 102
                self.condition_operator()
                self.state = 103
                self.match(ExprParser.ID)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 105
                self.match(ExprParser.T__4)
                self.state = 106
                self.condition_operator()
                self.state = 107
                self.match(ExprParser.ID)
                self.state = 108
                self.match(ExprParser.T__5)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(ExprParser.INT, 0)

        def FLOAT(self):
            return self.getToken(ExprParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(ExprParser.STRING, 0)

        def LIST(self):
            return self.getToken(ExprParser.LIST, 0)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def operation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.OperationContext)
            else:
                return self.getTypedRuleContext(ExprParser.OperationContext,i)


        def arithmetic_operator(self):
            return self.getTypedRuleContext(ExprParser.Arithmetic_operatorContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_operation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperation" ):
                listener.enterOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperation" ):
                listener.exitOperation(self)



    def operation(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.OperationContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_operation, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.state = 113
                self.match(ExprParser.INT)
                pass
            elif token in [28]:
                self.state = 114
                self.match(ExprParser.FLOAT)
                pass
            elif token in [29]:
                self.state = 115
                self.match(ExprParser.STRING)
                pass
            elif token in [30]:
                self.state = 116
                self.match(ExprParser.LIST)
                pass
            elif token in [26]:
                self.state = 117
                self.match(ExprParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 126
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExprParser.OperationContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_operation)
                    self.state = 120
                    if not self.precpred(self._ctx, 6):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                    self.state = 121
                    self.arithmetic_operator()
                    self.state = 122
                    self.operation(7) 
                self.state = 128
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Arithmetic_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_arithmetic_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmetic_operator" ):
                listener.enterArithmetic_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmetic_operator" ):
                listener.exitArithmetic_operator(self)




    def arithmetic_operator(self):

        localctx = ExprParser.Arithmetic_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_arithmetic_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3968) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_assignment_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment_operator" ):
                listener.enterAssignment_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment_operator" ):
                listener.exitAssignment_operator(self)




    def assignment_operator(self):

        localctx = ExprParser.Assignment_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_assignment_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 126976) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Condition_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_condition_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition_operator" ):
                listener.enterCondition_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition_operator" ):
                listener.exitCondition_operator(self)




    def condition_operator(self):

        localctx = ExprParser.Condition_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_condition_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 66977792) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.operation_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def operation_sempred(self, localctx:OperationContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         





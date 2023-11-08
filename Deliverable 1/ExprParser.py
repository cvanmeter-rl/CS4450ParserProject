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
        4,1,17,50,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,5,0,12,8,0,
        10,0,12,0,15,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,27,
        8,1,1,2,1,2,1,2,1,2,1,2,1,2,3,2,35,8,2,1,2,1,2,1,2,1,2,5,2,41,8,
        2,10,2,12,2,44,9,2,1,3,1,3,1,4,1,4,1,4,0,1,4,5,0,2,4,6,8,0,2,1,0,
        1,5,1,0,6,10,51,0,13,1,0,0,0,2,26,1,0,0,0,4,34,1,0,0,0,6,45,1,0,
        0,0,8,47,1,0,0,0,10,12,3,2,1,0,11,10,1,0,0,0,12,15,1,0,0,0,13,11,
        1,0,0,0,13,14,1,0,0,0,14,16,1,0,0,0,15,13,1,0,0,0,16,17,5,0,0,1,
        17,1,1,0,0,0,18,19,5,11,0,0,19,20,3,8,4,0,20,21,3,4,2,0,21,27,1,
        0,0,0,22,23,5,11,0,0,23,24,3,8,4,0,24,25,5,11,0,0,25,27,1,0,0,0,
        26,18,1,0,0,0,26,22,1,0,0,0,27,3,1,0,0,0,28,29,6,2,-1,0,29,35,5,
        12,0,0,30,35,5,13,0,0,31,35,5,14,0,0,32,35,5,15,0,0,33,35,5,11,0,
        0,34,28,1,0,0,0,34,30,1,0,0,0,34,31,1,0,0,0,34,32,1,0,0,0,34,33,
        1,0,0,0,35,42,1,0,0,0,36,37,10,6,0,0,37,38,3,6,3,0,38,39,3,4,2,7,
        39,41,1,0,0,0,40,36,1,0,0,0,41,44,1,0,0,0,42,40,1,0,0,0,42,43,1,
        0,0,0,43,5,1,0,0,0,44,42,1,0,0,0,45,46,7,0,0,0,46,7,1,0,0,0,47,48,
        7,1,0,0,48,9,1,0,0,0,4,13,26,34,42
    ]

class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'*'", "'/'", "'%'", "'+'", "'-'", "'='", 
                     "'+='", "'-='", "'*='", "'/='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "INT", 
                      "FLOAT", "STRING", "LIST", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_expr = 1
    RULE_operation = 2
    RULE_arithmetic_operator = 3
    RULE_assignment_operator = 4

    ruleNames =  [ "prog", "expr", "operation", "arithmetic_operator", "assignment_operator" ]

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
    ID=11
    INT=12
    FLOAT=13
    STRING=14
    LIST=15
    NEWLINE=16
    WS=17

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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


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
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 10
                self.expr()
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 16
            self.match(ExprParser.EOF)
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
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.state = 26
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                self.match(ExprParser.ID)
                self.state = 19
                self.assignment_operator()
                self.state = 20
                self.operation(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 22
                self.match(ExprParser.ID)
                self.state = 23
                self.assignment_operator()
                self.state = 24
                self.match(ExprParser.ID)
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
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_operation, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.state = 29
                self.match(ExprParser.INT)
                pass
            elif token in [13]:
                self.state = 30
                self.match(ExprParser.FLOAT)
                pass
            elif token in [14]:
                self.state = 31
                self.match(ExprParser.STRING)
                pass
            elif token in [15]:
                self.state = 32
                self.match(ExprParser.LIST)
                pass
            elif token in [11]:
                self.state = 33
                self.match(ExprParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 42
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExprParser.OperationContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_operation)
                    self.state = 36
                    if not self.precpred(self._ctx, 6):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                    self.state = 37
                    self.arithmetic_operator()
                    self.state = 38
                    self.operation(7) 
                self.state = 44
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

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
        self.enterRule(localctx, 6, self.RULE_arithmetic_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 62) != 0)):
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
        self.enterRule(localctx, 8, self.RULE_assignment_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1984) != 0)):
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
        self._predicates[2] = self.operation_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def operation_sempred(self, localctx:OperationContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         





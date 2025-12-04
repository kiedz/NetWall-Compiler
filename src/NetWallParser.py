# Generated from src/NetWall.g4 by ANTLR 4.13.1
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
        4,1,14,49,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,4,0,12,8,0,
        11,0,12,0,13,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        4,1,29,8,1,11,1,12,1,30,1,1,1,1,3,1,35,8,1,1,2,1,2,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,0,0,5,0,2,4,6,8,0,1,1,0,8,9,46,0,11,
        1,0,0,0,2,34,1,0,0,0,4,36,1,0,0,0,6,38,1,0,0,0,8,46,1,0,0,0,10,12,
        3,2,1,0,11,10,1,0,0,0,12,13,1,0,0,0,13,11,1,0,0,0,13,14,1,0,0,0,
        14,1,1,0,0,0,15,16,3,4,2,0,16,17,5,11,0,0,17,18,5,1,0,0,18,19,3,
        6,3,0,19,20,5,2,0,0,20,21,5,3,0,0,21,22,3,8,4,0,22,23,5,4,0,0,23,
        35,1,0,0,0,24,25,5,5,0,0,25,26,5,12,0,0,26,28,5,6,0,0,27,29,3,2,
        1,0,28,27,1,0,0,0,29,30,1,0,0,0,30,28,1,0,0,0,30,31,1,0,0,0,31,32,
        1,0,0,0,32,33,5,7,0,0,33,35,1,0,0,0,34,15,1,0,0,0,34,24,1,0,0,0,
        35,3,1,0,0,0,36,37,7,0,0,0,37,5,1,0,0,0,38,39,5,13,0,0,39,40,5,10,
        0,0,40,41,5,13,0,0,41,42,5,10,0,0,42,43,5,13,0,0,43,44,5,10,0,0,
        44,45,5,13,0,0,45,7,1,0,0,0,46,47,5,13,0,0,47,9,1,0,0,0,3,13,30,
        34
    ]

class NetWallParser ( Parser ):

    grammarFileName = "NetWall.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'from'", "'to'", "'port'", "';'", "'group'", 
                     "'{'", "'}'", "'allow'", "'block'", "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "PROTOCOL", 
                      "ID", "INT", "WS" ]

    RULE_prog = 0
    RULE_statement = 1
    RULE_action = 2
    RULE_ip_address = 3
    RULE_port_num = 4

    ruleNames =  [ "prog", "statement", "action", "ip_address", "port_num" ]

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
    PROTOCOL=11
    ID=12
    INT=13
    WS=14

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

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NetWallParser.StatementContext)
            else:
                return self.getTypedRuleContext(NetWallParser.StatementContext,i)


        def getRuleIndex(self):
            return NetWallParser.RULE_prog

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = NetWallParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.statement()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 800) != 0)):
                    break

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


        def getRuleIndex(self):
            return NetWallParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class RuleGroupContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a NetWallParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(NetWallParser.ID, 0)
        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NetWallParser.StatementContext)
            else:
                return self.getTypedRuleContext(NetWallParser.StatementContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRuleGroup" ):
                return visitor.visitRuleGroup(self)
            else:
                return visitor.visitChildren(self)


    class RuleNormalContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a NetWallParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def action(self):
            return self.getTypedRuleContext(NetWallParser.ActionContext,0)

        def PROTOCOL(self):
            return self.getToken(NetWallParser.PROTOCOL, 0)
        def ip_address(self):
            return self.getTypedRuleContext(NetWallParser.Ip_addressContext,0)

        def port_num(self):
            return self.getTypedRuleContext(NetWallParser.Port_numContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRuleNormal" ):
                return visitor.visitRuleNormal(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = NetWallParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 34
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 9]:
                localctx = NetWallParser.RuleNormalContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.action()
                self.state = 16
                self.match(NetWallParser.PROTOCOL)
                self.state = 17
                self.match(NetWallParser.T__0)
                self.state = 18
                self.ip_address()
                self.state = 19
                self.match(NetWallParser.T__1)
                self.state = 20
                self.match(NetWallParser.T__2)
                self.state = 21
                self.port_num()
                self.state = 22
                self.match(NetWallParser.T__3)
                pass
            elif token in [5]:
                localctx = NetWallParser.RuleGroupContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.match(NetWallParser.T__4)
                self.state = 25
                self.match(NetWallParser.ID)
                self.state = 26
                self.match(NetWallParser.T__5)
                self.state = 28 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 27
                    self.statement()
                    self.state = 30 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 800) != 0)):
                        break

                self.state = 32
                self.match(NetWallParser.T__6)
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


    class ActionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return NetWallParser.RULE_action

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAction" ):
                return visitor.visitAction(self)
            else:
                return visitor.visitChildren(self)




    def action(self):

        localctx = NetWallParser.ActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_action)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            _la = self._input.LA(1)
            if not(_la==8 or _la==9):
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


    class Ip_addressContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(NetWallParser.INT)
            else:
                return self.getToken(NetWallParser.INT, i)

        def getRuleIndex(self):
            return NetWallParser.RULE_ip_address

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIp_address" ):
                return visitor.visitIp_address(self)
            else:
                return visitor.visitChildren(self)




    def ip_address(self):

        localctx = NetWallParser.Ip_addressContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_ip_address)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(NetWallParser.INT)
            self.state = 39
            self.match(NetWallParser.T__9)
            self.state = 40
            self.match(NetWallParser.INT)
            self.state = 41
            self.match(NetWallParser.T__9)
            self.state = 42
            self.match(NetWallParser.INT)
            self.state = 43
            self.match(NetWallParser.T__9)
            self.state = 44
            self.match(NetWallParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Port_numContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(NetWallParser.INT, 0)

        def getRuleIndex(self):
            return NetWallParser.RULE_port_num

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPort_num" ):
                return visitor.visitPort_num(self)
            else:
                return visitor.visitChildren(self)




    def port_num(self):

        localctx = NetWallParser.Port_numContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_port_num)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(NetWallParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






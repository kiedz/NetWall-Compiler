# Generated from src/NetWall.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .NetWallParser import NetWallParser
else:
    from NetWallParser import NetWallParser

# This class defines a complete generic visitor for a parse tree produced by NetWallParser.

class NetWallVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by NetWallParser#prog.
    def visitProg(self, ctx:NetWallParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetWallParser#RuleNormal.
    def visitRuleNormal(self, ctx:NetWallParser.RuleNormalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetWallParser#RuleGroup.
    def visitRuleGroup(self, ctx:NetWallParser.RuleGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetWallParser#action.
    def visitAction(self, ctx:NetWallParser.ActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetWallParser#ip_address.
    def visitIp_address(self, ctx:NetWallParser.Ip_addressContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NetWallParser#port_num.
    def visitPort_num(self, ctx:NetWallParser.Port_numContext):
        return self.visitChildren(ctx)



del NetWallParser
import sys
from antlr4 import *
from NetWallLexer import NetWallLexer
from NetWallParser import NetWallParser
from NetWallVisitor import NetWallVisitor

#Implementação do Visitor (percorre a árvore e gera código)
class NetWallCompiler(NetWallVisitor):
    def __init__(self):
        self.output = []

    #Visitante para regras normais (allow/block)
    def visitRuleNormal(self, ctx):
        action_text = ctx.action().getText()
        protocol = ctx.PROTOCOL().getText()
        ip = ctx.ip_address().getText()
        port = ctx.port_num().getText()

        target = "ACCEPT" if action_text == "allow" else "DROP"
        command = f"iptables -A INPUT -p {protocol} -s {ip} --dport {port} -j {target}"
        
        self.output.append(command)
        return self.visitChildren(ctx)

    #Visitante para grupos (só para continuar visitando os filhos dentro do grupo)
    def visitRuleGroup(self, ctx):
        group_name = ctx.ID().getText()
        self.output.append(f"# Inicio do grupo: {group_name}")
        self.visitChildren(ctx) # Visita as regras dentro das chaves
        self.output.append(f"# Fim do grupo: {group_name}")

    def get_output(self):
        return "\n".join(self.output)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python main.py <arquivo_entrada.nw>")
        sys.exit(1)

    input_file = sys.argv[1]
    
    #1. Ler o arquivo (Lexer)
    input_stream = FileStream(input_file)
    lexer = NetWallLexer(input_stream)
    stream = CommonTokenStream(lexer)
    
    #2. Analisar a estrutura (Parser)
    parser = NetWallParser(stream)
    tree = parser.prog()
    
    #3. Gerar código (Visitor)
    compiler = NetWallCompiler()
    compiler.visit(tree)
    
    #4. Imprimir resultado
    print("#!/bin/bash")
    print("# Script gerado automaticamente pelo NetWall Compiler")
    print(compiler.get_output())
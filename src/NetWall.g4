grammar NetWall;

prog: statement+ ;

//Declarações
statement: action PROTOCOL 'from' ip_address 'to' 'port' port_num ';' # RuleNormal
         | 'group' ID '{' statement+ '}'                              # RuleGroup
         ;

//Tokens
action: 'allow' | 'block';

PROTOCOL: 'TCP' | 'UDP';

ip_address: INT '.' INT '.' INT '.' INT;

port_num: INT;

ID: [a-zA-Z]+;
INT: [0-9]+;

WS: [ \t\r\n]+ -> skip;
// Generated from /workspaces/NetWall-Compiler/src/NetWall.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class NetWallParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, PROTOCOL=11, ID=12, INT=13, WS=14;
	public static final int
		RULE_prog = 0, RULE_statement = 1, RULE_action = 2, RULE_ip_address = 3, 
		RULE_port_num = 4;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "statement", "action", "ip_address", "port_num"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'from'", "'to'", "'port'", "';'", "'group'", "'{'", "'}'", "'allow'", 
			"'block'", "'.'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, "PROTOCOL", 
			"ID", "INT", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "NetWall.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public NetWallParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgContext extends ParserRuleContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_prog);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(11); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(10);
				statement();
				}
				}
				setState(13); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 800L) != 0) );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	 
		public StatementContext() { }
		public void copyFrom(StatementContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class RuleGroupContext extends StatementContext {
		public TerminalNode ID() { return getToken(NetWallParser.ID, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public RuleGroupContext(StatementContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class RuleNormalContext extends StatementContext {
		public ActionContext action() {
			return getRuleContext(ActionContext.class,0);
		}
		public TerminalNode PROTOCOL() { return getToken(NetWallParser.PROTOCOL, 0); }
		public Ip_addressContext ip_address() {
			return getRuleContext(Ip_addressContext.class,0);
		}
		public Port_numContext port_num() {
			return getRuleContext(Port_numContext.class,0);
		}
		public RuleNormalContext(StatementContext ctx) { copyFrom(ctx); }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statement);
		int _la;
		try {
			setState(34);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__7:
			case T__8:
				_localctx = new RuleNormalContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(15);
				action();
				setState(16);
				match(PROTOCOL);
				setState(17);
				match(T__0);
				setState(18);
				ip_address();
				setState(19);
				match(T__1);
				setState(20);
				match(T__2);
				setState(21);
				port_num();
				setState(22);
				match(T__3);
				}
				break;
			case T__4:
				_localctx = new RuleGroupContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(24);
				match(T__4);
				setState(25);
				match(ID);
				setState(26);
				match(T__5);
				setState(28); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(27);
					statement();
					}
					}
					setState(30); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 800L) != 0) );
				setState(32);
				match(T__6);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ActionContext extends ParserRuleContext {
		public ActionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_action; }
	}

	public final ActionContext action() throws RecognitionException {
		ActionContext _localctx = new ActionContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_action);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(36);
			_la = _input.LA(1);
			if ( !(_la==T__7 || _la==T__8) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Ip_addressContext extends ParserRuleContext {
		public List<TerminalNode> INT() { return getTokens(NetWallParser.INT); }
		public TerminalNode INT(int i) {
			return getToken(NetWallParser.INT, i);
		}
		public Ip_addressContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ip_address; }
	}

	public final Ip_addressContext ip_address() throws RecognitionException {
		Ip_addressContext _localctx = new Ip_addressContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_ip_address);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(38);
			match(INT);
			setState(39);
			match(T__9);
			setState(40);
			match(INT);
			setState(41);
			match(T__9);
			setState(42);
			match(INT);
			setState(43);
			match(T__9);
			setState(44);
			match(INT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Port_numContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(NetWallParser.INT, 0); }
		public Port_numContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_port_num; }
	}

	public final Port_numContext port_num() throws RecognitionException {
		Port_numContext _localctx = new Port_numContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_port_num);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(46);
			match(INT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u000e1\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0001"+
		"\u0000\u0004\u0000\f\b\u0000\u000b\u0000\f\u0000\r\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0004\u0001"+
		"\u001d\b\u0001\u000b\u0001\f\u0001\u001e\u0001\u0001\u0001\u0001\u0003"+
		"\u0001#\b\u0001\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0000\u0000\u0005\u0000\u0002\u0004\u0006"+
		"\b\u0000\u0001\u0001\u0000\b\t.\u0000\u000b\u0001\u0000\u0000\u0000\u0002"+
		"\"\u0001\u0000\u0000\u0000\u0004$\u0001\u0000\u0000\u0000\u0006&\u0001"+
		"\u0000\u0000\u0000\b.\u0001\u0000\u0000\u0000\n\f\u0003\u0002\u0001\u0000"+
		"\u000b\n\u0001\u0000\u0000\u0000\f\r\u0001\u0000\u0000\u0000\r\u000b\u0001"+
		"\u0000\u0000\u0000\r\u000e\u0001\u0000\u0000\u0000\u000e\u0001\u0001\u0000"+
		"\u0000\u0000\u000f\u0010\u0003\u0004\u0002\u0000\u0010\u0011\u0005\u000b"+
		"\u0000\u0000\u0011\u0012\u0005\u0001\u0000\u0000\u0012\u0013\u0003\u0006"+
		"\u0003\u0000\u0013\u0014\u0005\u0002\u0000\u0000\u0014\u0015\u0005\u0003"+
		"\u0000\u0000\u0015\u0016\u0003\b\u0004\u0000\u0016\u0017\u0005\u0004\u0000"+
		"\u0000\u0017#\u0001\u0000\u0000\u0000\u0018\u0019\u0005\u0005\u0000\u0000"+
		"\u0019\u001a\u0005\f\u0000\u0000\u001a\u001c\u0005\u0006\u0000\u0000\u001b"+
		"\u001d\u0003\u0002\u0001\u0000\u001c\u001b\u0001\u0000\u0000\u0000\u001d"+
		"\u001e\u0001\u0000\u0000\u0000\u001e\u001c\u0001\u0000\u0000\u0000\u001e"+
		"\u001f\u0001\u0000\u0000\u0000\u001f \u0001\u0000\u0000\u0000 !\u0005"+
		"\u0007\u0000\u0000!#\u0001\u0000\u0000\u0000\"\u000f\u0001\u0000\u0000"+
		"\u0000\"\u0018\u0001\u0000\u0000\u0000#\u0003\u0001\u0000\u0000\u0000"+
		"$%\u0007\u0000\u0000\u0000%\u0005\u0001\u0000\u0000\u0000&\'\u0005\r\u0000"+
		"\u0000\'(\u0005\n\u0000\u0000()\u0005\r\u0000\u0000)*\u0005\n\u0000\u0000"+
		"*+\u0005\r\u0000\u0000+,\u0005\n\u0000\u0000,-\u0005\r\u0000\u0000-\u0007"+
		"\u0001\u0000\u0000\u0000./\u0005\r\u0000\u0000/\t\u0001\u0000\u0000\u0000"+
		"\u0003\r\u001e\"";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
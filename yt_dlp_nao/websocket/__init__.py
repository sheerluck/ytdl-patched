from __future__ import unicode_literals

HAVE_WEBSOCKET = False
WebSocket = None

# WebSocket: (URI, header={'Accept': 'nothing', 'X-Magic-Number': '42'})->WebSocket
# only send, recv, close are guaranteed to exist

HAVE_WS_WEBSOCKET_CLIENT, HAVE_WS_WEBSOCKETS = False, False

try:
    from websocket import create_connection, WebSocket

    def _enter(self):
        return self

    def _exit(self, type, value, traceback):
        self.close()

    WebSocket.__enter__ = _enter
    WebSocket.__exit__ = _exit

    def WebSocketClientWrapper(url, headers={}):
        return create_connection(url, headers=['%s: %s' % kv for kv in headers.items()])

    HAVE_WS_WEBSOCKET_CLIENT = True
    HAVE_WEBSOCKET = True
except (ImportError, ValueError, SyntaxError):
    WebSocketClientWrapper = None

try:
    from .websockets import WebSocketsWrapper
    HAVE_WS_WEBSOCKETS = True
    HAVE_WEBSOCKET = True
except (ImportError, ValueError, SyntaxError):
    WebSocketsWrapper = None

WebSocket = (WebSocketClientWrapper or WebSocketsWrapper) if HAVE_WEBSOCKET else None

# NOTE: directly importing this module is now deprecated. import via .dependencies

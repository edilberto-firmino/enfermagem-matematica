#!/usr/bin/env python3
"""
Servidor web para servir o mapa de calor de Fortaleza
Execute: python3 servidor_web.py
Acesse: http://localhost:8000
"""

from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
import webbrowser
from threading import Timer

# Mudar para o diretório do projeto
os.chdir('/Users/macbook/projects/enf-matematica')

class MyHTTPRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Adicionar headers para melhor compatibilidade
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def log_message(self, format, *args):
        # Log customizado
        print(f"[SERVIDOR] {format % args}")

def abrir_navegador():
    """Abre o navegador automaticamente após 1 segundo"""
    webbrowser.open('http://localhost:8000/mapa_calor_fortaleza.html')

if __name__ == '__main__':
    PORT = 8000
    
    print("=" * 60)
    print("🌐 SERVIDOR WEB DO MAPA DE CALOR - FORTALEZA")
    print("=" * 60)
    print(f"✅ Servidor iniciando na porta {PORT}...")
    print(f"📍 Acesse: http://localhost:{PORT}/mapa_calor_fortaleza.html")
    print(f"🌍 Ou para rede local: http://SEU_IP_LOCAL:{PORT}/mapa_calor_fortaleza.html")
    print("⏹️  Pressione Ctrl+C para parar o servidor")
    print("=" * 60)
    
    # Abrir navegador após 1 segundo
    timer = Timer(1.0, abrir_navegador)
    timer.daemon = True
    timer.start()
    
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, MyHTTPRequestHandler)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n⛔ Servidor parado pelo usuário")
        httpd.server_close()

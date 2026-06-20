from http.server import BaseHTTPRequestHandler, HTTPServer
import random
QUOTES = [
    "DevOps — это не профессия, это стиль жизни.",
    "Если код не работает, значит ты недостаточно пил кофе.",
    "Работает — не трогай. А если трогаешь — пиши манифесты."
]
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        quote = random.choice(QUOTES)
        html = f"<html><body><h1>Случайная цитата:</h1><h2>{quote}</h2></body></html>"
        self.wfile.write(html.encode('utf-8'))
if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8080), SimpleHandler)
    print("Сервер запущен на порту 8080...")
    server.serve_forever()
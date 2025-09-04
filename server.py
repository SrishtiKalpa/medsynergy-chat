from http.server import HTTPServer, SimpleHTTPRequestHandler
import webbrowser
import os

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    url = f'http://localhost:{port}'
    print(f"Server started at {url}")
    webbrowser.open(url)
    httpd.serve_forever()

if __name__ == '__main__':
    # Change working directory to the directory of this script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    run()

from http.server import BaseHTTPRequestHandler, HTTPServer

# Create a custom request handler by subclassing BaseHTTPRequestHandler
class RequestHandler(BaseHTTPRequestHandler):
    
    def do_POST(self):
        # Respond to POST requests
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        
        # Process the POST data here
        
        
        # Send a response back to the client
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        response = 'Received POST request with data: {}'.format(post_data)
        self.wfile.write(response.encode('utf-8'))

# Create an HTTP server and listen for incoming requests
server_address = ('', 8000)
httpd = HTTPServer(server_address, RequestHandler)
print('Listening on port 8000...')
httpd.serve_forever()

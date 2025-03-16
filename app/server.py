from http.server import HTTPServer, BaseHTTPRequestHandler

# Créer une classe de gestionnaire de requêtes
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Envoyer une réponse HTTP 200 (OK)
        self.send_response(200)

        # Définir l'en-tête de la réponse (type de contenu HTML)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # Définir le contenu de la réponse (une page HTML simple)
        message = "<html><body><h1>Hello, Docker!</h1></body></html>"
        
        # Envoyer le contenu de la réponse encodé en UTF-8
        self.wfile.write(message.encode("utf-8"))

# Point d'entrée du script
if __name__ == "__main__":
    # Définir le port sur lequel le serveur écoutera
    PORT = 8000

    # Définir l'adresse du serveur (0.0.0.0 signifie "toutes les interfaces")
    server_address = ("0.0.0.0", PORT)

    # Créer une instance du serveur HTTP
    httpd = HTTPServer(server_address, SimpleHandler)

    # Afficher un message indiquant que le serveur est en cours d'exécution
    print(f"Serving on port {PORT}...")

    # Démarrer le serveur et le faire écouter indéfiniment
    httpd.serve_forever()
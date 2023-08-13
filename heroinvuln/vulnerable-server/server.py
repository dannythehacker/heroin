from flask import Flask, send_file

app = Flask(__name__)

# Define the folder where your media assets are stored
MEDIA_FOLDER = 'media'

@app.route('/media/<path:filename>')
def serve_media(filename):
    try:
        return send_file(f"{MEDIA_FOLDER}/{filename}")
    except:
        return "<h1>Sorry! The file you where looking for was not found.</h1>", 404

if __name__ == '__main__':
    app.run(debug=False)
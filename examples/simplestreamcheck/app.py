from flask import Flask, redirect, make_response, request, abort
app = Flask(__name__)  

@app.route('/')
def index():
    return "Sample App"

@app.route('/publish-check', methods=['GET','POST','OPTIONS'] )
def publish_check():
    print(request.values)

    if request.form['name'] == 'sdf5zdfhdfgdrt':
        response = make_response()
        response.status_code = 301
        response.headers['location'] = 'cfluegel'
        response.autocorrect_location_header = False
        return response
        # return redirect('rtmp://192.168.178.23/ingest/cfluegel', code=301)
        # return redirect('rtmp://192.168.178.23/ingest/cfluegel', code=302)

    abort(403)


# https://stackoverflow.com/questions/22669447/how-to-return-a-relative-uri-location-header-with-flask
# https://benwilber.github.io/streamboat.tv/nginx/rtmp/streaming/2016/10/22/implementing-stream-keys-with-nginx-rtmp-and-django.html
if __name__ == '__main__':
    app.run(host='0.0.0.0')


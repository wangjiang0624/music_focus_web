import sys

from flask import redirect, send_file, render_template

from app.api import *
from app.driver import visit_history
from app.request_handler import RequestHandler


@app.route('/')
def index():
    return redirect('/weibo.html?music_type=rock')


@app.route('/weibo.html')
def show_weibo():
    return _show_biz('weibo.html')


@app.route('/focus.html')
def show_focus():
    return _show_biz('focus.html')


@app.route('/video.html')
def show_video():
    return _show_biz('video.html')


@app.route('/lizhi.html')
def show_lizhi():
    visit_history.write('/lizhi.html')
    return send_file('html/lizhi.html')


@app.route('/lizhi/album.html')
def show_album():
    visit_history.write('/lizhi/album.html')
    return send_file('html/album.html')


def _show_biz(html_name):
    visit_history.write('/' + html_name)
    if 'music_type' not in request.args:
        return 'error'
    return render_template(html_name, music_type=request.args['music_type'])


def start():
    host = '0.0.0.0'
    port = 8000
    if len(sys.argv) >= 3:
        host, port = sys.argv[1:3]
    if conf.is_debug:
        logger.warning('current is debug mode')
    app.run(host=host, port=port, debug=conf.is_debug, request_handler=RequestHandler)


if __name__ == '__main__':
    start()

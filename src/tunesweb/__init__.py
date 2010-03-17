import socket
import win32com.client as wc
from bottle import route, run, view, redirect


@route('/')
@view('index')
def index():
    return dict()
    
    
@route('/control/next')
def control_next():
    get_itunes().NextTrack()
    redirect('/')


@route('/control/prev')
def control_prev():
    get_itunes().PreviousTrack()
    redirect('/')


@route('/control/play')
def control_play():
    get_itunes().Play()
    redirect('/')
    

@route('/control/pause')
def control_pause():
    get_itunes().Pause()
    redirect('/')
    
    
def get_itunes():
    iTunes = wc.gencache.EnsureDispatch('iTunes.Application')
    return iTunes


def main():
    myip = socket.gethostbyname(socket.gethostname())
    run(host=myip, port=6688)
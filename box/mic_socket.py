
import cadquery as cq

from importlib import reload 
import gcab
gcab = reload(gcab)

if __name__ == '__cqgi__':
    show_object(gcab.mic_socket.create(cq))

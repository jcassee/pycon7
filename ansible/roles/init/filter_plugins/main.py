import socket


def resolve_ip(value):
    return socket.gethostbyname(value)


class FilterModule(object):
    def filters(self):
        return {
            'resolve_ip': resolve_ip,
        }

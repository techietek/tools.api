from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
import struct


def decode_cookie(encoded_string):

    (host, port, end) = encoded_string.split('.')
    (a, b, c, d) = [ord(i) for i in struct.pack("<I", int(host))]
    (v) = [ord(j) for j in struct.pack("<H", int(port))]
    p = "0x%02X%02X" % (v[0], v[1])

    return {
        'ip': "%s.%s.%s.%s" % (a, b, c, d),
        'port': "%s" % (int(p, 16)),
        'src': encoded_string
    }

@api_view(['POST'])
def decode(request):
    if request.method == 'POST':
        try:
            d = json.loads(request.body)
            if 'encoded_string' in d:
                data = decode_cookie(d['encoded_string'])
                return Response(data)
            else:
                return Response({"error": "encoded_string not parsed."})
        except Exception as e:
            return Response({"error": e.__str__()})
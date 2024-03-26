import grpc
import time
from concurrent import futures

import Text_To_Audio_pb2
import Text_To_Audio_pb2_grpc  
import Text_Audio

class TextToAudioServicer(Text_To_Audio_pb2_grpc.TextToAudioServicer):


    def ConvertTextToAudio(self, request, context):
        audio_data = Text_Audio.text_to_audio(request.sent)  # Use 'sent' field from request
        return Text_To_Audio_pb2.Audio(audio=audio_data)

    



server=grpc.server(futures.ThreadPoolExecutor(max_workers=10))

Text_To_Audio_pb2_grpc.add_TextToAudioServicer_to_server(TextToAudioServicer(),server) 

print('Starting server.Listening on port 50051')
server.add_insecure_port('[::]:50051')
server.start()

try:
    while True:
        time.sleep(86400)

except KeyboardInterrupt:
    server.stop(0)
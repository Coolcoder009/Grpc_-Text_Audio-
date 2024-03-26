
import grpc
import Text_To_Audio_pb2
import Text_To_Audio_pb2_grpc  

channel = grpc.insecure_channel('localhost:50051')
stub = Text_To_Audio_pb2_grpc.TextToAudioStub(channel)

sentence = Text_To_Audio_pb2.Sentence(sent='Hello, how are you?')

response = stub.ConvertTextToAudio(sentence)

# After receiving the response from the server
with open('output.mp3', 'wb') as audio_file:
    audio_file.write(response.audio)

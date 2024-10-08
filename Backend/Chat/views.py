import time
from django.http import StreamingHttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .services.llm_api_service import basic_inference
from .serializers import ChatRequestSerializer
from FileSystem.models import File

class ChatView(APIView):
    serializer_class = ChatRequestSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        message = serializer.validated_data["message"]
        file_paths = serializer.validated_data["file_paths"]

        #check if all file paths are valid
        #meaning they exist in the database
        if(file_paths is not None and len(file_paths) > 0):
            for file_path in file_paths:
                if not File.objects.filter(path=file_path).exists():
                    return Response({"message": "Some file path is not valid", "files": file_paths}, status=400)

        response = basic_inference(message)

        return Response({"response": response, "files": file_paths})
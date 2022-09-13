from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import allData
from .serializers import allDataSerializer


class FavouriteShow(APIView):
    def get(self,request):
        data = allData.objects.values()
        serializer = allDataSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = {
            'title': request.data.get('title'),
            'price': request.data.get('price'),
            'created_by': request.data.get('created_by'),
            'description': request.data.get('description')
        }
        serializer = allDataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FavouriteChange(APIView):
    def get_object(self, todo_id):
        try:
            return allData.objects.get(id=todo_id)
        except allData.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self,request, todo_id):
        todo_instance = allData.objects.get(id=todo_id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = allDataSerializer(todo_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, todo_id):
        todo_instance = self.get_object(todo_id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'title': request.data.get('title'),
            'price': request.data.get('price'),
            'created_by': request.data.get('created_by'),
            'description': request.data.get('description')
        }
        serializer = allDataSerializer(
            instance=todo_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, todo_id):
        todo_instance = self.get_object(todo_id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        todo_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )

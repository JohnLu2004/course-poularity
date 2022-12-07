from rest_framework import status, generics
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from polls.models import Question
from polls.serializers import QuestionSerializer


class QuestionList(generics.GenericAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    parser_classes = [JSONParser]

    # get refers to method in Django because we get. It just works cuz it do
    def get(self, _):
        print("getting")
        # get all questions
        questions = self.get_queryset()
    
        # serialize the questions
        serializer = self.serializer_class(questions, many=True)

        # return the serialized questions
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # process request data
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # if the request data is valid, process the request
            data = serializer.validated_data
            print(data)
            
            # create the question
            question = Question.objects.create(**data)

            # serialize the questions
            serializer = self.serializer_class(question, many=False)

            # return the result
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # if you did not provide the required fields, return an error
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDetails(generics.RetrieveAPIView):
    serializer_class = QuestionSerializer

    def get(self, _, id):
        try:
            # try to fetch the question
            question = Question.objects.get(id=id)

            # serialize the question
            serializer = self.serializer_class(question, many=False)

            # return the serialized question
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Question.DoesNotExist:
            # return an error if the question does not exist
            # error = ErrorSerializer()

            # return the error
            return Response({"message": "Question not found."}, status=status.HTTP_404_NOT_FOUND)

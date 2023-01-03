from rest_framework import status, generics
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from courses.models import Course
from courses.models import ManuallyAddedCourse
from courses.serializers import CourseSerializer
from courses.getInfo import crawl


class CourseList(generics.GenericAPIView):
    #queryset = Course.objects.all() | ManuallyAddedCourse.objects.all()
    queryset = Course.objects.all().union(ManuallyAddedCourse.objects.all(), all=True)
    serializer_class = CourseSerializer
    parser_classes = [JSONParser]

    # get refers to method in Django because we get. It just works cuz it do
    def get(self, _):
        print("getting")
        #first, we get rid of all the old models
        Course.objects.all().delete()

        #then we get a dictionary using Webscraper
        courseInfoList = crawl()

        #then we turn it into django models
        for i in range(len(courseInfoList)):
            if courseInfoList[i][1]=="":
                courseInfoList[i][1]=0
            Course.objects.create(course_name=courseInfoList[i][0],course_population=((int)(courseInfoList[i][1])))

        # get all courses
        courses = self.get_queryset()
        print(self.queryset)
    
        # serialize the courses
        serializer = self.serializer_class(courses, many=True)

        # return the serialized courses
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        print("posting")
        # process request data
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # if the request data is valid, process the request
            data = serializer.validated_data
            print(data)
            
            # create the course
            course = ManuallyAddedCourse.objects.create(**data)

            # serialize the questions
            serializer = self.serializer_class(course, many=False)

            # return the result
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # if you did not provide the required fields, return an error
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetails(generics.RetrieveAPIView):
    serializer_class = CourseSerializer

    def get(self, _, id):
        try:
            # try to fetch the course
            course = Course.objects.get(id=id)

            # serialize the course
            serializer = self.serializer_class(course, many=False)

            # return the serialized course
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Course.DoesNotExist:
            # return an error if the question does not exist
            # error = ErrorSerializer()

            # return the error
            return Response({"message": "Course not found."}, status=status.HTTP_404_NOT_FOUND)
    def post(self, request):
        # process request data
        serializer = self.serializer_class(data=request.data)
        print("\n \n \n")
        print("okey dokey")
        print("\n \n \n")
        if serializer.is_valid():
            # if the request data is valid, process the request
            data = serializer.validated_data
            print(data)
            
            # create the course
            ManuallyAddedCourse = ManuallyAddedCourse.objects.create(**data)

            # serialize the questions
            serializer = self.serializer_class(ManuallyAddedCourse, many=False)

            # return the result
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # if you did not provide the required fields, return an error
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

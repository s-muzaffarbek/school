from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Subject, Test, StudentResult
from .serializers import SubjectSerializer, TestSerializer, StudentResultSerializer


class SubjectListAPIView(APIView):

    def get(self, request):
        subjects = Subject.objects.filter(teacher=request.user)
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)


class TestListAPIView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, subject_id):
        try:
            subject = Subject.objects.get(unique_id=subject_id)
            tests = Test.objects.filter(subject=subject)
            serializer = TestSerializer(tests, many=True)
            return Response(serializer.data)
        except Subject.DoesNotExist:
            return Response({'error': 'Subject not found'}, status=404)


class SubmitTestAPIView(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        subject = Subject.objects.get(unique_id=data['subject_id'])
        correct_count = 0
        incorrect_count = 0

        for question in data['answers']:
            test = Test.objects.get(id=question['test_id'])
            if test.correct_answer == question['answer']:
                correct_count += 1
            else:
                incorrect_count += 1

        result = StudentResult.objects.create(
            student=request.user,
            subject=subject,
            total_questions=correct_count + incorrect_count,
            correct_answers=correct_count,
            incorrect_answers=incorrect_count,
        )

        serializer = StudentResultSerializer(result)
        return Response(serializer.data)

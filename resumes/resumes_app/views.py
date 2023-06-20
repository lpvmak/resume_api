from rest_framework.viewsets import ModelViewSet

from resumes_app.models import Resume
from resumes_app.permissions import EditCreateResumePermission
from resumes_app.serializers import ResumeModelSerializer


class ResumeViewSet(ModelViewSet):
    permission_classes = (EditCreateResumePermission,)
    queryset = Resume.api_objects.public()
    serializer_class = ResumeModelSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Resume.api_objects.private(self.request.user)
        return Resume.api_objects.public()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
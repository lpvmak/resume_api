from rest_framework.routers import DefaultRouter

from resumes_app.views import ResumeViewSet

router = DefaultRouter()
router.register('resume', ResumeViewSet)

urlpatterns = router.urls

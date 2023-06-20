from rest_framework import serializers

from resumes_app.models import Resume


class ResumeModelSerializer(serializers.ModelSerializer):
    """
    Сериализатор Resume
    """

    class Meta:
        model = Resume
        fields = (
            'id',
            'title',
            'status',
            'grade',
            'specialty',
            'salary',
            'education',
            'experience',
            'portfolio',
            'phone',
            'email',
        )

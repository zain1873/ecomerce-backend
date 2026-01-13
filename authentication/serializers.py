from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=150,
        required=True,
        help_text="Enter your username"
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'},
        help_text="Enter your password"
    )
from rest_framework import serializers
from . models import CustomUser,StreamPlatform,WatchList


class WatchListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=40)
    storyline = serializers.CharField(max_length=200)
    active = serializers.BooleanField(default=True)
    created = serializers.DateTimeField()
    # platform = models.ManyToManyField(StreamPlatform)

    def create(self, validated_data):
        """
        Create and return a new 'Watchlist' instance, given the validated data
        """
        return WatchList.objects.create(**validated_data)
    

    def update(self, instance, validated_data):
        """
        Update and return an existing 'Watchlist' instance, given the validated data
        """
        instance.title = validated_data.get('title', instance.title)
        instance.storyline = validated_data.get('storyline', instance.storyline)
        instance.active = validated_data.get('active', instance.active)
        instance.created = validated_data.get('created', instance.created)
        # instance.platform = validated_data.get('platform', instance.platform)
        instance.save()
        return instance
    

class StreamPlatformSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    about = serializers.CharField(max_length=200)
    website = serializers.URLField(max_length=100)

    def create(self, validated_data):
        """
        Create and return a new 'StreamPlatform' instance, given the validated data
        """
        return StreamPlatform.objects.create(**validated_data)
    

    def update(self, instance, validated_data):
        """
        Update and return an existing 'StreamPlatform' instance, given the validated data
        """
        instance.name = validated_data.get('name', instance.name)
        instance.about = validated_data.get('about', instance.about)
        instance.website = validated_data.get('website', instance.website)
        instance.save()
        return instance
    
class UserSignupSerializer(serializers.Serializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        """
        Create and return a new 'CustomUser' instance, given the validated data
        """
        return CustomUser.objects.create(**validated_data)
    
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        if not username or not password:
            raise serializers.ValidationError('Please enter a username and password')
        
        user = CustomUser.objects.filter(username=username).first()

        if user and user.check_password(password):
            return data
        
        raise serializers.ValidationError('Invalid username or password')
    


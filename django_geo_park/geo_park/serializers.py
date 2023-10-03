from .models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class GeneralUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = GeneralUser
        fields = '__all__'


class CreateGeneralUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralUser
        fields = '__all__'


class SubUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    subscription_fields = serializers.CharField(source='get_subscription_display')

    class Meta:
        model = SubUser
        fields = '__all__'


class CreateSubUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubUser
        fields = '__all__'


class EditImageSerializer(serializers.ModelSerializer):
    user_general = GeneralUserSerializer()
    user_sub = SubUserSerializer()

    class Meta:
        model = EditImage
        fields = '__all__'


class CreateEditImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EditImage
        fields = '__all__'

    # def update(self, instance, validated_data):
    #     instance.time_update = validated_data.get("name", instance.name)
    #     instance.time_update = validated_data.get("is_active", instance.is_active)
    #     instance.save()
    #     return instance


class CreateCategoriesNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriesNews
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    categories = CreateCategoriesNewsSerializer()

    class Meta:
        model = News
        fields = '__all__'


class CreateNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class UpdateImageSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        instance.time_update = validated_data.get("is_done", True)
        instance.save()
        return instance


class UpdateTestModelSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        instance.time_update = validated_data.get("name", instance.name)
        instance.time_update = validated_data.get("is_active", instance.is_active)
        instance.save()
        return instance





class MyImageModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyImageModel
        fields = ('data', 'image')

    def create(self, validated_data):
        image = validated_data.pop('image')
        data = validated_data.pop('data')
        return MyImageModel.objects.create(data=data, image=image)

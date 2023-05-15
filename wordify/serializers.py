from rest_framework import serializers
from .models import Category, Tag, Article, Comment, ExtraText, ExtraImage


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'title', 'count']
    count = serializers.SerializerMethodField(read_only=True)

    def get_count(self, obj):
        return obj.article.count()


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ['id', 'title']


class MineExtraImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExtraImage
        fields = ['id', 'image', 'is_wide']


class MineExtraTextSerializer(serializers.ModelSerializer):
    extraimage = MineExtraImageSerializer(many=True, read_only=True)

    class Meta:
        model = ExtraText
        fields = ['id', 'extratext', 'extraimage']


class ArticleGetSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(read_only=True, many=True)
    extratext = MineExtraTextSerializer(read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'author', 'title', 'image', 'category', 'description', 'views', 'tags', 'extratext',
                  'created_date']


class ExtraImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExtraImage
        fields = ['id', 'extratext', 'image', 'is_wide']


class ExtraTextSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExtraText
        fields = ['id', 'article', 'extratext']
        extra_kwargs = {
            'article': {'required': False}
        }

    def create(self, validated_data):
        article_id = self.context['article_id']
        extratext = validated_data.get('extratext')
        instance = ExtraText.objects.create(article_id=article_id, extratext=extratext)
        return instance


class ArticlePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ['id', 'author', 'title', 'image', 'category', 'tags', 'description', 'views', 'created_date']

    def create(self, validated_data):
        request = self.context.get('request')
        author = request.user.profile
        instance = super().create(validated_data)
        instance.author = author
        instance.save()
        return instance


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'article', 'author', 'description', 'created_date']

    def create(self, validated_data):
        request = self.context['request']
        article_id = self.context['article_id']
        author_id = request.user.profile.id
        description = validated_data.get('description')
        instance = Comment.objects.create(article_id=article_id, author_id=author_id, description=description)
        return instance

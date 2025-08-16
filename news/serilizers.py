from rest_framework import serializers
from .models import News,Notice

class NewsSerilizers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id','image','title','content','status','published_date','created_at']



class NoticeSerilizers(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = ['file','title','content','status','created_at','published_date']
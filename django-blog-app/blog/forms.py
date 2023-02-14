from django import forms
from blog.models import Comment, Reply

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "text")
        widgets - {
            "name": forms.TextImput(attrs={"placeholder": "名前"}),
            "text": forms.Textarea(attr={"placeholder", "コメントを入力してください"})
        }

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ("name", "text")
        widgets - {
            "name": forms.TextImput(attrs={"placeholder": "名前"}),
            "text": forms.Textarea(attr={"placeholder", "返信を入力してください"})
        }
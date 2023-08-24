from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from .forms import PostCreateForm,CommentCreateForm,CommentReplyForm
from django.utils.text import slugify
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import PostModel,CommentModel
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class ContactView(View):
    def get(self, request):
        posts = PostModel.objects.all()
        return render(request, 'contact/contact.html', {'posts':posts})


class PostDetailView(View):
    form_class = CommentCreateForm
    form_class_reply = CommentReplyForm

    def setup(self, request, *args, **kwargs):
        self.post_instance = get_object_or_404(PostModel, pk=kwargs['post_id'], slug=kwargs['post_slug'])
        return super().setup(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        comments = self.post_instance.pcomments.filter(is_reply=False)
        return render(request, 'contact/detail.html', {'post':self.post_instance, 'comments':comments, 'form':self.form_class, 'reply_form':self.form_class_reply})

    @method_decorator(login_required())
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = self.post_instance
            new_comment.save()
            messages.success(request, 'پیغام شما با موفقیت ثبت شد', 'success')
            return redirect('contact:post_detail', self.post_instance.id, self.post_instance.slug)



class PostView(LoginRequiredMixin,View):
    form_class = PostCreateForm
    def get(self, request,*args, **kwargs):
        form = self.form_class
        return render(request, 'contact/contact.html',{'form':form})

    def post(self, request,*args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.slug = slugify(form.cleaned_data['body'][:3])
            new_post.user = request.user
            new_post.save()
            messages.success(request, 'با موفقیت پیام شما ثبت گردید', 'success')
            return redirect('contact:post_detail', new_post.id, new_post.slug)

class PostAddReplyView(LoginRequiredMixin, View):
    form_class = CommentReplyForm
    def post(self, request, post_id, comment_id):
        post = get_object_or_404(PostModel, id=post_id)
        comment = get_object_or_404(CommentModel, id=comment_id)
        form = self.form_class(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.user = request.user
            reply.post = post
            reply.reply = comment
            reply.is_reply = True
            reply.save()
            messages.success(request, 'پاسخ شما با موفقیت ثبت شد' , 'success')
        return redirect('contact:post_detail', post.id , post.slug)






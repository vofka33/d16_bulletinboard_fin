from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Post, Comment
from .forms import PostForm, CommentForm
from .filters import PostFilter

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin





class PostsList(ListView):
    model = Post
    ordering = '-creation_date'
    template_name = 'post_list.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_context_data(self, *args, **kwargs):
        context = super(PostsList, self).get_context_data(*args, **kwargs)
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    queryset = Post.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(DetailView, self).get_context_data(*args, **kwargs)
        current_post = get_object_or_404(Post, id=self.kwargs['pk'])
        post_comments = current_post.comments.order_by('-creation_date')
        accepted_post_comments = post_comments.filter(accepted__exact=True)
        post_comments_count = current_post.comments.count()
        accepted_post_comments_count = accepted_post_comments.count()
        context['post_comments_count'] = post_comments_count
        context['post_comments'] = post_comments
        context['accepted_post_comments_count'] = accepted_post_comments_count
        return context


class PostAddView(LoginRequiredMixin, CreateView):
    template_name = 'post_add.html'
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentAddView(LoginRequiredMixin, CreateView):
    template_name = 'comment_add.html'
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'post_delete.html'
    queryset = Post.objects.all()
    success_url = '/'


class PostEditView(LoginRequiredMixin, UpdateView):
    template_name = 'post_add.html'
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class CommentsModeratonView(LoginRequiredMixin, ListView):
    model = Post
    ordering = '-creation_date'
    template_name = 'comment_moderation.html'
    context_object_name = 'author_posts'

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user).order_by('-creation_date')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        author = self.request.user
        author_posts = Post.objects.filter(author=author).order_by('creation_date')
        context['author_posts'] = author_posts
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


@login_required
def comment_accept(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.accept()
    return redirect('post_detail', pk=comment.post.pk)



@login_required
def comment_reject(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.reject()
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)





# @receiver(m2m_changed, sender=Post)
# def notify_post_create(sender, instance, *args, **kwargs):
#     for cat_id in instance.postCategory.all():
#
#         users = Category.objects.filter(name=cat_id).values("subscribers")
#         # print('user', users)
#         link = ''.join(['http://', get_current_site(None).domain, ':8000/'])
#         for user_id in users:
#             send_mail(
#                 subject=f'Новая публикация - "{instance.title}"',
#                 message=f"Здравствуй, {User.objects.get(pk=user_id['subscribers']).username}. "
#                         f'Новая публикация в вашем любимом разделе! \n"{instance.text[:50]}..."\n'
#                         f'Пройдите по ссылке {link} что бы прочитать на нашем сайте.',
#                 from_email='imya6301@yandex.ru',
#                 recipient_list=[User.objects.get(pk=user_id['subscribers']).email]
#             )


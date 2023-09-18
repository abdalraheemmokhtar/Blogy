from django.shortcuts import render, get_object_or_404, redirect
from .models import Post  # Import the Post model
from django.contrib.auth.models import User
from .forms import PostForm  # Import your PostForm

def post_list(request):
    posts = Post.objects.all()  # Retrieve all Post objects
    return render(request, 'core/post_list.html', {'posts': posts})

def post_details(request, author_id):
    author = User.objects.get(id=author_id)  # Get the author by their ID
    posts = Post.objects.filter(author=author)  # Filter posts by the author

    return render(request, 'core/post_details.html', {'author': author, 'posts': posts})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # Save the new post and redirect to its detail view
            post = form.save()
            return redirect('post_details', author_id=post.author.id)  # Replace 'post_detail' with your detail view name
    else:
        form = PostForm()
    return render(request, 'core/create_post.html', {'form': form})

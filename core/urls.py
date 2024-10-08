from django.contrib import admin
from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from .schema import schema

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('blog.urls')),  # Include your app's URLs
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]
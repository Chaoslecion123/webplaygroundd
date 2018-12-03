from django.urls import path
from pages.views import PagesListView,PageDetailView,PageCreateView,PageUpdateView,PageDeleteView


pages_patterns = ([
    path('', PagesListView.as_view(), name='pages'),
    # en un detail lo que espera es un pk
    path('<int:pk>/<slug:slug>/', PageDetailView.as_view(), name='page'),
    path('create/', PageCreateView.as_view(),name='create'),
    path('update/<int:pk>/', PageUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/', PageDeleteView.as_view(),name='delete'),
],'pages')


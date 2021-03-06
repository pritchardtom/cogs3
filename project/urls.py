from . import views

from django.urls import path

urlpatterns = [
    path(
        'create/',
        views.ProjectCreateView.as_view(),
        name='create-project',
    ),
    path(
        'join/',
        views.ProjectUserMembershipFormView.as_view(),
        name='project-membership-create',
    ),
    path(
        'applications/',
        views.ProjectListView.as_view(),
        name='project-application-list',
    ),
    path(
        'applications/<int:pk>/',
        views.ProjectDetailView.as_view(),
        name='project-application-detail',
    ),
    path(
        'memberships/',
        views.ProjectUserMembershipListView.as_view(),
        name='project-membership-list',
    ),
    path(
        'memberships/user-requests/',
        views.ProjectUserRequestMembershipListView.as_view(),
        name='project-user-membership-request-list',
    ),
    path(
        'memberships/user-requests/update/<int:pk>/',
        views.ProjectUserRequestMembershipUpdateView.as_view(),
        name='project-user-membership-request-update',
    ),
]

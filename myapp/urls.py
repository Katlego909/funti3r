from django.urls import path
from myapp.views import home, marketplace, academy, task_planner, documents, assistant, account, pricing, signup, chatpdf, dashboard, category_tasks, categories

urlpatterns = [
    path("", home, name="home"),
    path('category/<int:category_id>/', category_tasks, name='category_tasks'),
    path("categories", categories, name="categories"),
    path("dashboard", dashboard, name="dashboard"),
    path("marketplace/", marketplace, name="marketplace"),
    path("academy/", academy, name="academy"),
    path("task_planner/", task_planner, name="task_planner"),
    path("documents/", documents, name="documents"),
    path("assistant/", assistant, name="assistant"),
    path("chatpdf/", chatpdf, name="chatpdf"),
    path("account/", account, name="account"),
    path("pricing/", pricing, name="pricing"),
    path("signup/", signup, name="signup"),
]
 
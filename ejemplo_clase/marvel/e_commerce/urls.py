from django.urls import path
from e_commerce.api.marvel_api_views import *

# Importamos las API_VIEWS:
from e_commerce.views import *


from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required, permission_required

INDEX_LIST = ['index/', 'index/#', '']
INDEX_PATTERNS = [path(x, IndexView.as_view()) for x in INDEX_LIST]

urlpatterns = [
    # NOTE: e-commerce base:
    path('base', PruebaView.as_view()),

    # NOTE: Manejo de sesión:
    path('login', auth_views.LoginView.as_view(template_name='e-commerce/login.html', redirect_authenticated_user=True, redirect_field_name='index'), name='login'
         ),
    path('logout', auth_views.LogoutView.as_view(next_page='/e-commerce/index', redirect_field_name='index'),
         ),
    path('singup', register, name='register'),

    # NOTE: Páginas del sitio:
    path('detail', DetailsView.as_view(), name='detail'),
    path('index', IndexView.as_view(), name='index'),
    path('thanks', ThanksView.as_view(), name='thanks'),
    path('update-user', UpdateUserView.as_view(), name= 'update'),
    path('user', login_required(UserView.as_view()), name= 'user'),
    path('wish', login_required(WishView.as_view()), name='wish'),
    path('cart', login_required(CartView.as_view()), name='cart'),

    # NOTE: Formularios ocultos
    path('checkbutton', check_button, name='checkbutton'),

    # NOTE: Ejemplos de Bootstrap HTML:
    path('bootstrap-login', BootstrapLoginUserView.as_view(), name='loginbootstrap'),
    path('bootstrap-singup', BootstrapSingupView.as_view(), name='singupbootstrap'),
]
urlpatterns += INDEX_PATTERNS

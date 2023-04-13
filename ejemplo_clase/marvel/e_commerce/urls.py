from django.urls import path
from e_commerce.api.marvel_api_views import *

# Importamos las API_VIEWS:
from e_commerce.views import *

# Librerías para el manejo de sesión.
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

# Una forma de listar endpoints para redirección. 
# Django posee su propia herramienta para esto: 
# Django redirects app: https://docs.djangoproject.com/en/3.2/ref/contrib/redirects/#module-django.contrib.redirects 

INDEX_LIST = ['index/', 'index/#', '']
INDEX_PATTERNS = [path(x, IndexView.as_view()) for x in INDEX_LIST]

urlpatterns = [
     # NOTE: e-commerce base:
     path('hello', PruebaView.as_view()),
     path('text', TextView.as_view()),
     path('links', LinksView.as_view()),
     path('lists', ListsView.as_view()),
     path('button', ButtonsView.as_view()),
     path('table', TableView.as_view()),
     path('form', FormView.as_view()),
     path('image', ImageView.as_view()),
     path('example', ExampleView.as_view()),
     path('variables', VariablesView.as_view(), name='variables'),
     path(
          'variable-contexto',
          VariableDeContextoView.as_view(),
          name='variable-contexto'
     ),
     path('for', ForView.as_view(), name='for'),
     path('if', IfView.as_view(), name='if'),
     path('url-origen', UrlOrigenView.as_view(), name='origen'),
     path('url-destino', UrlDestinoView.as_view(), name='destino'),
     path('csrf-form', CsrfTokenFormView.as_view(), name='formulario'),
     path('extendido', ExtendidoView.as_view(), name='extendido'),
     path('base', BaseView.as_view()),
     # NOTE: Manejo de sesión:
     path(
          'login',
          auth_views.LoginView.as_view(
               template_name='e-commerce/login.html',
               redirect_authenticated_user=True,
               redirect_field_name='index'
          ),
          name='login'
     ),
     path(
          'logout',
          auth_views.LogoutView.as_view(
               next_page='/e-commerce/index',
               redirect_field_name='index'
          )
     ),
     path('signup', register, name='register'),
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
     path(
          'bootstrap-login',
          BootstrapLoginUserView.as_view(),
          name='loginbootstrap'
     ),
     path(
          'bootstrap-signup',
          BootstrapSignupView.as_view(),
          name='signupbootstrap'
     ),
]

urlpatterns += INDEX_PATTERNS
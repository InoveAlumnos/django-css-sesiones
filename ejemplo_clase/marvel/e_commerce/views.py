
# Importamos vistas genericas:
from django.views.generic import TemplateView, CreateView, ListView

# Importamos los modelos que vamos a usar:
from django.contrib.auth.models import User
from e_commerce.models import *


# Formulario de registro:
from django import forms
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm

# Utilidades:
from marvel.settings import VERDE, AMARILLO


# NOTE: Generamos las vistas genéricas para probar Django Template:

TEST_DIC = {
    'saludo': 'Hola, mi nombre es: ',
    'user': 'INOVE!! '
}

TEST_LIST = ['Hola, ', 'mi ', 'nombre ', 'es ', 'Inove ']


# NOTE: Generamos las vistas genéricas para probar bloques HTML:
class PruebaView(TemplateView):
    template_name = 'e-commerce/hello.html'


class TextView(TemplateView):
    template_name = 'e-commerce/00-text.html'


class LinksView(TemplateView):
    template_name = 'e-commerce/01-links.html'


class ListsView(TemplateView):
    template_name = 'e-commerce/02-listas.html'


class ButtonsView(TemplateView):
    template_name = 'e-commerce/03-buttons.html'


class TableView(TemplateView):
    template_name = 'e-commerce/04-table.html'


class FormView(TemplateView):
    template_name = 'e-commerce/05-form.html'


class ImageView(TemplateView):
    template_name = 'e-commerce/06-images.html'


class ExampleView(TemplateView):
    template_name = 'e-commerce/example.html'


class VariablesView(TemplateView):
    template_name = 'e-commerce/variables.html'


class VariableDeContextoView(TemplateView):
    template_name = 'e-commerce/variable-contexto.html'

    def get_context_data(self, **kwargs):
        '''
        En esta función vamos a agregar más información a nuestro 
        contexto de ejecución para que pueda ser incluido en nuestros templates!
        La variable `context` es funciona como un diccionario, es por ello que vamos a 
        ir agregandole información para luego ser accedida por su key.
        Aquí también podemos interceptar el objeto "request" 
        con los datos de la petición realizada al sitio.
        '''
        context = super().get_context_data(**kwargs)
        # NOTE: Agregamos una lista a nuestro contexto:
        context['prueba_lista'] = [
            'Hola', 'mi nombre es', self.request.user.username]
        
        # NOTE: Agregamos un diccionario a nuestro contexto:
        context['prueba_diccionario'] = {
            'saludo': 'hola, mi nombre es: ', 'usuario': f'{self.request.user.username}'.upper()}
        return context


class ForView(TemplateView):
    template_name = 'e-commerce/for.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['TEST_DIC']=TEST_DIC
        context['TEST_LIST']=TEST_LIST
        return context


# NOTE: Generamos el template base para extender:
class IfView(TemplateView):
    template_name = 'e-commerce/if.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['TEST_DIC']=TEST_DIC
        context['TEST_LIST']=TEST_LIST
        return context


class UrlOrigenView(TemplateView):
    template_name = 'e-commerce/url-origen.html'


class UrlDestinoView(TemplateView):
    template_name = 'e-commerce/url-destino.html'


class CsrfTokenFormView(CreateView):
    '''
    Importante: Utilizamos un CreateView porque éste admite peticiones POST, 
    necesarias para el envío del formulario en este caso.
    Esta clase requiere un modelo y un campo como mínimo para funcionar.
    '''
    model = User
    fields = ['username']
    template_name = 'e-commerce/csrf-form.html'


class ExtendidoView(TemplateView):
    template_name = 'e-commerce/extendido.html'


# NOTE: Páginas del sitio **********************************************************
class BaseView(TemplateView):
    '''
    Template base que vamos a extender para el resto de las páginas del sitio.
    '''
    template_name = 'e-commerce/base.html'


class LoginUserView(TemplateView):
    '''
    Formulario de inicio de sesión.
    '''
    template_name = 'e-commerce/login.html'

class UserForm(UserCreationForm):
    '''
    Formulario de creación de usuario.
    Utilizamos un formulario que viene por defecto en Django y que cumple con todos los
    requisitos para agregar un nuevo usuario a la base de datos.
    También tiene los métodos para validar todos sus campos.
    '''
    first_name = forms.CharField(widget=forms.TextInput(
        # Así podemos asignar las clases CSS a nuestros forms . . .
        attrs={
            'class': 'form-control',
            'placeholder': 'Username'
        }
    ))
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',
                  'email', 'password1', 'password2')


def register(request):
    '''
    Función que complementa el formulario de registro de usuario.
    Al completar el formulario, se envía la información a esta función que espera
    una petición de tipo `POST`, si la información enviada no es valida o la petición no es POST, 
    se redirige nuevamente a la página de registro. Si el registro fue exitoso,
    el usuario será redirigido a la página de logueo.
    '''
    if request.method == 'POST':
        # Si la petición es de tipo POST, analizamos los datos del formulario:
        # Creamos un objeto de tipo UserForm (la clase que creamos mas arriba)
        # Pasandole los datos del request:
        form = UserForm(request.POST)
        # Luego, utilizamos el método que viene en en la clase UserCreationForm
        # para validar los datos del formulario: 
        [print(VERDE+'',item) for item in form] # NOTE: Imprimimos para ver el contenido del formulario COMPLETO
        if form.is_valid():
            # Si los datos son validos, el formulario guarda los datos en la base de datos.
            # Al heredar de UserCreationForm, aplica las codificaciónes en el password y todo
            # lo necesario:
            form.save()
            # Con todo terminado, redirigimos a la página de inicio de sesión,
            # porque por defecto, registrar un usuario no es iniciar una sesión.
            return redirect('/e-commerce/login')
    else:
        # Si el método no es de tipo POST, se crea un objeto de tipo formulario
        # Y luego se envía al contexto de renderización. 
        form = UserForm()
    # Si los datos del POST son invalidos o si el método es distinto a POST
    # retornamos el render de la página de registro, con el formulario de registro en el contexto.
    [print(AMARILLO+'',item) for item in form] # NOTE: Imprimimos para ver el contenido del formulario vacío
    return render(request, 'e-commerce/signup.html', {'form': form})

class IndexView(ListView):
    '''
    Página principal del sitio.
    Utilizamos `ListView` para poder aprovechar sus funciones de paginado.
    Para ello tenemos que utilizar sus atributos:
    \n
    '''
    queryset = Comic.objects.all().order_by('-id')
    # NOTE: Este queryset incorporará una lista de elementos a la que le asignará
    # Automáticamente el nombre de comic_list
    template_name = 'e-commerce/index.html'
    paginate_by = 10

    # NOTE: Examinamos qué incluye nuestro contexto:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        [print(AMARILLO+f'{element}\n') for element in context.items()]
        return context


class DetailsView(TemplateView):
    template_name = 'e-commerce/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            _comic = Comic.objects.get(
                marvel_id=self.request.GET.get('marvel_id')
            )
            context["comic"] = _comic
            context['comic_picture_full'] = str(
                _comic.picture
            ).replace('/standard_xlarge', '')
            context['comic_desc'] = str(
                _comic.description
            ).replace('<br>', '\n')
            if self.request.user:
                _wish_qs = WishList.objects.filter(
                    user=self.request.user, comic=_comic
                )
                if _wish_qs.exists():
                    _wish = _wish_qs.first()
                    context["favorite"] = _wish.favorite
                    context["cart"] = _wish.cart
                    context["wished_qty"] = _wish.wished_qty
                else:
                    context["favorite"] = False
                    context["cart"] = False
                    context["wished_qty"] = 0
        except:
            return context
        return context


def check_button(request):
    '''
    Esta función tiene como objetivo el cambio de estado de los botones de favoritos y carrito.
    '''
    if request.method == 'POST':
        print(request.path)
        # NOTE: Obtenemos los datos necesarios:
        username = request.POST.get('username')
        marvel_id = request.POST.get('marvel_id')
        user_authenticated = request.POST.get('user_authenticated')
        type_button = request.POST.get('type_button')
        actual_value = request.POST.get('actual_value')
        path = request.POST.get('path')
        print('FERNANDAAA', marvel_id)

        # Validamos los datos y les damos formato:
        username = username if username != '' else None
        marvel_id = marvel_id if marvel_id else None
        user_authenticated = True if user_authenticated == 'True' else False
        type_button = type_button if type_button != '' else None
        actual_value = True if actual_value == 'True' else False
        path = path if path != None else 'index'

        if user_authenticated and username != None:
            # Si el usuario está autenticado, traemos su "wishlist"
            user_obj = User.objects.get(username=username)
            comic_obj = Comic.objects.get(marvel_id=marvel_id)
            wish_obj = WishList.objects.filter(
                user=user_obj, comic=comic_obj).first()
            if not wish_obj:
                # Si no tiene "wishlist" creamos una
                wish_obj = WishList.objects.create(
                    user=user_obj, comic=comic_obj)

            # Remplazamos el estado del botón seleccionado:
            if type_button == "cart":
                wish_obj.cart = not actual_value
                wish_obj.save()
                print('wish_obj.cart :', wish_obj.cart)
            elif type_button == "favorite":
                wish_obj.favorite = not actual_value
                print('wish_obj.favorite :', wish_obj.favorite)
                wish_obj.save()
            else:
                pass
            # Componemos los endpoints segun la página:
            if 'detail' in path:
                path += f'?marvel_id={marvel_id}'
            
            # Una vez terminada la modificación, volvemos a la misma página.
            return redirect(path)
        else:
            # Si el usuario no está autenticado, lo redirigimos a la página de logueo.
            return redirect('login')
    else:
        # Si por error quisieron acceder al recurso con otro método que no sea POST, lo redirigimos al index
        return redirect('index')


class CartView(TemplateView):
    '''
    Vista de carrito de compras.
    Aquí se listará el total de elementos del carrito del usuario, 
    luego en el template se colocará un formulario en cada elemento del carrito
    para darlo de baja, y un boton general para concretar el pedido.
    '''
    template_name = 'e-commerce/cart.html'

    def get_context_data(self, **kwargs):
        '''
        En el contexto, devolvemos la lista total de elementos en el carrito de compras, 
        y el precio total calculado para la compra.
        '''
        context = super().get_context_data(**kwargs)
        username = self.request.user
        user_obj = User.objects.get(username=username)
        wish_obj = WishList.objects.filter(user=user_obj, cart=True)
        cart_items = [obj.comic for obj in wish_obj]
        context['cart_items'] = cart_items
        context['total_price'] = round((sum([float(comic.price) for comic in cart_items])), 2)
        print(context['cart_items'])
        return context


class WishView(TemplateView):
    '''
    En esta vista vamos a traer todos los comics favoritos de un usuario en particular.
    Luego en el Template vamos a colocar un formulario por cada favorito, 
    para eliminarlo de la lista de favoritos.
    '''
    template_name = 'e-commerce/wish.html'

    def get_context_data(self, **kwargs):
        '''
        Preparamos en nuestro contexto la lista de comics del usuario registrado.
        '''
        context = super().get_context_data(**kwargs)
        username = self.request.user
        user_obj = User.objects.get(username=username)
        wish_obj = WishList.objects.filter(user=user_obj, favorite=True)
        cart_items = [obj.comic for obj in wish_obj]
        context['fav_items'] = cart_items
        print(context['fav_items'])
        return context


class ThanksView(TemplateView):
    '''
    Página de agradecimiento. Esta es la página de respuesta una vez realizado el pedido.
    El Template tiene que tener un botón de redireccionamiento al index.
    '''
    template_name = 'e-commerce/thanks.html'


class UpdateUserView(TemplateView):
    '''
    Esta vista tiene como objetivo, proporcionar un formulario de actualización de los campos de usuario.
    '''
    template_name = 'e-commerce/update-user.html'

    def get_context_data(self, **kwargs):
        # TODO: Realizar la lógica de actualización de los datos de usuario.
        return super().get_context_data(**kwargs)

class UserView(TemplateView):
    '''Vista con el detalle de los datos personales del usuario'''

    template_name = 'e-commerce/user.html'

    def get_context_data(self, **kwargs):
        # TODO: Realizar la lógica que lista los datos del usuario, 
        # incluyendo los datos de la tabla de datos adicionales de usuario.
        return super().get_context_data(**kwargs)


# NOTE: Vistas con Bootstrap:

class BootstrapLoginUserView(TemplateView):
    '''
    Vista para Template de login con estilo de bootstrap.
    '''
    template_name = 'e-commerce/bootstrap-login.html'

class BootstrapSignupView(TemplateView):
    '''
    Vista para Template de registro de usuario con estilo de bootstrap.
    '''
    template_name = 'e-commerce/bootstrap-signup.html'

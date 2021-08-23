from django.shortcuts import render
from django.urls.conf import path

# Importamos vistas genericas:
from django.views.generic import TemplateView, RedirectView, DetailView, ListView

# Importamos los modelos que vamos a usar:
from django.contrib.auth.models import User
from e_commerce.models import *

# TEST:
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect


# Probamos la vista generica:
class PruebaView(TemplateView):
    template_name = 'e-commerce/base.html'

# NOTE: Generamos las vistas genéricas para probar bloques HTML:

# NOTE: Ejemplos **********************************************************


# NOTE: Páginas del sitio **********************************************************
class LoginUserView(TemplateView):
    template_name = 'e-commerce/login.html'


class UserForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',
                  'email', 'password1', 'password2')


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/e-commerce/index')
    else:
        form = UserForm()

    return render(request, 'e-commerce/singup.html', {'form': form})


class IndexView(ListView):
    queryset = Comic.objects.all().order_by('-id')
    template_name = 'e-commerce/index.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mensaje"] = "Hola! :D"
        return context


class DetailsView(TemplateView):
    template_name = 'e-commerce/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # try:
        comic_obj = Comic.objects.get(
            marvel_id=self.request.GET.get('marvel_id'))
        context["comic"] = comic_obj
        context['comic_picture_full'] = str(
            comic_obj.picture).replace('/standard_xlarge', '')
        context['comic_desc'] = str(
            comic_obj.description).replace('<br>', '\n')
        username = self.request.user
        if username != None:
            user_obj = User.objects.filter(username=username)
            if user_obj.first() != None:
                wish_obj = WishList.objects.filter(
                    user_id=user_obj[0].id, comic_id=comic_obj)
                if wish_obj.first() != None:
                    context["favorite"] = wish_obj.first().favorite
                    context["cart"] = wish_obj.first().cart
                    context["wished_qty"] = wish_obj.first().wished_qty
                else:
                    context["favorite"] = False
                    context["cart"] = False
                    context["wished_qty"] = 0
        # except:
        #     return context
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
        print('path', path)

        # Validamos los datos y les damos formato:
        username = username if username != '' else None
        marvel_id = marvel_id if marvel_id != '' else None
        user_authenticated = True if user_authenticated == 'True' else False
        type_button = type_button if type_button != '' else None
        actual_value = True if actual_value == 'True' else False
        path = path if path != None else 'index'

        if user_authenticated and username != None:
            # Si el usuario está autenticado, traemos su "wishlist"
            user_obj = User.objects.get(username=username)
            comic_obj = Comic.objects.get(marvel_id=marvel_id)
            wish_obj = WishList.objects.filter(
                user_id=user_obj, comic_id=comic_obj).first()
            if not wish_obj:
                # Si no tiene "wishlist" creamos una
                wish_obj = WishList.objects.create(
                    user_id=user_obj, comic_id=comic_obj)

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
    template_name = 'e-commerce/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.request.user
        user_obj = User.objects.get(username=username)
        wish_obj = WishList.objects.filter(user_id=user_obj, cart=True)
        cart_items = [obj.comic_id for obj in wish_obj]
        context['cart_items'] = cart_items
        context['total_price'] = round((sum([float(comic.price) for comic in cart_items])), 2)
        print(context['cart_items'])
        return context


class WishView(TemplateView):
    template_name = 'e-commerce/wish.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.request.user
        user_obj = User.objects.get(username=username)
        wish_obj = WishList.objects.filter(user_id=user_obj, favorite=True)
        cart_items = [obj.comic_id for obj in wish_obj]
        context['fav_items'] = cart_items
        print(context['fav_items'])
        return context


class ThanksView(TemplateView):
    template_name = 'e-commerce/thanks.html'


class UpdateUserView(TemplateView):
    template_name = 'e-commerce/update-user.html'


class UserView(TemplateView):
    template_name = 'e-commerce/user.html'

# NOTE: Vistas con Bootstrap:

class BootstrapLoginUserView(TemplateView):
    template_name = 'e-commerce/bootstrap-login.html'

class BootstrapSingupView(TemplateView):
    template_name = 'e-commerce/bootstrap-singup.html'
from ads.serializer import AdSerializer, AdListSerializer, AdDetailSerializer, CategorySerializer
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView

from ads.models import Ad, Category
from rest_framework.viewsets import ModelViewSet


def home(request):
    return JsonResponse({"status": "ok"}, status=200)


class AdViewSet(ModelViewSet):
    queryset = Ad.objects.all()
    default_serializer = AdSerializer
    serializers = {
        "list": AdListSerializer,
        "retrieve": AdDetailSerializer
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)

    def list(self, request, *args, **kwargs):
        cat = request.GET.getlist("cat")
        if cat:
            self.queryset = self.queryset.filter(category_id__in=cat)

        text = request.GET.get("text")
        if text:
            self.queryset = self.queryset.filter(name__icontains=text)

        location = request.GET.get("location")
        if location:
            self.queryset = self.queryset.filter(author__locations__name__icontains=location)

        price_from = request.GET.get("price_from")
        if price_from:
            self.queryset = self.queryset.filter(price__gte=price_from)

        price_to = request.GET.get("price_to")
        if price_to:
            self.queryset = self.queryset.filter(price__lte=price_to)

        return super().list(request,*args, **kwargs)


@method_decorator(csrf_exempt, name="dispatch")
class AdUploadImageView(UpdateView):
    model = Ad
    fields = "__all__"

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        self.object.image = request.FILES.get("image")
        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "author": self.object.author.username,
            "description": self.object.description,
            "price": self.object.price,
            "category": self.object.category.name,
            "is_published": self.object.is_published,
            "image": self.object.image.url,
        })


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

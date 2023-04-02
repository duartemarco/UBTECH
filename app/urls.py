from rest_framework import routers
from app.views import ServicoDetail, ServicoList, FuncionarioDetail, FuncionarioList

router = routers.DefaultRouter()
# router.register(r'', FuncionarioViewSet)
# router.register(r'', ServicoViewSet)

urlpatterns = router.urls
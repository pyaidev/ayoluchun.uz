from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from src.apps.payment.api.v1.serializer import PaymentSerializer
from src.apps.payment.models import Payment


class PaymentCreateView(CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

import random
from datetime import datetime

from django.utils import timezone

from core.models import Card
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from dateutil.relativedelta import relativedelta
from django.views.generic import ListView, DetailView, DeleteView, TemplateView, FormView, UpdateView
from core.forms import CreateCardForm
from core.service import get_random_card_cvv, get_random_card_number
# Create your views here.


class IndexView(ListView):
    template_name = "index.html"
    model = Card
    paginate_by = 10


class CardDetailView(DetailView):
    template_name = "card-detail.html"
    model = Card


class ChangeStatusView(DetailView):
    template_name = "card-detail.html"
    model = Card

    def post(self, request, pk):
        card = Card.objects.get(id=pk)
        if card.status.lower() == "active":
            card.status = "Inactive"
        elif card.status.lower() == "inactive":
            card.status = "Active"

        card.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class DeleteCardView(DeleteView):
    template_name = "card_confirm_delete.html"
    model = Card
    success_url = "/"


class CreateCardView(FormView):
    template_name = "create-card.html"
    form_class = CreateCardForm

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        context = self.get_context_data()
        form = self.get_form(form_class)
        context['form'] = form
        if form.is_valid():
            form.save()
            return redirect("/")

        return self.render_to_response(context)


class UpdateCardView(UpdateView):
    model = Card
    fields = "__all__"
    template_name = "edit-card.html"
    success_url = "/"


class GenerateCardsView(TemplateView):
    template_name = "generate-cards.html"

    def post(self, request):
        series = request.POST.get("series")
        count = int(request.POST.get("count"))
        period = int(request.POST.get("period"))
        year_or_month = request.POST.get("rad")
        today = timezone.now()

        activity_end_date = today + relativedelta(months=1)

        if year_or_month.lower() == "month":
            activity_end_date = today + relativedelta(months=period)
        elif year_or_month.lower() == "year":
            activity_end_date = today + relativedelta(years=period)

        for iterator in range(count):
            card = Card.objects.create(
                series=series,
                number=get_random_card_number(),
                release_date=today,
                cvv=get_random_card_cvv(),
                funds=random.randint(1, 1_000_000),
                activity_end_date=activity_end_date,
                status="Active"
            )
            card.save()
        return redirect("/")


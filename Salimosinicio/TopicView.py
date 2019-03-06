from django.shortcuts import render
from django.views import View


class TopicView(View):
    template_name = "application/template.html"

    def get(self, request, *args, **kwargs):
        topic = TopicView.objects.get(id=1)

        data = {
            'topic': topic,
        }

        return render(request, self.template_name, data)

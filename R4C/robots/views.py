import datetime
import json

from django.db.models import Count
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.utils.decorators import method_decorator

from robots.models import Robot
from .utils import write_csv


@method_decorator(csrf_exempt, name='dispatch')
class RobotCreationView(View):
    def post(self, request, *args, **kwargs):
        """Добавление робота в БД, с валидацией"""
        data = json.loads(request.body)
        serial = f"{data['model']}1{data['version']}"
        model = data['model']
        version = data['version']
        created = data['created']

        if Robot.objects.filter(model=model, version=version).exists():
            return JsonResponse(
                {'message': 'Данная модель и версия робота уже существует.'},
                status=400
            )
        if (len(model) or len(version)) != 2:
            return JsonResponse(
                {'message': 'У поля номера и модели по 2 символа.'},
                status=400
            )
        if created:
            Robot.objects.create(
                serial=serial,
                model=model,
                version=version,
                created=created
            )
            return JsonResponse(
                {'message': 'Robot created successfully.'}
            )
        
        return JsonResponse(
            {'message': 'Invalid data provided.'},
            status=400
        )

class ExcelReportView(View):
    def get(self, request, *args, **kwargs):
        """Отправка Excel-файла пользователю"""
        end_date = timezone.now()
        start_date = end_date - datetime.timedelta(days=7)
        robots = Robot.objects.filter(
            created__range=[start_date, end_date]
        ).values('model', 'version').annotate(count=Count('id'))

        csv = write_csv(robots)

        response = HttpResponse(content_type="application/ms-excel")
        response["Content-Disposition"] = f'attachment; filename="robot_production_report.xlsx"'
        csv.save(response)
        
        return response
import json

from django.http import JsonResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

from robots.models import Robot


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
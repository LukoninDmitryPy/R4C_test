from openpyxl import Workbook


def write_csv(robots):
    """Создание Excel-файла"""
    wb = Workbook()
    current_model = None
    for robot in robots:
        model = robot['model']
        version = robot['version']
        count = robot['count']

        if model != current_model:
            ws = wb.create_sheet(title=model)
            print(model)
            ws.append(["Модель", "Версия", "Количество за неделю"])
            current_model = model
        else:
            ws = wb[model]

        ws.append([model, version, count])

    wb.remove(wb['Sheet'])

    return wb
from datetime import datetime, timezone


def year(request):
    """Добавляет переменную с текущим годом."""
    utc_dt = datetime.now(timezone.utc)
    dt = utc_dt.astimezone().year
    return {
        'year': dt
    }

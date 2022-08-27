from . import schemas


class HealthChecker:
    def health_check(self) -> schemas.HealthCheck:
        # вставить любую логику проверки из модуля `logic`
        return schemas.HealthCheck(status='ok')

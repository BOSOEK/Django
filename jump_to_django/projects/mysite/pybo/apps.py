from django.apps import AppConfig


class PyboConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pybo'
    # 이 클래스가 config/setting.py 파일의 INSTALLED_APPS에
    # 추가되지 않으면 장고는 pybo 앱을 인식하지 못한다.

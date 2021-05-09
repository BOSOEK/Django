# 어플리케이션 생성, 데이터베이스 작업, 개발 웹 서버 시작을 위해 사용됨
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'locallibrary.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

# 장고는 저장되어야 할 데이터의 구조에 영향을 미치는 방식으로 모델 변경시 마다 아래의 명령어를 실행해야 함.
# python manage.py makemigrations
# python manage.py migrate
# 그러면 데이터 베이스 안의 모델들을 위한 테이블들을 정의함(ORM을 이용해서)

# makemigrations : 프로젝트에 설치된 모든 어플리케이션에 대한 migration을 생성한다.(적용은 하지 않는다.)
# makemigrations는 그저 단일 프로젝트를 위한 migrations을 실행하기 위해 어플리케이션 이름 지정 가능

# migrate : migration을 실제로 데이터베이스에 적용함

from config import settings
import platform
import sys


def create_allure_environment_file():
    items = [f'{key}={value}' for key, value in settings.model_dump().items()]
    properties = '\n'.join(items)
    properties += f'\nos_info={platform.system()}, {platform.release()}'
    properties += f'\npython_version={sys.version}'
    print(properties)

    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(properties)


create_allure_environment_file()

from api_handler import ApiHandler


class TaskHandler:
    def __init__(self, api_handler: ApiHandler):
        self.api_handler = api_handler

    def create_task(self):
        self.api_handler.connect_api()

        pass

    def update_task(self):
        self.api_handler.connect_api()

        pass

    def remove_task(self):
        self.api_handler.connect_api()

        pass

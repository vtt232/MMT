from gui.client.App_process.TableView import TableView
from gui.client.App_process.InputButtonView import InputButtonView

from gui.popup import PopUp


class AppView(TableView):
    def __init__(self, client):
        super(AppView, self).__init__(
            "App", ["App", "ID", "Thread Counts"])

        self.client = client

        self.view_button.clicked.connect(self.view_function)
        self.terminate_button.clicked.connect(self.kill_function)
        self.start_button.clicked.connect(self.start_function)

    def view_function(self):
        try:
            self.client.Command({"state": "GetApps"})
            data = self.client.bytes2dict(self.client.Recv())
            self.insert_data(data)

        except Exception as e:
            msg = "Cannot view.\n" + str(e)
            PopUp.show_popup(self, "Error", msg)

    def kill_function(self):
        def kill_app(app_id, parent = None):
            try:
                self.client.Command({"state": "KillApp"})
                self.client.Command({"app_id": app_id})
                data = self.client.bytes2dict(self.client.Recv())
                PopUp.show_popup(parent, "SUCCESS", data["message"], 
                                 closeParent=True)
            except Exception as e:
                msg = f"Cannot kill {app_id}.\n" + str(e)
                PopUp.show_popup(parent, "Error", msg, 
                                 closeParent=True)
        self.kill_input_button_view = InputButtonView(
            "Kill app", "Enter app ID", "Kill",
            kill_app)
        self.kill_input_button_view.show()
    def start_function(self):
        def start_app(app_name, parent = None):
            try:
                self.client.Command({"state": "StartApp"})
                self.client.Command({"app_name": app_name})
                data = self.client.bytes2dict(self.client.Recv())
                PopUp.show_popup(parent, "SUCCESS", data["message"],
                                 closeParent=True)
                
            except Exception as e:
                msg = f"Cannot start {app_name}.\n" + str(e)
                PopUp.show_popup(parent, "Error", msg, 
                                 closeParent=True)
        self.start_input_button_view = InputButtonView(
            "Start app", "Enter app Name", "Start", 
            start_app)
        self.start_input_button_view.show()
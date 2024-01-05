from mvc.model.person_model import model


def controller(name):
    print("Controller")
    print("اولین شغل من مدیریت خطا است")
    print("دومین شغل من اعتبار سنجی داده ها است")
    print("----------------------------------")
    return model(name)
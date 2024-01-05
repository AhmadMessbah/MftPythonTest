from mvc.controller.person_controller import controller


def view():
    print("View")
    print("شغل من صرفا نمایش ظاهر برنامه است")
    print("----------------------------------")
    name = input("Enter Name : ")
    return controller(name)
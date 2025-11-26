class Notification:
    def get_notification(self):
        pass

class Instagram(Notification):

    def get_notification(self):
        print("Instagram notification")

class Facebook(Notification):

    def get_notification(self):
        print("Facebook notification")

inst=Instagram()
inst.get_notification()

face=Facebook()
face.get_notification()
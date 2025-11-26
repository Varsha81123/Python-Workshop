class Aadhar:
    def __init__(self,name,aadhar_no,dob,finger_print,retina):
        self.name=name
        self.aadhar_no=aadhar_no
        self.dob=dob
        self._finger_print=finger_print
        self.__retina=retina

    def display_userData(self):
        print(f"Aadhar name is {self.name}")
        print(f"Aadhar number is :{self.aadhar_no}")
        print(f"DOB {self.dob}")
        print(self._finger_print)#protected
        print(self.__retina)#private

    def getRetina(self):
        print(f"{self.__retina}")

var=Aadhar("Varsha",692761548756,"21/08/2003","vbs","rrr")
var.display_userData()
var.getRetina()

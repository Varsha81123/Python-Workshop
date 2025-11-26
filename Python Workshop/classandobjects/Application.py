class Application:
    def __init__(self,application_name,category,company,size,no_of_users,ratings):
        self.application_name=application_name
        self.category=category
        self.company=company
        self.size=size
        self.no_of_users=no_of_users
        self.ratings=ratings

    def signup(self):
        print(f"Signup done,{self.application_name}")

    def login(self):
        print(f"Welcome to {self.application_name}")

    def logout(self):
        print("Thank you for using")
    def info(self):
        print(f"Welcome to {self.application_name},its category is {self.category},it consumes {self.size}MB,and it has {self.no_of_users}users with rating{self.ratings}")


app1=Application("Instagram","social media","meta",42.45,1000,4.4)
app2=Application("Facebook","social media","meta",50,2000,4)
app3=Application("Flipkart","shopping","walmart",60,5000,4.1)
app4=Application("BGMI","Gaming","krafton",900,20000,4.6)

app1.signup()
app1.login()
app1.logout()


app2.signup()
app2.login()
app2.logout()

app3.signup()
app3.login()
app3.logout()

app4.signup()
app4.login()
app4.logout()

app1.info()
app2.info()
app3.info()
app4.info()



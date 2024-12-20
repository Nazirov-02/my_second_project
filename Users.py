from collections import namedtuple

User = namedtuple('users',['full_name','age','phone_number'])

class Users:
      def __init__(self):
          self.data = []

      # add users function
      def add_users(self,full_name,age,phone_number):
          # check phone is already exists or not
          for data in self.data:
            if data.phone_number == phone_number:
                raise ValueError(f'This {phone_number} phone number is already exists ')
          user = User(full_name,age,phone_number)
          self.data.append(user)

      # This function show all users data
      def show_all_data(self):
          for data in self.data:
            print(f"full name = {data.full_name} age = {data.age} phone number = {data.phone_number}")

users = Users()
users.add_users('Donald Tramp',69,+998999999999)
users.add_users('Joe Biden',82,+998990009900)
users.show_all_data()

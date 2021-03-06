class User :
    '''
    class to generate new intances of a user
    '''
    user_list = []

    def __init__ (self,username,password):
        '''
        method that helps define the properties of our objects.
        '''
        self.username = username
        self.password = password
    
    def save_user(self):
        '''
        method that saves new user instance in user list
        '''
        User.user_list.append(self)

    def delete_user(self):
        '''
        method to delete the user information
        '''
        User.user_list.remove(self)

    @classmethod
    def display_user(cls):
        '''
        method to display infromation passed in user list
        '''
        return cls.user_list

    @classmethod
    def user_verif(cls, username, password):
        '''
        method to verify user info
        '''
        my_user = ""
        for user in cls.user_list:

            if(user.username == username and user.password == password):

                return True 

class Credentials :
    '''
    class to create credential instances
    '''
    creds_list = []
    
    def __init__(self, account, user_name, pass_word):
        '''
        method for credential properties
        '''
        self.account = account
        self.user_name = user_name
        self.pass_word = pass_word

    def save_creds(self):
        '''
        method to save credentials in credential list
        '''
        Credentials.creds_list.append(self)

    def delete_creds(self):
        '''
        method to remove credential info from our list
        '''
        Credentials.creds_list.remove(self)
    @classmethod
    def find_creds(cls, account):
        '''
        method that shows credentials info using account
        '''
        for credential in cls.creds_list :
            if credential.account == account:
                return credential
    @classmethod
    def display_creds(cls):
        '''
        method that displays credentials
        '''
        return cls.creds_list

    
    
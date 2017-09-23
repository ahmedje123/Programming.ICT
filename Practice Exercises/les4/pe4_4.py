oldPassword = input('Wat is uw oude wachtwoord?')
newPassword = input('Wat wordt uw nieuwe wachtwoord?')


def new_password(oldPassword, newPassword):

    if len(newPassword) >= 6 and newPassword != oldPassword:
        print('True')

    else:
        print('False')


new_password(oldPassword, newPassword)
from django.db import models, DatabaseError
from account.storage import AccountImageStorage
from account.util.verify_code import generate_verify_code


class Account(models.Model):
    user_name = models.CharField(max_length=20)
    nick_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    photo = models.ImageField(upload_to="static/accountImage", null=False, storage=AccountImageStorage())
    created = models.DateTimeField(auto_now_add=True)
    last_visit = models.DateTimeField(auto_now=True)
    email = models.EmailField()
    verify_code = models.CharField(max_length=128)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    @staticmethod
    def sign_in(user_name, password):
        account = Account.objects.filter(user_name=user_name, password=password)
        if account.count() == 1:
            return account[0]
        else:
            return None

    @staticmethod
    def create_account(user_name, password, nick_name, photo, email, last_name, first_name):
        if (not Account.is_nick_name_exist(nick_name)) & (not Account.is_user_name_exist(user_name)) & (
                not Account.is_email_exist(email)):
            new_account = Account(user_name=user_name, password=password,
                                  nick_name=nick_name, photo=photo,
                                  last_name=last_name, first_name=first_name,
                                  email=email)
            new_account.save()
            return Account.objects.filter(user_name=user_name).first()
        else:
            return None

    @staticmethod
    def is_user_name_exist(user_name):
        return not (Account.objects.filter(user_name=user_name).count() == 0)

    @staticmethod
    def is_nick_name_exist(nickname):
        return not (Account.objects.filter(nick_name=nickname).count() == 0)

    @staticmethod
    def is_email_exist(email):
        return not Account.objects.filter(email=email).count() == 0

    @staticmethod
    def modify_account(id, nick_name, photo, first_name, last_name):
        user = Account.objects.get(id=id)
        user.nick_name = nick_name
        if photo is not None:
            user.photo = photo
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return user

from django.db import models

# Create your models here.
from account.models import Account
from ideas.models import Idea


class Fund(models.Model):
    fonder = models.ForeignKey(Account)
    idea = models.ForeignKey(Idea)
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(max_length=100)

    @staticmethod
    def make_fund(fonder, idea, amount, comment):
        fund = Fund(fonder_id=fonder, idea_id=idea, amount=amount, comment=comment)
        fund.save()
        return fund

    @staticmethod
    def cancel_fund(fonder, idea):
        fund = Fund.objects.get(fonder_id=fonder, idea_id=idea).delete()
        return fund

    @staticmethod
    def get_fund_by_fonder(user_id):
        return Fund.objects.filter(fonder=user_id)

    @staticmethod
    def get_fund_by_idea(idea_id):
        return Fund.objects.filter(idea_id=idea_id)

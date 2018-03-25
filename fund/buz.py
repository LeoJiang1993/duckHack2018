from fund.models import Fund


def get_fund_by_fonder(user_id):
    return Fund.get_fund_by_fonder(user_id=user_id)


def fund(user_id, idea_id, amount, comment):
    return Fund.make_fund(user_id, idea_id, amount, comment)


def get_fund_by_idea(idea_id):
    return Fund.get_fund_by_idea(idea_id)


def cancel_fund(user_id, idea_id):
    return Fund.cancel_fund(user_id, idea_id)

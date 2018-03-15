from .spam_assassin_rule import SpamAssassinRule

class SpamFilterResults(object):
    """SpamFilterResults.

    :param spam_assassin:
    :type spam_assassin: list[~mailosaur.models.SpamAssassinRule]
    """

    def __init__(self, data=dict):
        self.spam_assassin = [SpamAssassinRule(i) for i in data.get('spamAssassin', None)]

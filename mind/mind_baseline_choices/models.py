from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Daniel Parra '

doc = """
Mind Game - Baseline
"""


class Constants(BaseConstants):
    name_in_url = 'exp_t0b'
    players_per_group = None
    num_rounds = 1

    payoff_win = c(2.5)
    payoff_lose = c(0.3)
    completion_fee = c(1.15)
    beliefs_payoff = c(0.3)

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):


# For beliefs elicitation, needed for compute payoffs
    report1 = models.BooleanField(
        choices=[
            [True, 'Yes'],
            [False, 'No'],
        ],
        widget=widgets.RadioSelect,
        label="Please indicate whether the color behind the card you picked is the color that you thought of:"
    )
    randomDraw1 = models.IntegerField()
    guess_payoff = models.CurrencyField()
    random_num = models.IntegerField()
    not_a_bot = models.IntegerField()








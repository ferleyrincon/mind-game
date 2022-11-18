from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class pick_colorA(Page):
    def is_displayed(self):
        return self.player.id_in_group == 1

    def get_timeout_seconds(self):
        if self.participant.vars.get('is_dropout'):
            return 1  # instant timeout, 1 second
        else:
            return 5 * 60


class R1_draw(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.player.id_in_group == 1

    def get_form_fields(self):
        return ['randomDraw1']

    def get_timeout_seconds(self):
        if self.participant.vars.get('is_dropout'):
            return 1  # instant timeout, 1 second
        else:
            return 5 * 60

class R1_Choice(Page):
    def is_displayed(self):
        return self.player.id_in_group == 1

    form_model = 'player'
    form_fields = ['report1']

    def before_next_page(self):
        if self.player.report1 == 0:
            self.participant.vars['payoff_1'] = 1000
        else:
            self.participant.vars['payoff_1'] = 5000

class WaitForP1(WaitPage):
    pass

class Inst_guess(Page):
    def is_displayed(self):
        return self.player.id_in_group == 1

    form_model = 'player'
    form_fields = ['times_clicked_info']

    def get_timeout_seconds(self):
        if self.participant.vars.get('is_dropout'):
            return 1  # instant timeout, 1 second
        else:
            return 5 * 60

    def before_next_page(self):

        import random
        self.player.robot = random.randint(1, 100)
        self.player.random_num = random.randint(1, 100)

        if self.participant.vars.get('is_dropout'):
            self.player.not_a_bot = 0
        else:
            self.player.not_a_bot = 1


class guess(Page):
    def is_displayed(self):
        return self.player.id_in_group == 1

    form_model = 'player'

    def get_form_fields(self):
        return ['guess_p1', 'confidence_guess']

    def get_timeout_seconds(self):
        if self.participant.vars.get('is_dropout'):
            return 1  # instant timeout, 1 second
        else:
            return 5 * 60

    def before_next_page(self):
        if self.timeout_happened:
            self.participant.vars['is_dropout'] = True
            self.player.guess_p1 = 1
            self.player.confidence_guess = 1
        if self.participant.vars.get('is_dropout'):
            self.player.not_a_bot = 0
        else:
            self.player.not_a_bot = 1

        self.player.players_in_group = len(self.player.get_others_in_group()) + 1

class pick_colorB(Page):
    def is_displayed(self):
        return self.player.id_in_group == 2

    def get_timeout_seconds(self):
        if self.participant.vars.get('is_dropout'):
            return 1  # instant timeout, 1 second
        else:
            return 5 * 60

    def before_next_page(self):
        if self.timeout_happened:
            self.participant.vars['is_dropout'] = True


class R2_draw(Page):
    def is_displayed(self):
        return self.player.id_in_group == 2

    form_model = 'group'

    def get_form_fields(self):
        return ['randomDraw2']

    def get_timeout_seconds(self):
        if self.participant.vars.get('is_dropout'):
            return 1  # instant timeout, 1 second
        else:
            return 5 * 60

    def before_next_page(self):
        if self.timeout_happened:
            self.participant.vars['is_dropout'] = True

        if self.participant.vars.get('is_dropout'):
            self.player.not_a_bot = 0
        else:
            self.player.not_a_bot = 1


class R2_Choice(Page):
    def is_displayed(self):
        return self.player.id_in_group == 2

    form_model = 'group'
    form_fields = ['report2']

    def get_timeout_seconds(self):
        if self.participant.vars.get('is_dropout'):
            return 1  # instant timeout, 1 second
        else:
            return 5 * 60

    def before_next_page(self):
        if self.timeout_happened:
            self.participant.vars['is_dropout'] = True
            self.group.report2 = True
        if self.participant.vars.get('is_dropout'):
            self.player.not_a_bot = 0
        else:
            self.player.not_a_bot = 1

        self.player.players_in_group = len(self.player.get_others_in_group()) + 1


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'

class Results(Page):
    def vars_for_template(self): 
        return {
            'valor_pagar':self.participant.vars.get('payoff_1')
        }

    def is_displayed(self):
        return self.player.id_in_group == 1



page_sequence = [
    pick_colorA,
    R1_draw,
    R1_Choice,
    Results
]

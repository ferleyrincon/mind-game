from otree.api import Currency as c, currency_range
from . import pages
from otree.api import Bot, SubmissionMustFail
from .models import Constants

import random

class PlayerBot(Bot):

    def play_round(self):
        print('vars is', self.participant.vars['treat'])

        random_d1 = random.choice([1, 2, 3, 4])
        random_d2 = random.choice([1, 2, 3, 4])
        random_r1 = random.choice([True, False, False])
        random_r2 = random.choice([True,False, False])

        if self.participant.vars['treat'] == 'baseline':
            if self.player.id_in_group == 1:
                yield pages.pick_colorA
                yield pages.R1_draw, dict(randomDraw1=random_d1)
                yield pages.R1_Choice, dict(report1=random_r1)
                yield pages.Inst_guess
                yield SubmissionMustFail(pages.guess, dict(guess_p1=True, confidence_guess=101))
                yield pages.guess, dict(guess_p1=True, confidence_guess=50)
                yield pages.Results
            else:
                yield pages.pick_colorB
                yield pages.R2_draw, dict(randomDraw2=random_d2)
                yield pages.R2_Choice, dict(report2=random_r2)
                yield pages.Results

        print('I have a profit of', self.player.payoff)




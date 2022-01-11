#Change fields here.

from pykintone import model

class Hankyo(model.kintoneModel):
    def __init__(self):
        super(Hankyo, self).__init__()
        self.title=""
        self.mail_from=""
        self.mail_to=""
        self.main=""
        self.slackChannel=""
        self.slackTS=""

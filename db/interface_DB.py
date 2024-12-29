from interface import Interface, implements


class ConnDB(Interface):

    def __init__(self, conn: str):
        pass

    def connection(self):
        pass

    def check_answer_on_question(self):
        pass

    def add_message(self):
        pass

    def get_all_record(self):
        pass

    def get_all_chats(self):
        pass

    def delete_all_message(self):
        pass

    def delete_message(self, id_: str):
        pass

    def sever(self):
        pass

from .. import loader, utils
from random import randrange
from telethon import functions
from asyncio import sleep

def register(cb):
    cb(DancingwithdeathMod())
class DancingwithdeathMod(loader.Module):
    strings = {'name': 'Dancing with death'}

    async def deadplaycmd(self, die):
        args = utils.get_args_raw(die)
        if args == "rules":
            await die.edit("������� ������ \n\n>���� ������� ������� �������� ����� �� 1 �� 6 \n\n>���� ���� ����� ������� ���� ��������� � ��������� �� 1 �� 6\n\n>��� ������� ���� ��� ����� ��������� - �� ��������(������� �������)\n\n>� ����� ��������� ������� �� ��������� � �����\n\n\n->��� ��������� ������ ������� - <b>.deadplay <����� �� 1 �� 6></b> ������ - .deadplay 5")
            return
        if int(args) > 0 and int(args) < 7:
            await die.edit("������� ����������� (0)")
            await sleep(1)
            await die.edit("������� ����������� (1)")
            await sleep(1)
            await die.edit("������� ����������� (2)")
            await sleep(1)
            await die.edit("������� ����������� (3)")
            await sleep(1)
            deadnumber = randrange(1, 6)
            if deadnumber == int(args):
                await die.edit("�� ��� ���! �� ���!!!!! �� �����!!!!!!")
                await die.edit("����... �� ��������...")
                await die.edit("�������...")
            else:
                await die.edit("���... ��� ��� ���... ���� ����� {args} , ����� ������ {deadnumber}")
        else:
            await die.edit("��� ��������� ������� �������, ����� ������ �� 1 �� 6")
            return
import random
import os
from typing import List

import discord

TOKEN = os.getenv('TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print('ログインしました')


# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # botの発言を弾く
    if message.author.bot:
        return
    if message.content == '/neko':
        await message.channel.send('にゃーん')

    if message.content == '/dice':
        text = str(random.randint(1, 6))
        await message.channel.send(text)
    if message.content == '/omikuji':
        text = str(get_slip_result(10))
        await message.channel.send(text)


def get_slip_result(num: int) -> str:
    num_ = max(10, num)
    dice = random.randint(0, num_)
    slip = generate_fortune_slip(num_)
    return slip[dice]


def generate_fortune_slip(base_num: int) -> List[str]:
    from math import ceil

    def _get_range(_num: int, percentage: int) -> int:
        return max(1, ceil(_num * percentage / 100))

    # 10%, 35%, 35%, 10%
    very_good_luck = ['大吉' for _ in range(_get_range(base_num, 10))]
    good_luck = ['吉' for _ in range(_get_range(base_num, 35))]
    bad_luck = ['凶' for _ in range(_get_range(base_num, 35))]
    extremely_bad_luck = ['大凶' for _ in range(_get_range(base_num, 10))]

    return very_good_luck + good_luck + bad_luck + extremely_bad_luck


client.run(TOKEN)

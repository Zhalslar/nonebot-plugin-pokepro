from nonebot import get_plugin_config, on_notice
from .config import Config
from nonebot.adapters.onebot.v11 import PokeNotifyEvent, Bot, MessageSegment
import random

config = get_plugin_config(Config)


def _check(event: PokeNotifyEvent):
    return event.target_id == event.self_id


poke_pro = on_notice(rule=_check)


@poke_pro.handle()
async def _(bot: Bot, event: PokeNotifyEvent):
    random_number = random.random()  # 在[0.0, 1.0)范围内生成一个随机浮点数

    if random_number < 0.25:  # 返回戳一戳
        if event.group_id:  # 如果是群聊中的戳一戳
            await bot.group_poke(group_id=event.group_id, user_id=event.user_id)
        else:  # 如果是私聊中的戳一戳
            await bot.poke(user_id=event.user_id)

    elif random_number < 0.5:  # 返回文本
        await poke_pro.finish(MessageSegment.text('text'))

    elif random_number < 0.65:  # 返回表情包
        await poke_pro.finish(MessageSegment.text('emotion'))

    elif random_number < 0.8:  # 返回QQ表情
        await poke_pro.finish(MessageSegment.face(random.randint(1, 221)))
        
    elif random_number < 0.9:  # 返回语音
        await poke_pro.finish(MessageSegment.text('voice'))

    else:  # 禁言
        await poke_pro.finish(MessageSegment.text('ban'))

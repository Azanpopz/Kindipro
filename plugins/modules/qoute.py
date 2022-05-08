import itertools
import os
import asyncio
import secrets
import logging
import configparser
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from textwrap import TextWrapper
from pyrogram import Client
from pyrogram import Client, idle, filters
from pyrogram.types import Message
from PIL import Image, ImageDraw, ImageFont, ImageChops





async def get_y_and_heights(text_wrapped, dimensions, margin, font):
    _, descent = font.getmetrics()
    line_heights = [font.getmask(text_line).getbbox()[3] + descent + margin for text_line in text_wrapped]
    line_heights[-1] -= margin
    height_text = sum(line_heights)
    y = (dimensions[1] - height_text) // 2
    return y, line_heights


async def crop_to_circle(im):
    bigsize = (im.size[0] * 3, im.size[1] * 3)
    mask = Image.new("L", bigsize, 0)
    ImageDraw.Draw(mask).ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(im.size, Image.ANTIALIAS)
    mask = ImageChops.darker(mask, im.split()[-1])
    im.putalpha(mask)


async def rounded_rectangle(rectangle, xy, corner_radius, fill=None, outline=None):
    upper_left_point = xy[0]
    bottom_right_point = xy[1]

    rectangle.pieslice(
        [upper_left_point, (upper_left_point[0] + corner_radius * 2, upper_left_point[1] + corner_radius * 2)],
        180,
        270,
        fill=fill,
        outline=outline
    )
    rectangle.pieslice(
        [(bottom_right_point[0] - corner_radius * 2, bottom_right_point[1] - corner_radius * 2), bottom_right_point],
        0,
        90,
        fill=fill,
        outline=outline
    )
    rectangle.pieslice([(upper_left_point[0], bottom_right_point[1] - corner_radius * 2),
                        (upper_left_point[0] + corner_radius * 2, bottom_right_point[1])],
                       90,
                       180,
                       fill=fill,
                       outline=outline
                       )
    rectangle.pieslice([(bottom_right_point[0] - corner_radius * 2, upper_left_point[1]),
                        (bottom_right_point[0], upper_left_point[1] + corner_radius * 2)],
                       270,
                       360,
                       fill=fill,
                       outline=outline
                       )
    rectangle.rectangle(
        [
            (upper_left_point[0], upper_left_point[1] + corner_radius),
            (bottom_right_point[0], bottom_right_point[1] - corner_radius)
        ],
        fill=fill,
        outline=fill
    )
    rectangle.rectangle(
        [
            (upper_left_point[0] + corner_radius, upper_left_point[1]),
            (bottom_right_point[0] - corner_radius, bottom_right_point[1])
        ],
        fill=fill,
        outline=fill
    )
    rectangle.line([(upper_left_point[0] + corner_radius, upper_left_point[1]),
                    (bottom_right_point[0] - corner_radius, upper_left_point[1])], fill=outline)
    rectangle.line([(upper_left_point[0] + corner_radius, bottom_right_point[1]),
                    (bottom_right_point[0] - corner_radius, bottom_right_point[1])], fill=outline)
    rectangle.line([(upper_left_point[0], upper_left_point[1] + corner_radius),
                    (upper_left_point[0], bottom_right_point[1] - corner_radius)], fill=outline)
    rectangle.line([(bottom_right_point[0], upper_left_point[1] + corner_radius),
                    (bottom_right_point[0], bottom_right_point[1] - corner_radius)], fill=outline)





async def create_sticker(c: Client, m: Message):
    if len(m.text) < 150:
        body_font_size = 40
        wrap_size = 30
    elif len(m.text) < 250:
        body_font_size = 50
        wrap_size = 35
    elif len(m.text) < 550:
        body_font_size = 20
        wrap_size = 40
    elif len(m.text) < 1050:
        body_font_size = 12
        wrap_size = 90
    else:
        body_font_size = 15
        wrap_size = 150

    font = ImageFont.truetype("Segan-Light.ttf", body_font_size)
    font_who = ImageFont.truetype("TitilliumWeb-Bold.ttf", 50)
    AKKU = ImageFont.truetype("Sticky-Notes.ttf", body_font_size)

    img = Image.new("RGBA", (512, 512), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle = rounded_rectangle

    wrapper = TextWrapper(width=wrap_size, break_long_words=False, replace_whitespace=False)
    lines_list = [wrapper.wrap(i) for i in m.text.split('\n') if i != '']
    text_lines = list(itertools.chain.from_iterable(lines_list))

    y, line_heights = await get_y_and_heights(
        text_lines,
        (512, 512),
        30,
        font
    )

    in_y = y
    rec_y = (y + line_heights[0]) if wrap_size >= 40 else y

    for i, _ in enumerate(text_lines):
        rec_y += line_heights[i]

    await rounded_rectangle(draw, ((90, in_y), (512, rec_y + line_heights[-1])), 10, fill="#000000")

    f_user = m.from_user.first_name + " " + m.from_user.last_name if m.from_user.last_name else m.from_user.first_name
    draw.text((100, y), f"{f_user}»", "#ffffff", font=font_who)

    y = (y + (line_heights[0] * (25/100))) if wrap_size >= 40 else y

    for i, line in enumerate(text_lines):
        x = 100
        y += line_heights[i]
        draw.text((x, y), line, "#ffffff", font=font_who)

    try:
        user_profile_pic = await c.get_profile_photos(m.from_user.id)
        photo = await c.download_media(user_profile_pic[0].file_id, file_ref=user_profile_pic[0].file_ref)
    except Exception as e:
        photo = "default.jpg"
        logging.error(e)

    im = Image.open(photo).convert("RGBA")
    im.thumbnail((60, 60))
    await crop_to_circle(im)
    img.paste(im, (20, in_y))

    sticker_file = f"{secrets.token_hex(2)}.webp"

    img.save(sticker_file)

    await m.reply_sticker(
        sticker=sticker_file
    )
    try:
        if os.path.isfile(sticker_file):
            os.remove(sticker_file)

        if os.path.isfile(photo) and (photo != "default.jpg"):
            os.remove(photo)
    except Exception as e:
        logging.error(e)


@Client.on_message(filters.command(['q']))
async def create_sticker_private_handler(c: Client, m: Message):
    s = await m.reply_text("...")
    await create_sticker(c, m)
    await s.delete()


@Client.on_message(filters.command(['quote']))
async def create_sticker_group_handler(c: Client, m: Message):
    s = await m.reply_text("...", reply_to_message_id=m.message_id)
    await create_sticker(c, m.reply_to_message)
    await s.delete()




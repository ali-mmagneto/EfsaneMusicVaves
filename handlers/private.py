from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as BN
from helpers.filters import command, other_filters2


@Client.on_message(command(["start", f"start"]))
async def start(_, message: Message):
    await message.reply_photo("https://telegra.ph/file/c6c4493b5f3a9c03c8e7f.jpg")
    await message.reply_text(
        f"""**Merhaba ben botum, {message.from_user.mention} 🎵
Sesli sohbetlerde müzik çalabilen botum. Ban yetkisiz, Ses yönetimi yetkisi verip, Asistanı gruba ekleyiniz.\n\nDüzen Tasarım by @mmagneto [Kişisel Blogu 🎙️](https://t.me/mmagneto3).
 **""",

        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Grubunuza Ekle ➕", url="https://t.me/alimuzikbot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔊 Asistan", url="https://t.me/alimuzikasistant" 
                    ),
                    InlineKeyboardButton(
                        "💬 Kişisel Blog", url="https://t.me/mmagneto3"
                    ),
                    InlineKeyboardButton(
                        "🙎‍♂️ Geliştirici", url="https://t.me/mmagneto") 
                ],
                [
                    InlineKeyboardButton(
                        "komik bir vidyo", url="https://t.me/mmagneto3/31"
                    )
                ]
            ]
        ), 
     disable_web_page_preview=True
   ) 

@Client.on_message(command(["bilgi"])) 
async def bilgi(_, message: Message):
      await message.reply_text(f"**Merhaba {message.from_user.mention}!\n Bu botun bilgi menüsü 📚\n\n ▶️ /play - şarkı çalmak için youtube url'sine veya şarkı dosyasına yanıt verme\n ▶️ /play <song name> - istediğiniz şarkıyı çalınız\n 🔴 /ytplay <Sorgu> - youtube üzerinden çalar\n 🎵 /bul <song name> - istediğiniz şarkıları hızlı bir şekilde bulun\n 🎵 /vbul istediğiniz videoları hızlı bir şekilde bulun\n 🔍 /ara <query> - youtube'da ayrıntıları içeren videoları arama\n\n Yalnızca yöneticiler için..\n ⏩ /resume - şarkı çalmaya devam et\n ⏹ /end - müzik botunu kapatmak için\n 🔼 /ver botun sadece yönetici için kullanılabilir olan komutlarını kullanabilmesi için kullanıcıya yetki ver\n 🔽 /al botun yönetici komutlarını kullanabilen kullanıcının yetkisini al\n 🎚 /ses asistan hesabın ses seviyesini kontrol et\n\n ⚪ /katil - Müzik asistanı grubunuza katılır\n ⚫ /ayril - Müzik asistanı grubunuzu terk eder.**", 
      reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "👨‍🔧 Geliştirici", url="https://t.me/mmagneto")
                 ]
             ]
         )
    )

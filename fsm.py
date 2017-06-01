from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_user(self, update):
        text = update.message.text
        return text.lower() == 'start'

    def is_going_to_state1(self, update):
        text = update.message.text
        return text.lower() == '醫院'

    def is_going_to_state11(self, update):
        text = update.message.text
        return text.lower() == '成'

    def is_going_to_state12(self, update):
        text = update.message.text
        return text.lower() == '台'

    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == '診所'

    def is_going_to_state21(self, update):
        text = update.message.text
        return text.lower() == '皮'

    def is_going_to_state211(self, update):
        text = update.message.text
        return text.lower() == '麥'

    def is_going_to_state22(self, update):
        text = update.message.text
        return text.lower() == '眼'

    def is_going_to_state221(self, update):
        text = update.message.text
        return text.lower() == '李'

    def is_going_to_state222(self, update):
        text = update.message.text
        return text.lower() == '陳'

    def is_going_to_state223(self, update):
        text = update.message.text
        return text.lower() == '曾'

    def is_going_to_state23(self, update):
        text = update.message.text
        return text.lower() == '內'

    def is_going_to_state231(self, update):
        text = update.message.text
        return text.lower() == '詠'

    def is_going_to_state24(self, update):
        text = update.message.text
        return text.lower() == '骨'

    def is_going_to_state241(self, update):
        text = update.message.text
        return text.lower() == '開'

    def is_going_to_state242(self, update):
        text = update.message.text
        return text.lower() == '薛'

    def is_going_to_state25(self, update):
        text = update.message.text
        return text.lower() == '牙'

    def is_going_to_state251(self, update):
        text = update.message.text
        return text.lower() == '楓'

    def is_going_to_state252(self, update):
        text = update.message.text
        return text.lower() == '木'

    def is_going_to_state3(self, update):
        text = update.message.text
        return text.lower() == '藥局'

    def back_to_state1(self, update):
        text = update.message.text
        return text.lower() == 'back'

    def back_to_state22(self, update):
        text = update.message.text
        return text.lower() == 'back'

    def back_to_start(self, update):
        text = update.message.text
        return text.lower() == 'seeya'

    def back_to_state24(self, update):
        text = update.message.text
        return text.lower() == 'back'

    def back_to_state25(self, update):
        text = update.message.text
        return text.lower() == 'back'

    def end(self, update):
        text = update.message.text
        return text.lower() == 'end'

    def on_enter_user(self, update):
        update.message.reply_text("醫院\n診所\n藥局")
        #self.go_back(update)

    def on_exit_user(self, update):
        print('Leaving user')

    def on_enter_state1(self, update):
        update.message.reply_text("成大醫院\n台南醫院")
        #self.go_back(update)

    def on_exit_state1(self, update):
        print('Leaving state1')

    def on_enter_state11(self, update):
        update.message.reply_text('院 址：臺南市勝利路138號\n'
                                  '電 話：(06)2353535\n'
                                  '網 站：http://www.hosp.ncku.edu.tw/nckm/index.aspx\n'
                                  '網路掛號 : http://service.hosp.ncku.edu.tw/Tandem/DeptUI.aspx?Lang=')
        #update.message.reply_photo('http://i.imgur.com/ENumiGZ.png')
        self.go_back(update)

    def on_exit_state11(self, update):
        print('Leaving state11')

    def on_enter_state12(self, update):
        #update.message.reply_text("I'm entering state12")
        update.message.reply_text('院 址：台南市中西區中山路125號\n'
                                  '電 話：(06)2200055轉9\n'
                                  '網 站：http://www.tnhosp.mohw.gov.tw/\n'
                                  '網路掛號 : http://tnweb.tnhosp.mohw.gov.tw/OINetReg/OINetReg.Reg/Reg_NetReg.aspx')
        self.go_back(update)

    def on_exit_state12(self, update):
        print('Leaving state12')

    def on_enter_state2(self, update):
        update.message.reply_text("皮膚科\n眼科\n內科\n骨科/復健科\n牙科")
        #self.go_back(update)

    def on_exit_state2(self, update):
        print('Leaving state2')

    def on_enter_state21(self, update):
        update.message.reply_text("麥鎮平皮膚專科診所")
        #self.go_back(update)

    def on_exit_state21(self, update):
        print('Leaving state2')

    def on_enter_state211(self, update):
        update.message.reply_text('地 址：台南市長榮路三段129號\n'
                                  '電 話：(06)2342219')
        update.message.reply_photo('http://i.imgur.com/ENumiGZ.png')
        self.go_back(update)

    def on_exit_state211(self, update):
        print('Leaving state211')

    def on_enter_state22(self, update):
        update.message.reply_text("李尚儒眼科附設眼鏡部\n陳秀琴眼科診所附設眼鏡部\n曾順輝眼科診所")
        #self.go_back(update)

    def on_exit_state22(self, update):
        print('Leaving state22')

    def on_enter_state221(self, update):
        update.message.reply_text('地 址 : 台南市長榮路二段75號\n'
                                  '電 話 :(06)2757789\t\t(06)2362490')
        update.message.reply_photo('http://i.imgur.com/W4oJHm1.png?1')
        #self.go_back(update)

    def on_exit_state221(self, update):
        print('Leaving state221')

    def on_enter_state222(self, update):
        update.message.reply_text('地 址：台南市東安路146-1號\n'
                                  '電 話：(06)2376767\t\t(06)2749799')
        update.message.reply_photo('http://i.imgur.com/EaW0z0I.png')
        #self.go_back(update)

    def on_exit_state222(self, update):
        print('Leaving state222')

    def on_enter_state223(self, update):
        update.message.reply_text('地 址：台南市小東路167號\n'
                                  '電 話: (06)2354988')
        update.message.reply_photo('http://i.imgur.com/0Y1oFxI.png')
        #self.go_back(update)

    def on_exit_state223(self, update):
        print('Leaving state223')

    def on_enter_state23(self, update):
        update.message.reply_text("詠心診所")
        #self.go_back(update)

    def on_exit_state23(self, update):
        print('Leaving state23')

    def on_enter_state231(self, update):
        update.message.reply_text('地 址：台南市東光路一段130號\n'
                                  '電 話：(06)2089877')
        update.message.reply_photo('http://i.imgur.com/6WnxLlf.png')
        self.go_back(update)

    def on_exit_state231(self, update):
        print('Leaving state231')

    def on_enter_state24(self, update):
        update.message.reply_text("開元骨外科診所\n薛澤杰復健診所")
        #self.go_back(update)

    def on_exit_state24(self, update):
        print('Leaving state24')

    def on_enter_state241(self, update):
        update.message.reply_text('地 址：台南市北區林森路三段338號\n'
                                  '電 話：(06)2361566')
        update.message.reply_photo('http://i.imgur.com/WeyPd3Q.png')
        #self.go_back(update)

    def on_exit_state241(self, update):
        print('Leaving state241')

    def on_enter_state242(self, update):
        update.message.reply_text('地 址：台南市東門路一段298號1樓\n'
                                  '電 話：(06)2386150')
        update.message.reply_photo('http://i.imgur.com/IuUqtPM.png')
        #self.go_back(update)

    def on_exit_state242(self, update):
        print('Leaving state242')

    def on_enter_state25(self, update):
        update.message.reply_text("楓鄰牙醫診所\n木棉咬合疼痛牙醫診所")
        #self.go_back(update)

    def on_exit_state25(self, update):
        print('Leaving state25')

    def on_enter_state251(self, update):
        update.message.reply_text('地 址：台南市北區開元路485巷21-23號1樓\n'
                                  '電 話：(06)2389085')
        #update.message.reply_photo('http://i.imgur.com/IuUqtPM.png')
        self.go_back(update)

    def on_exit_state251(self, update):
        print('Leaving state251')

    def on_enter_state252(self, update):
        update.message.reply_text('地 址：台南市東區長榮路一段180號\n'
                                  '電 話：(06)2005129')
        self.go_back(update)

    def on_exit_state252(self, update):
        print('Leaving state252')

    def on_enter_state3(self, update):
        update.message.reply_text('24H台安藥局(台南市東區中華東路一段6號)\n'
                                  '杏一醫療用品(台南市東區東豐路155號)\n'
                                  '小太陽藥局(台南市東區東平路13號)\n'
                                  '王藥局(台南市東區小東路190之1號)\n'
                                  '文成藥局(台南市東區東寧路43之1號)\n'
                                  '佳禾藥局(台南市東區東寧路213號)\n'
                                  '榮記健康藥局(台南市東區育樂街156-4號)')
        #update.message.reply_text("*bold* _italic_ [link](http://google.com).")
        #update.message.reply_photo('https://telegram.org/img/t_logo.png')
       # self.sendMessage(chat_id=update.message.chat_id,text="*bold* _italic_ [link](http://google.com).",parse_mode=telegram.ParseMode.MARKDOWN)
        self.go_back(update)

    def on_exit_state3(self, update):
        print('Leaving state3')



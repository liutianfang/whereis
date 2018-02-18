#coding=utf8
import sys

class Processor():
    modal_particle = {"zh": {"了", "啦","啊"}}
    prepositions={"en":{"on":["on ","over "],"in":["in ","into ","inside "]}}

    command=""
    lang=""
    deviceID=""
    action="init"
    paras={}
    localizer=''
    preposition=''

    def __init__(self):
        self.paras={}

    def process(self, lang, command, deviceID):
        self.command=command
        self.lang=lang.lower()
        # 搜索关键词,，确认动作
        self.searchActionKeyword()
        # 分离变量
        self.paras = self.getVariable()

        # ret = searchDB()

        returnSentense = self.generateReturn()

        return returnSentense

    def generateReturn(self):
        if self.lang == "zh":
            pass

    def searchActionKeyword(self):
        action = 'init'
        if self.lang == "zh":
            if self.command.find("在哪") >= 0:
                self.action = 'whereis'
            elif self.command.find("放在") > 0:
                self.action = 'put'
        elif self.lang.lower() == 'en':
            self.command=self.command.lower()
            if self.command.find("where is") >= 0:
                self.action = 'whereis'
            elif self.command.find("i put") >= 0:
                self.action = 'put'
        else:
            self.action='unknown'
        return self.action

    def getVariable(self):
        paras = {}
        self.__prepare()
        if self.lang == "zh":
            if self.action == 'put':
                self.paras['item'] = self.command[self.command.find('把')+1:self.command.rfind("放在")]
                self.paras['posotion'] = self.command[self.command.find("放在")+2:]
            if self.action == 'whereis':
                self.paras['item'] = self.command[0: self.command.rfind("在哪")]

        if self.lang == "en":
            if self.action == 'put':
                first_preposition=len(self.command)-1
                #遍历方位及方位词，找到command中的第一个
                for key in self.prepositions[self.lang]:
                    for count in range(len(self.prepositions[self.lang][key])):
                        prep=self.prepositions[self.lang][key][count]
                        if self.command.find(prep)>0 and self.command.find(prep)<first_preposition:
                            self.localizer=key
                            self.preposition=prep
                            first_preposition=self.command.find(prep)
                self.paras['posotion'] = self.command[first_preposition:]
                self.paras['item'] = self.command[len('i put'):first_preposition-1]
            if self.action == 'whereis':
                self.paras['item'] = self.command[self.command.rfind("where is ")+len("where is "):]
        return self.paras

    def getCache(lang, deviceID):
        pass

    def __prepare(self):

        #删除语气助词
        if self.lang == "zh":
            mps=self.modal_particle[self.lang]
            for mp in mps:
                # print(mp)
                # command=command.rstrip(mp)
                # print(command)
                position=self.command.rfind(mp)
                if position>0 and (position + len(mp))==len(self.command):
                    self.command=self.command[0:position]
        pass



    def show(self):
        print("command：  ", self.command)
        print("language=", self.lang)
        print("action  ", self.action)

        show_all_dict(self.paras)
        print("________________________________")


def show_all_dict(dict_a):

    if isinstance(dict_a,dict) :
        for key in dict_a:
            temp_value = dict_a[key]
            print("%s : %s" %(key,temp_value))
            show_all_dict(temp_value) #遍历


def main(argv=None):
    if argv is None:
        argv = sys.argv

    p = Processor()
    deviceID = ""

    # command = '我把妈妈的钥匙放在桌子上了'
    # command = '妈妈的钥匙在哪里'
    # command = 'where is mummy\'s key'
    lang = 'en'

    command = 'I put mummy\'s key on the table'
    command = 'I put the spare car key in the first drawer of the study desk'
    p.process(lang, command, deviceID)
    p.show()

    lang = 'en'
    command = 'where is mummy\'s key'
    command = 'where is the spare car key'
    p = Processor()
    p.process(lang, command, deviceID)
    p.show()

    lang = 'zh'
    command = '我把备用车钥匙放在书房桌子的第一个抽屉里了'
    p = Processor()
    p.process(lang, command, deviceID)
    p.show()

    lang = 'zh'
    command = '备用车钥匙在哪里啊'
    p = Processor()
    p.process(lang, command, deviceID)
    p.show()



if __name__ == '__main__':
    sys.exit(main())

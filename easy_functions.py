"""
easy_functions是一个简单的模块，可以通过里面提供的方法来简化代码，这些方法往往很简单，但十分实用
本模块使用MIT协议
"""
import os
import socket
import tempfile
import logging

__all__ = [
    "start", "call", "find_file", "Vbs",
    "mode", "ban", "choice", "Cipher",
    "pause", "get_IP", "Log"
]

__version__ = "6.0.0"
__author__ = "Jerry0940"


def start(path):
    """
    打开一个文件或者文件夹
    :param path:文件路径
    """
    return os.system("start /b %s >nul" % path)


def call(path):
    """
    文件调用功能

    start命令和call命令的区别

    1.start命令在执行时会打开另一个窗口，而call命令不会

    2.call可以获取特定文件的返回值，例如调用.vbs文件，按下弹窗上的按钮后会返回数字

    3.此命令只能用于文件

    :param path:文件路径
    """
    return os.system("call %s >nul" % path)


def find_file(file, mode):
    """
    文件查找功能

    参数mode共有两种可填

    1."exist?"判断文件是否存在，返回布尔值

    2."import?"判断文件是否可以被导入，返回布尔值

    :param file:被检测的文件
    :param mode:查找模式
    """
    if not type(file) is str:
        raise SyntaxError(
            "需要输入字符串，而你输入的是%s" % type(file)
        )
    if mode == "exist?":
        return os.path.exists(file)
    elif mode == "import?":
        try:
            __import__(file)
        except ModuleNotFoundError:
            return False
        else:
            return True
    else:
        raise SyntaxError(
            '没有模式"%s"' % mode
        )


class Vbs:
    """显示弹窗"""

    def __init__(self):
        self.path = tempfile.gettempdir() + "\\easy_functionsMSG.vbs"

    def shownormal(self, title="easy_functions msgbox", message="模块easy_functions，简单，实用",
                   *chr13):
        """显示一个普通弹窗"""
        title = title.replace("\n", "").replace("\r", "")
        message = message.replace("\n", "").replace("\r", "")
        true = False
        chr = " "
        if len(chr13) != 0:
            for i in chr13:
                chr = chr + "+ chr(13) + " + '"' + i + '"'
            true = True
        with open(self.path, "w") as f:
            f.write("wsh.quit(msgbox(")
            f.write('"' + message + '"')
            if true:
                f.write(chr)
            f.write("," + "0" + ",")
            f.write('"' + title + '"')
            f.write("))")
        return call(self.path)

    def warningaskcancel(self, title="easy_functions msgbox", message="模块easy_functions，简单，实用",
                         *chr13):
        """显示警告图标并提供[确认]和[取消]"""
        title = title.replace("\n", "").replace("\r", "")
        message = message.replace("\n", "").replace("\r", "")
        true = False
        chr = " "
        if len(chr13) != 0:
            for i in chr13:
                chr = chr + "+ chr(13) + " + '"' + i + '"'
            true = True
        with open(self.path, "w") as f:
            f.write("wsh.quit(msgbox(")
            f.write('"' + message + '"')
            if true:
                f.write(chr)
            f.write("," + "49" + ",")
            f.write('"' + title + '"')
            f.write("))")
        return call(self.path)

    def erroraskcancel(self, title="easy_functions msgbox", message="模块easy_functions，简单，实用",
                       *chr13):
        """显示错误图标并提供[确认]和[取消]"""
        title = title.replace("\n", "").replace("\r", "")
        message = message.replace("\n", "").replace("\r", "")
        true = False
        chr = " "
        if len(chr13) != 0:
            for i in chr13:
                chr = chr + "+ chr(13) + " + '"' + i + '"'
            true = True
        with open(self.path, "w") as f:
            f.write("wsh.quit(msgbox(")
            f.write('"' + message + '"')
            if true:
                f.write(chr)
            f.write("," + "17" + ",")
            f.write('"' + title + '"')
            f.write("))")
        return call(self.path)

    def infoaskcancel(self, title="easy_functions msgbox", message="模块easy_functions，简单，实用",
                      *chr13):
        """显示信息图标并提供[确认]和[取消]"""
        title = title.replace("\n", "").replace("\r", "")
        message = message.replace("\n", "").replace("\r", "")
        true = False
        chr = " "
        if len(chr13) != 0:
            for i in chr13:
                chr = chr + "+ chr(13) + " + '"' + i + '"'
            true = True
        with open(self.path, "w") as f:
            f.write("wsh.quit(msgbox(")
            f.write('"' + message + '"')
            if true:
                f.write(chr)
            f.write("," + "65" + ",")
            f.write('"' + title + '"')
            f.write("))")
        return call(self.path)

    def warningaskyesno(self, title="easy_functions msgbox", message="模块easy_functions，简单，实用",
                        *chr13):
        """显示警告图标并提供[是]和[否]"""
        title = title.replace("\n", "").replace("\r", "")
        message = message.replace("\n", "").replace("\r", "")
        true = False
        chr = " "
        if len(chr13) != 0:
            for i in chr13:
                chr = chr + "+ chr(13) + " + '"' + i + '"'
            true = True
        with open(self.path, "w") as f:
            f.write("wsh.quit(msgbox(")
            f.write('"' + message + '"')
            if true:
                f.write(chr)
            f.write("," + "52" + ",")
            f.write('"' + title + '"')
            f.write("))")
        return call(self.path)

    def errorretry(self, title="easy_functions msgbox", message="模块easy_functions，简单，实用", *chr13):
        """显示错误图标并提供[重试]和[取消]"""
        title = title.replace("\n", "").replace("\r", "")
        message = message.replace("\n", "").replace("\r", "")
        true = False
        chr = " "
        if len(chr13) != 0:
            for i in chr13:
                chr = chr + "+ chr(13) + " + '"' + i + '"'
            true = True
        with open(self.path, "w") as f:
            f.write("wsh.quit(msgbox(")
            f.write('"' + message + '"')
            if true:
                f.write(chr)
            f.write("," + "21" + ",")
            f.write('"' + title + '"')
            f.write("))")
        return call(self.path)


def mode(cols, lines):
    """
    更改命令行窗口大小
    :param cols:宽
    :param lines:高
    """
    return os.system("mode con cols=" + str(cols) + " lines=" + str(lines))


def ban(words: str, WordsBlackList: list):
    """
    词语屏蔽功能
    :param words:被检测的文字
    :param WordsBlackList:文字黑名单，会将此列表中出现的词语全部替换为"*"
    """
    ban_list = []
    for i in range(len(words)):
        ban_list.append("*" * (i + 1))
    if type(WordsBlackList) is not list:
        raise SyntaxError(
            "词语黑名单需要传入列表类型"
        )
    for i in WordsBlackList:
        length = len(i) - 1
        words = words.replace(i, ban_list[length])
    return words


def choice(choose="YN", text="Y/N", default=False, timeout="10", *, hide=False):
    """
    按键选择功能

    返回值是根据用户选择的按键的排序生成的

    例如("YNC")这个用户可选按键列表中，共有3个按键：<Y>、<N>和<C>

    如果用户按下<Y>，返回值为1

    如果用户按下<N>，返回值为2

    如果用户按下<C>，返回值为3

    以此类推

    但在选择按键的过程中，如果用户使用<Ctrl+Break>或<Ctrl+C>键，该功能会返回0

    如果检测到错误状态，该功能会返回255

    如果用户按下的键不是有效的选择，电脑会发出警告响声（如果在音量合成器里启用了系统声音）

    :param choose:用户能够选择的按键
    :param text:显示的提示文字
    :param default:默认按键
    :param timeout:设置默认按键后的超时时间
    :param hide:是否隐藏可选按键列表
    :return:按键返回值
    """
    choice = "choice "
    choice = choice + " /C "
    for i in range(len(text)):
        if text[i] == " ":
            raise SyntaxError(
                "显示的文字中不能含有空格"
            )
    if hide:
        choice = choice + choose + " /N " + " /M " + text
    else:
        choice = choice + choose + " /M " + text
    if default:
        if default in choose:
            choice = choice + " /D " + default
            choice = choice + " /T " + timeout
        elif default not in choose:
            raise SyntaxError(
                "按键默认值不在设置的按键中"
            )
    return os.system(choice)


class Cipher:
    """加密或解密英文"""

    def __init__(self):
        self.WordsComparison = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
                                "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        self.NumberComparison = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п",
                                 "р", "с", "Я", "Ч", "Ш", "Щ", "ц", "ю", "э"]
        self.WordsCapsComparison = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
                                    "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        self.NumberCapsComparison = ["α", "β", "Φ", "ε", "Λ", "γ", "Ω", "σ", "υ", "δ", "Ъ", "×", "Γ", "Σ", "Ψ", "Υ",
                                     "ψ", "μ", "ω", "ξ", "U", "≌", "□", "○", "∷", "θ"]

    def lock(self, text: str):
        """
        加密英文
        :param text:被加密的英文
        """
        for i in range(26):
            text = text.replace(
                self.WordsComparison[i], self.NumberComparison[i])
        for i in range(26):
            text = text.replace(
                self.WordsCapsComparison[i], self.NumberCapsComparison[i])
        return text

    def unlock(self, text: str):
        """
        解密英文
        :param text:被解密的英文
        """
        for i in range(26):
            text = text.replace(
                self.NumberComparison[i], self.WordsComparison[i])
        for i in range(26):
            text = text.replace(
                self.NumberCapsComparison[i], self.WordsCapsComparison[i])
        return text


def pause(text="请按任意键继续..."):
    """
    暂停命令行
    :param text:暂停时显示的提示文字
    """
    print(text)
    os.system("pause >nul")
    return


def get_IP():
    """返回本机IP"""
    hostname = socket.gethostname()
    IP = socket.gethostbyname(hostname)
    return IP


class Log:
    """日志写入功能"""

    def __init__(self, logname, *, default_level=logging.INFO,
                 log_format="[%(asctime)s] [%(name)s/%(levelname)s]: %(message)s"):
        """
        :param logname:日志文件名称
        :param default_level:默认日志等级
        :param log_format:日志格式
        """
        logging.basicConfig(
            filename=logname, level=default_level, format=log_format)

    def write(self, words, level=logging.INFO, log_function=print):
        """
        写入日志
        :param words:写入的文字
        :param level:日志等级
        :param log_function:日志文字操作函数，日志的文字将会作为参数被传入到这个函数中
        """
        log_function(words)

        if level == "info" or logging.INFO:
            logging.info(words)
        elif level == "debug" or logging.DEBUG:
            logging.debug(words)
        elif level == "warning" or logging.WARNING:
            logging.warning(words)
        elif level == "error" or logging.ERROR:
            logging.error(words)
        else:
            logging.critical(words)

    def clear(self):
        """清空日志内容"""
        with open(self.logname, "w") as f:
            f.write("")

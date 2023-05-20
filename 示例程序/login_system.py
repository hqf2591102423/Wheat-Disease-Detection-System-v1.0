from _pyuis import login, register, retrieve_password, about, author_information, register_root, retrieve_pwd_root, \
    database_setup
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QLineEdit
from PyQt5 import QtGui
import sys
from _user.User import User
from _mysqlsdk import user as mysql_user_
from _mysqlsdk import login as Mysql_Login
from _mysqlsdk import administrator as mysql_administrator_
from _manage.administrator import Administrator


# login_ = Mysql_Login.Login()
# mysql_user = mysql_user_.User_Sdk(login_.conn)  # 实例化数据库user模块
# mysql_administrator = mysql_administrator_.Admin_Sdk(login_.conn)  # 实例化数据库administrator模块


class Login(QMainWindow, login.Ui_MainWindow):

    # 构造函数
    def __init__(self):
        super().__init__()  # 调用父类构造函数
        self.setupUi(self)  # 初始化窗体
        self.setWindowIcon(
            QtGui.QIcon('E:\\VisualStudioIDE\\Project\\Python\\IOWPexe_\\a_pictures\\logo.png'))  # 设置窗体图标
        self.setWindowTitle('登录系统')  # 设置窗体标题

        self.account = None  # 账号
        self.password = None  # 密码
        self.user = None
        self.admin = None
        self.database_setup = None

        self.pushButton_2.clicked.connect(self.login)  # 登录按钮绑定登录函数
        self.pushButton_2.setShortcut('Return')  # 设置登录按钮快捷键
        self.pushButton.clicked.connect(self.register)  # 注册按钮绑定注册函数
        self.pushButton_3.clicked.connect(self.retrieve_password)  # 忘记密码按钮绑定忘记密码函数
        self.actionjhhjhj.triggered.connect(self.about_us)  # 菜单栏绑定函数
        self.actiondd.triggered.connect(self.help)  # 菜单栏绑定函数
        self.action1.triggered.connect(self.database)  # 菜单栏绑定函数
        self.lineEdit_2.setEchoMode(2)  # 设置密码输入框为密码模式

        self.close_control()

        self.mysql_user = None
        self.mysql_administrator = None
        self.login_root = None

        self.Retrieve_password = None
        self.Register = None
        self.About = None

    def close_control(self):
        self.lineEdit.setEnabled(False)
        self.lineEdit_2.setEnabled(False)
        self.pushButton.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.pushButton_3.setEnabled(False)

    def open_control(self):
        self.lineEdit.setEnabled(True)
        self.lineEdit_2.setEnabled(True)
        self.pushButton.setEnabled(True)
        self.pushButton_2.setEnabled(True)
        self.pushButton_3.setEnabled(True)

    def login(self):
        self.account = self.lineEdit.text()
        self.password = self.lineEdit_2.text()
        if self.account == '' or self.password == '':
            QMessageBox.critical(self, '错误', '账号密码不能为空', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            return
        if self.radioButton_2.isChecked():
            user_info = self.mysql_user.find_user(self.account)
            if user_info != ():  # 判断是否存在该用户
                if self.account == user_info[0][0] and self.password == user_info[0][3]:
                    print(user_info[0][2], '登录成功')
                    user_setting = self.mysql_user.find_user_set_up(self.account)
                    background_color = user_setting[0][1]
                    transparency = user_setting[0][3]
                    font_color = user_setting[0][4]
                    font_family = user_setting[0][5]
                    font_size = user_setting[0][6]
                    self.user = User(self.account, self.login_root.conn)
                    self.user.setStyleSheet('font-family: %s;font-size:%spt;background-color: %s;color: %s' % (
                        font_family, font_size, background_color, font_color))
                    self.user.setFont(QtGui.QFont(font_family, 10))
                    self.user.setWindowIcon(
                        QtGui.QIcon('E:\\VisualStudioIDE\\Project\\Python\\IOWPexe_\\a_pictures\\logo.png'))
                    self.user.setWindowOpacity(transparency)
                    self.user.show()
                    self.close()
                    return
                else:
                    QMessageBox.critical(self, '错误', '请检查账号密码是否正确', QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.Yes)
                    print('登录失败')
            else:
                QMessageBox.critical(self, '错误', '该用户不存在', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                print('登录失败')
        else:
            # 管理员登录

            user_info = self.mysql_administrator.find_administrator(self.account)
            if user_info != ():  # 判断是否存在该用户
                if self.account == user_info[0][0] and self.password == user_info[0][3]:
                    print(user_info[0][2], '登录成功')
                    admin_setting = self.mysql_administrator.find_admin_set_up(self.account)
                    background_color = admin_setting[0][1]
                    transparency = admin_setting[0][3]
                    font_color = admin_setting[0][4]
                    font_family = admin_setting[0][5]
                    font_size = admin_setting[0][6]
                    self.admin = Administrator(self.account, self.login_root.conn)
                    self.admin.setStyleSheet('font-family: %s;font-size:%spt;background-color: %s;color: %s' % (
                        font_family, font_size, background_color, font_color))
                    self.admin.setWindowIcon(
                        QtGui.QIcon('E:\\VisualStudioIDE\\Project\\Python\\IOWPexe_\\a_pictures\\logo.png'))
                    self.admin.setWindowOpacity(transparency)
                    self.admin.show()
                    self.close()
                    return
                else:
                    QMessageBox.critical(self, '错误', '请检查账号密码是否正确', QMessageBox.Yes | QMessageBox.No,
                                         QMessageBox.Yes)
                    print('登录失败')
            else:
                QMessageBox.critical(self, '错误', '该用户不存在', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                print('登录失败')

    def register(self):
        if self.radioButton_2.isChecked():
            self.Register = Register(self.mysql_user)
            self.Register.show()
        else:
            self.Register = Register_Root(self.mysql_administrator)
            self.Register.show()

    def retrieve_password(self):
        if self.radioButton_2.isChecked():
            self.Retrieve_password = Retrieve(self.mysql_user)
            self.Retrieve_password.show()
        else:
            self.Retrieve_password = Retrieve_Root(self.mysql_administrator)
            self.Retrieve_password.show()

    def about_us(self):
        self.About = About()
        self.About.show()

    def help(self):
        QMessageBox.about(self, '帮助', '这是一个帮助窗体')

    def database(self):
        self.database_setup = Database_Setup()
        self.database_setup.show()
        self.database_setup.exec_()
        if self.database_setup.flag_open:
            self.open_control()
            try:
                self.login_root = Mysql_Login.Login(self.database_setup.database['host'],
                                                    self.database_setup.database['user'],
                                                    self.database_setup.database['password'],
                                                    self.database_setup.database['database'],
                                                    self.database_setup.database['port'])
                self.mysql_user = mysql_user_.User_Sdk(self.login_root.conn)
                self.mysql_administrator = mysql_administrator_.Admin_Sdk(self.login_root.conn)
            except Exception as err:
                QMessageBox.critical(self, '错误', str(err), QMessageBox.Yes)
                self.close_control()
        else:
            QMessageBox.critical(self, '错误', '数据库配置失败！', QMessageBox.Yes)


class Register(QMainWindow, register.Ui_Form):
    def __init__(self, mysql_user):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('../a_picture/logo.png'))  # 设置窗体图标
        self.setWindowTitle('注册系统')  # 设置窗体标题

        self.student_id = None
        self.phone_number = None
        self.name = None
        self.password = None
        self.mysql_user = mysql_user
        self.pushButton.clicked.connect(self.register)
        self.lineEdit_4.setEchoMode(2)  # 设置密码输入框为密码模式
        self.lineEdit_5.setEchoMode(2)  # 设置密码输入框为密码模式

    def register(self):
        if self.lineEdit.text() == "":
            QMessageBox.warning(self, '警告', '学号不能为空，请输入！')
        elif self.lineEdit_2.text() == "":
            QMessageBox.warning(self, '警告', '手机号不能为空，请输入！')
        elif self.lineEdit_3.text() == "":
            QMessageBox.warning(self, '警告', '姓名不能为空，请输入！')
        elif self.lineEdit_4.text() == "":
            QMessageBox.warning(self, '警告', '密码不能为空，请输入！')
        else:
            self.student_id = self.lineEdit.text()
            self.phone_number = self.lineEdit_2.text()
            self.name = self.lineEdit_3.text()
            self.password = self.lineEdit_4.text()
            if len(self.password) != 8:
                QMessageBox.warning(self, '警告', '密码长度不符合要求，需8位以上，请重新输入！')
            elif self.password != self.lineEdit_5.text():
                QMessageBox.warning(self, '警告', '两次输入的密码不一致，请重新输入！')
            else:
                if bool(len(self.mysql_user.find_user(self.student_id))):
                    QMessageBox.warning(self, '警告', '该账号已被注册，请重新输入！')
                    return
                else:
                    if self.mysql_user.save_user(self.student_id, self.phone_number, self.name, self.password):
                        self.mysql_user.init_oneself_data(self.student_id)
                        self.mysql_user.save_init_user_set_up(self.student_id)

                        QMessageBox.information(self, '提示', '注册成功！')
                        self.close()
                        return
                    else:
                        QMessageBox.warning(self, '警告', '注册失败，请重新输入！')
                        return


class Register_Root(QMainWindow, register_root.Ui_Form):
    def __init__(self, mysql_administrator):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('./a_picture/logo.png'))  # 设置窗体图标
        self.setWindowTitle('注册系统')  # 设置窗体标题

        self.student_id = None
        self.phone_number = None
        self.name = None
        self.password = None
        self.mysql_administrator = mysql_administrator
        self.pushButton.clicked.connect(self.register)
        self.lineEdit_4.setEchoMode(2)  # 设置密码输入框为密码模式
        self.lineEdit_5.setEchoMode(2)  # 设置密码输入框为密码模式

    def register(self):
        if self.lineEdit.text() == "":
            QMessageBox.warning(self, '警告', '内部号不能为空，请输入！')
        elif self.lineEdit_2.text() == "":
            QMessageBox.warning(self, '警告', '手机号不能为空，请输入！')
        elif self.lineEdit_3.text() == "":
            QMessageBox.warning(self, '警告', '姓名不能为空，请输入！')
        elif self.lineEdit_4.text() == "":
            QMessageBox.warning(self, '警告', '密码不能为空，请输入！')
        else:
            self.student_id = self.lineEdit.text()
            self.phone_number = self.lineEdit_2.text()
            self.name = self.lineEdit_3.text()
            self.password = self.lineEdit_4.text()
            if len(self.password) != 8:
                QMessageBox.warning(self, '警告', '密码长度不符合要求，需8位以上，请重新输入！')
            elif self.password != self.lineEdit_5.text():
                QMessageBox.warning(self, '警告', '两次输入的密码不一致，请重新输入！')
            else:
                if bool(len(self.mysql_administrator.find_administrator(self.student_id))):
                    QMessageBox.warning(self, '警告', '该账号已被注册，请重新输入！')
                    return
                else:
                    if self.mysql_administrator.save_administrator(self.student_id, self.phone_number, self.name,
                                                                   self.password):
                        self.mysql_administrator.save_oneself_data(self.student_id)
                        self.mysql_administrator.save_init_admin_set_up(self.student_id)
                        QMessageBox.information(self, '提示', '注册成功！')
                        self.close()
                        return
                    else:
                        QMessageBox.warning(self, '警告', '注册失败，请重新输入！')
                        return


class Retrieve(QMainWindow, retrieve_password.Ui_Form):
    def __init__(self, mysql_user):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(
            QtGui.QIcon('E:\\VisualStudioIDE\\Project\\Python\\IOWPexe_\\a_pictures\\logo.png'))  # 设置窗体图标
        self.setWindowTitle('找回密码')  # 设置窗体标题
        self.pushButton.clicked.connect(self.retrieve_password)
        self.account_number = None
        self.phone_number = None
        self.mysql_user = mysql_user

    def retrieve_password(self):
        self.account_number = self.lineEdit.text()
        self.phone_number = self.lineEdit_2.text()
        if self.account_number == '' or self.phone_number == '':
            QMessageBox.warning(self, '警告', '账号或手机号不能为空，请输入！')
            return
        user_info = self.mysql_user.find_user(self.account_number)
        if user_info is None:
            QMessageBox.warning(self, '警告', '未找到，请检查是否注册！')
            return
        else:
            if self.account_number == user_info[0][0] and self.phone_number == user_info[0][1]:
                QMessageBox.warning(self, '警告', '您的密码是' + user_info[0][3] + '，请牢记！')
                return
            else:
                QMessageBox.warning(self, '警告', '手机号错误，请重新输入！')
                return


class Retrieve_Root(QMainWindow, retrieve_pwd_root.Ui_Form):
    def __init__(self, mysql_administrator):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(
            QtGui.QIcon('E:\\VisualStudioIDE\\Project\\Python\\IOWPexe_\\a_pictures\\logo.png'))  # 设置窗体图标
        self.setWindowTitle('找回密码')  # 设置窗体标题
        self.pushButton.clicked.connect(self.retrieve_password)
        self.account_number = None
        self.phone_number = None
        self.mysql_administrator = mysql_administrator

    def retrieve_password(self):
        self.account_number = self.lineEdit.text()
        self.phone_number = self.lineEdit_2.text()
        if self.account_number == '' or self.phone_number == '':
            QMessageBox.warning(self, '警告', '内部号或手机号不能为空，请输入！')
            return
        user_info = self.mysql_administrator.find_administrator(self.account_number)
        if user_info is None:
            QMessageBox.warning(self, '警告', '未找到，请检查是否注册！')
            return
        else:
            if self.account_number == user_info[0][0] and self.phone_number == user_info[0][1]:
                QMessageBox.warning(self, '警告', '您的密码是' + user_info[0][3] + '，请牢记！')
                return
            else:
                QMessageBox.warning(self, '警告', '手机号错误，请重新输入！')
                return


class About(QMainWindow, about.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(
            QtGui.QIcon('E:\\VisualStudioIDE\\Project\\Python\\IOWPexe_\\a_pictures\\logo.png'))  # 设置窗体图标
        self.setWindowTitle('关于我们')  # 设置窗体标题
        self.wei = None
        self.huang = None
        self.chen = None

        self.pushButton_7.clicked.connect(self.Wei)
        self.pushButton_8.clicked.connect(self.Huang)
        self.pushButton_9.clicked.connect(self.Chen)

    def Wei(self):
        self.wei = About_Win()
        self.wei.setWindowTitle('魏凯杰')  # 设置窗体标题
        self.wei.lineEdit.setText('1248426034@qq.com')
        self.wei.lineEdit_2.setText('wLkLjX-forever')
        self.wei.lineEdit_3.setText('魏凯杰')
        self.wei.show()

    def Huang(self):
        self.huang = About_Win()
        self.huang.setWindowTitle('黄启帆')  # 设置窗体标题
        self.huang.lineEdit.setText('2591102423@qq.com')
        self.huang.lineEdit_2.setText('hqf15225918309')
        self.huang.lineEdit_3.setText('黄启帆')
        self.huang.show()

    def Chen(self):
        self.chen = About_Win()
        self.chen.setWindowTitle('陈朝辉')  # 设置窗体标题
        self.chen.lineEdit.setText('1461103631@qq.com')
        self.chen.lineEdit_2.setText('ChaoHui_Chen1024')
        self.chen.lineEdit_3.setText('陈朝辉')
        self.chen.show()


class About_Win(QMainWindow, author_information.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(
            QtGui.QIcon('E:\\VisualStudioIDE\\Project\\Python\\IOWPexe_\\a_pictures\\logo.png'))  # 设置窗体图标
        self.buttonBox.accepted.connect(self.close)


class Database_Setup(QDialog, database_setup.Ui_Dialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.flag_open = False
        self.database = dict()
        self.database['host'] = "localhost"
        self.database['port'] = 3306
        self.database['user'] = "root"
        self.database['password'] = "123456"
        self.database['database'] = "lowp"

        self.lineEdit.setText(self.database['user'])
        self.lineEdit_2.setText(self.database['password'])
        self.lineEdit_3.setText(self.database['host'])
        self.lineEdit_4.setText(str(self.database['port']))
        self.lineEdit_5.setText(self.database['database'])

        self.pushButton.clicked.connect(self.setup_button_clicked)

    def setup_button_clicked(self):

        for lineEdit in self.findChildren(QLineEdit):
            if lineEdit.text() == '':
                QMessageBox.warning(self, '警告', '数据库设置不能为空，请输入！')
                self.flag_open = False
                return

        self.database['user'] = self.lineEdit.text()
        self.database['password'] = self.lineEdit_2.text()
        self.database['host'] = self.lineEdit_3.text()
        self.database['port'] = int(self.lineEdit_4.text())
        self.database['database'] = self.lineEdit_5.text()
        QMessageBox.information(self, '提示', '数据库设置成功！')
        self.close()
        self.flag_open = True


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建 QApplication 实例对象
    window = Login()  # 实例化window用户窗体对象
    window.show()  # 显示窗口
    app.exit(app.exec_())  # 启动主事件循环

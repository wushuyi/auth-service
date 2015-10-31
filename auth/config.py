# -*- coding:utf-8 -*-

SECURITY_URL_PREFIX = '/auth'
SECURITY_REGISTERABLE = True
SECURITY_CONFIRMABLE = True
SECURITY_CHANGEABLE = True
SECURITY_RECOVERABLE = True

SECURITY_FORGOT_PASSWORD_TEMPLATE = 'forgot_password.html'
SECURITY_RESET_PASSWORD_TEMPLATE = 'reset_password.html'
SECURITY_LOGIN_USER_TEMPLATE = 'login_user.html'
SECURITY_REGISTER_USER_TEMPLATE = 'register_user.html'
SECURITY_SEND_CONFIRMATION_TEMPLATE = 'send_confirmation.html'
SECURITY_CHANGE_PASSWORD_TEMPLATE = 'change_password.html'

SECURITY_MSG_EMAIL_NOT_PROVIDED = ('电子邮箱不为空', 'error')

SECURITY_MSG_PASSWORD_NOT_PROVIDED = ('密码不为空', 'error')


# SECURITY_RECOVERABLE=True
# SECURITY_TRACKABLE=True
# SECURITY_PASSWORDLESS=True
# SECURITY_CHANGEABLE=True

SECURITY_POST_REGISTER_VIEW = '/auth/login'


# SECURITY_SEND_REGISTER_EMAIL = False


class MockConfig(dict):
    import os
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 25
    MAIL_USERNAME = os.environ['APP_MAIL_USERNAME']
    MAIL_PASSWORD = os.environ['APP_MAIL_PASSWORD']
    SECURITY_EMAIL_SENDER = MAIL_USERNAME


security_messages = {
    'UNAUTHORIZED': (
        '您没有权限查看该资源.', 'error'),
    'CONFIRM_REGISTRATION': (
        '谢谢.确认指示已被送往 %(email)s.', 'success'),
    'EMAIL_CONFIRMED': (
        '谢谢.您的邮箱已被证实.', 'success'),
    'ALREADY_CONFIRMED': (
        '您的电子邮件已确认.', 'info'),
    'INVALID_CONFIRMATION_TOKEN': (
        '无效的确认标记.', 'error'),
    'EMAIL_ALREADY_ASSOCIATED': (
        '%(email)s 已经与帐户相关联.', 'error'),
    'PASSWORD_MISMATCH': (
        '密码不匹配', 'error'),
    'RETYPE_PASSWORD_MISMATCH': (
        '密码不匹配', 'error'),
    'INVALID_REDIRECT': (
        '外域重定向被禁止', 'error'),
    'PASSWORD_RESET_REQUEST': (
        '重置您的密码已发送到 %(email)s.', 'info'),
    'PASSWORD_RESET_EXPIRED': (
        '你没有在重置密码 %(within)s. 新的指令已被送往 '
        ' %(email)s.', 'error'),
    'INVALID_RESET_PASSWORD_TOKEN': (
        '无效的重置密码令牌.', 'error'),
    'CONFIRMATION_REQUIRED': (
        '电子邮件需要确认.', 'error'),
    'CONFIRMATION_REQUEST': (
        '确认指示已被送往 %(email)s.', 'info'),
    'CONFIRMATION_EXPIRED': (
        '你没有在确认您的电子邮件 %(within)s. 新的指令来确认您的电子邮件 '
        '已发送到 %(email)s.', 'error'),
    'LOGIN_EXPIRED': (
        '您没有权限登录 %(within)s. 新的登录指令已被送往 '
        '%(email)s.', 'error'),
    'LOGIN_EMAIL_SENT': (
        '已发送登录的指示 %(email)s.', 'success'),
    'INVALID_LOGIN_TOKEN': (
        '无效登录令牌.', 'error'),
    'DISABLED_ACCOUNT': (
        '帐户被禁用.', 'error'),
    'EMAIL_NOT_PROVIDED': (
        '未提供电子邮件', 'error'),
    'INVALID_EMAIL_ADDRESS': (
        '无效的电子邮件地址', 'error'),
    'PASSWORD_NOT_PROVIDED': (
        '未提供密码', 'error'),
    'PASSWORD_NOT_SET': (
        '无密码为该用户设置', 'error'),
    'PASSWORD_INVALID_LENGTH': (
        '密码必须至少6个字符', 'error'),
    'USER_DOES_NOT_EXIST': (
        '指定用户不存在', 'error'),
    'INVALID_PASSWORD': (
        '无效密码', 'error'),
    'PASSWORDLESS_LOGIN_SUCCESSFUL': (
        '您已经成功登录.', 'success'),
    'PASSWORD_RESET': (
        '您成功重置您的密码,您已自动登录.',
        'success'),
    'PASSWORD_IS_THE_SAME': (
        '您的新密码必须与以前的密码不同.', 'error'),
    'PASSWORD_CHANGE': (
        '你成功地改变了你的密码.', 'success'),
    'LOGIN': (
        '请登录访问此页.', 'info'),
    'REFRESH': (
        '请验证访问此页面.', 'info'),
}

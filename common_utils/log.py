import os
import logging


# base_url = "D:\\m8sdp\\test_log"
base_url = "../test_log"


class Logger:
    def __init__(self, path=base_url + "/log/autotest.log", clevel=logging.DEBUG, Flevel=logging.INFO):
        # 判断log文件夹是否存在，不存在的话创建文件夹以及日志文件
        project_dir = os.listdir(base_url)
        dir_name = 'log'  # log文件夹
        if dir_name not in project_dir:
            create_path = base_url + '/' + dir_name
            os.makedirs(create_path)
        # 创建logger
        self.logger = logging.getLogger(path)
        self.logger.setLevel(logging.DEBUG)
        # 防止创建多个logger对象
        if not self.logger.handlers:
            # 设置日志格式
            fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
            # 设置CMD日志
            sh = logging.StreamHandler()
            sh.setFormatter(fmt)
            sh.setLevel(clevel)
            # 设置文件日志
            fh = logging.FileHandler(path, mode='a', encoding='utf-8')
            fh.setFormatter(fmt)
            fh.setLevel(Flevel)
            self.logger.addHandler(sh)
            self.logger.addHandler(fh)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def war(self, message):
        self.logger.warn(message)

    def error(self, message):
        self.logger.error(message)

    def cri(self, message):
        self.logger.critical(message)

import logging,time,os
class Logger(object):
    def __init__(self,logger):
        '''
            指定保存日志的文件路径，日志级别，以及调用文件
            将日志存入到指定的文件中
        '''
        #创建logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        #创建handle
        rq = time.strftime('%Y-%m-%d_%H.%M')
        file_path = os.path.dirname(os.getcwd()) + '/framework_demo/logs/'
        file_name = file_path + rq + '.log'
        fn = logging.FileHandler(file_name)
        #写入file的logging级别
        fn.setLevel(logging.DEBUG)
        #定义输出格式
        formater = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
        fn.setFormatter(formater)
        #给logger添加handle
        self.logger.addHandler(fn)
        #创建handle输出到控制台
        kzt = logging.StreamHandler()
        kzt.setLevel(logging.DEBUG)
        kzt.setFormatter(formater)
        self.logger.addHandler(kzt)
    def getlog(self):
        return self.logger
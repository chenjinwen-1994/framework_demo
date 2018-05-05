import BeautifulReport,unittest,os,time
from framework.email import Email
#测试报告路径
# 在pycharm中运行此行，但在使用jenkins构建项目时会报目录错误
# report_path = os.path.dirname(os.getcwd())+'/framework_demo/test_report/'
report_path = os.path.dirname(os.getcwd())+'/test_baidu/'
now_time = time.strftime('%Y-%m-%d_%H.%M')
report_name = now_time + '测试报告.html'
#跑用例
test_dir = 'D:/PYTEST/framework_demo/testsuits'
suite = unittest.defaultTestLoader.discover(test_dir)
if __name__=='__main__':
    #生成测试报告
    result = BeautifulReport.BeautifulReport(suite)
    result.report(filename=report_name,
                  description='百度测试报告',
                  log_path=report_path)
    #取最新报告
    new_email = Email(email='.')
    new_report = new_email.new_file(report_path)
    print(new_report)
    #发送邮件
    new_email.send_email(new_report)


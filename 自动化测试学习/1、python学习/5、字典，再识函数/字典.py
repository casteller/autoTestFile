filedir = r"C:\Users\Administrator\PycharmProjects\软件自动化测试\自动化测试学习\1、python学习\5、字典，再识函数\001.txt"
def putInfoToDict(fileName):
    with open(fileName) as f:
        setdict = {}
        lines = f.read().splitlines()
        for line in lines:
            #将括号替换为空,去空格
            line = line.replace("(","").replace(")","").replace("'","").strip()
            parts = line.split(",")
            #分别记录学生id，课程id，签到时间
            studentid = parts[2].strip().replace(";","")
            lessonsid = int(parts[1].strip())
            checkintime = parts[0].strip()
            toAdd = {'lessonid': lessonsid, 'checkintime': checkintime}
            if studentid not in setdict:
                setdict[studentid] = []
            setdict[studentid].append(toAdd)
    return setdict
studentCheckInfo = putInfoToDict(filedir)
#print(studentCheckInfo)
# 直接print打印显示为一行，不知道怎么输出，参考了答案，百度了下pprint模块.pprint方法是一种标准、格式化输出方式
import pprint
pprint.pprint(studentCheckInfo)

from course_lib import *

def case02(name, desc, idx):
    before_courses = list_course()
    retObj = add_course(name, desc, idx)
    if retObj=={"retcode": 2,"reason": "同名课程存在"}:
        print('pass')
    after_courses = list_course()

    if before_courses ==after_courses:
        print('pass')

    before=[]
    for ret in before_courses:
        if ret['name']==name:
            before.append(ret)

    after=[]
    for ret in after_courses:
        if ret['name']==name:
            after.append(ret)

    if before[0]['id'] == after[0]['id']:
        print('同名课程添加失败')
    else:
        print('同名课程添加成功')

case02('java','webdesc',3)
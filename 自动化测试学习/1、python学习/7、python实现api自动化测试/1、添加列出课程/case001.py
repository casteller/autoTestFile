
import pprint
import time

from task06.course_lib import *

def case01(name,desc,idx):
    before_courses=list_course()

    retObj=add_course(name,desc,idx)

    if retObj['retcode']==0:
        print('pass')

    after_courses=list_course()

    one=[]
    for courses in after_courses:
        if courses not in before_courses:
            one.append(courses)
            break
    print(one)

    cour=one[0]
    assert cour['name'] == name
    assert cour['desc'] == desc
    assert cour['display_idx'] == idx

    print('==========pass===========')
#时间戳
timestamp=time.time()

case01('web测试%s'%timestamp,'web测试描述',2)




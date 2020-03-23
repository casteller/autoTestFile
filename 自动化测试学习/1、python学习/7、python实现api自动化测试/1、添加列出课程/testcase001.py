from webapi import *
import time
def testcase1(name,desc,idx):
    before_courses=list_course()

    retObj = add_course(name, desc, idx)

    if retObj['retcode'] == 0:
        print('pass')

    after_courses = list_course()

    one = []
    for courses in after_courses:
        if courses not in before_courses:
            one.append(courses)
            break
    print(one)

    cour = one[0]
    assert cour['name'] == name
    assert cour['desc'] == desc
    assert cour['display_idx'] == idx

    print('-----测试通过-----')
t = time.time()
testcase1("python"+str(t),"一种编程语言",1)
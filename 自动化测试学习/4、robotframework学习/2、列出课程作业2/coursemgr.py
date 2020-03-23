import requests
def listCourse():
    payload = {'action': 'list_course', 'pagenum': 1, 'pagesize': 20}
    resp = requests.get("http://localhost/api/mgr/sq_mgr/", params=payload)
    retlists = resp.json()['retlist']
    course_name = []
    for retlist in retlists:
        name = retlist['name']
        course_name.append(name)
    return course_name

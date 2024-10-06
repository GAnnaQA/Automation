from YouGileApi import YouGile


def test_get_projects_list():
    You_gile = YouGile('https://ru.yougile.com')
    res = You_gile.get_project_list()
    status = res.status_code
    json = res.json()
    count = json['paging']['count']
    assert status == 200
    assert count > 0


def test_add_projects():
    You_gile = YouGile('https://ru.yougile.com')
    res_before = You_gile.get_project_list()
    json = res_before.json()
    print(json)
    count_before = json['paging']['count']
    res_add = You_gile.add_project('Mos.ru')
    status = res_add.status_code
    json_add = res_add.json()
    res_after = You_gile.get_project_list()
    json_after = res_after.json()
    count_after = json_after['paging']['count']
    assert status == 201
    assert count_after-count_before == 1
    assert json_add['id'] is not None


def test_get_project_with_id():
    You_gile = YouGile('https://ru.yougile.com')
    new_title = 'SkyPro'
    new_project = You_gile.add_project(new_title)
    json = new_project.json()
    new_id = json['id']
    desired_project = You_gile.get_project_with_id(new_id)
    status = desired_project.status_code
    json = desired_project.json()
    assert status == 200
    assert json['id'] == new_id
    assert json['title'] == new_title


def test_change_project_title():
    You_gile = YouGile('https://ru.yougile.com')
    add_title = 'SkyPro'
    new_project = You_gile.add_project(add_title)
    json = new_project.json()
    new_id = json['id']
    new_title = 'Python'
    modified_project = You_gile.change_project_title(new_id, new_title)
    modified_project_status = modified_project.status_code
    modified_project_json = modified_project.json()
    desired_project = You_gile.get_project_with_id(new_id)
    desired_project_json = desired_project.json()
    assert modified_project_status == 200
    assert modified_project_json['id'] == new_id
    assert desired_project_json['title'] == new_title

import requests


class YouGile():

    def __init__(self, url):
        self.url = url

    def get_project_list(self, token='Bearer v2la61zn8A2lU+pp3GAeLVvHr8TRE08olrA-2iXh9Cx7+9hvDKIfMIkW12-geMEr'):
        my_headers = {}
        my_headers["Authorization"] = token
        result = requests.get(self.url + '/api-v2/projects', headers=my_headers)
        return result

    def add_project(self, title, user_id='b3603ac0-a2f2-405f-8055-06b6f9c4f514', user_role='admin', token='Bearer v2la61zn8A2lU+pp3GAeLVvHr8TRE08olrA-2iXh9Cx7+9hvDKIfMIkW12-geMEr'):
        my_headers = {}
        my_headers["Authorization"] = token
        body = {
            "title": title,
            "users":
            {user_id: user_role}
        }
        result = requests.post(self.url + '/api-v2/projects', json=body, headers=my_headers)
        return result

    def get_project_with_id(self, id, token='Bearer v2la61zn8A2lU+pp3GAeLVvHr8TRE08olrA-2iXh9Cx7+9hvDKIfMIkW12-geMEr'):
        my_headers = {}
        my_headers["Authorization"] = token
        result = requests.get(self.url + '/api-v2/projects/' + id, headers=my_headers)
        return result

    def change_project_title(self, id, new_title, token='Bearer v2la61zn8A2lU+pp3GAeLVvHr8TRE08olrA-2iXh9Cx7+9hvDKIfMIkW12-geMEr'):
        my_headers = {}
        my_headers["Authorization"] = token
        body = {'title': new_title}
        result = requests.put(self.url + '/api-v2/projects/' + id, json=body, headers=my_headers)
        return result

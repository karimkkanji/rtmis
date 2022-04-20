from django.core import signing
from django.core.management import call_command
from django.test import TestCase

from api.v1.v1_profile.constants import UserRoleTypes
from api.v1.v1_users.models import SystemUser


class UserInvitationTestCase(TestCase):

    def test_user_list(self):
        call_command("administration_seeder", "--test")
        user_payload = {"email": "admin@rtmis.com", "password": "Test105*"}
        user_response = self.client.post('/api/v1/login',
                                         user_payload,
                                         content_type='application/json')
        user = user_response.json()
        token = user.get('token')
        response = self.client.get(
            "/api/v1/users?administration=1&role=1", follow=True,
            **{'HTTP_AUTHORIZATION': f'Bearer {token}'})
        users = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(users['data'][0]['first_name'], 'Admin')
        self.assertEqual(users['data'][0]['last_name'], 'RTMIS')
        self.assertEqual(users['data'][0]['email'], 'admin@rtmis.com')
        self.assertEqual(users['data'][0]['administration'],
                         {'id': 1, 'name': 'Indonesia', 'level': 0})
        self.assertEqual(users['data'][0]['role'],
                         {'id': 1, 'value': 'Super Admin'})
        call_command("fake_user_seeder", "-r", 100)
        response = self.client.get(
            "/api/v1/users?page=3", follow=True,
            **{'HTTP_AUTHORIZATION': f'Bearer {token}'})
        users = response.json()
        self.assertEqual(len(users['data']), 10)
        self.assertEqual(
            ['id', 'first_name', 'last_name', 'email', 'administration',
             'role', 'phone_number', 'designation', 'invite'],
            list(users['data'][0]))
        response = self.client.get(
            "/api/v1/users?pending=true",
            follow=True,
            **{'HTTP_AUTHORIZATION': f'Bearer {token}'})

        self.assertGreater(len(response.json().get('data')), 0)
        self.assertEqual(response.status_code, 200)

    def test_add_edit_user(self):
        call_command("administration_seeder", "--test")
        user_payload = {"email": "admin@rtmis.com", "password": "Test105*"}
        user_response = self.client.post('/api/v1/login',
                                         user_payload,
                                         content_type='application/json')
        user = user_response.json()
        token = user.get('token')
        payload = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john@example.com",
            "administration": 2,
        }
        header = {
            'HTTP_AUTHORIZATION': f'Bearer {token}'
        }
        add_response = self.client.post("/api/v1/user",
                                        payload,
                                        content_type='application/json',
                                        **header)
        self.assertEqual(add_response.status_code, 400)
        payload["role"] = 2
        add_response = self.client.post("/api/v1/user",
                                        payload,
                                        content_type='application/json',
                                        **header)

        self.assertEqual(add_response.status_code, 200)
        self.assertEqual(add_response.json(),
                         {'message': 'User added successfully'})

        edit_payload = {
            "first_name": "Joe",
            "last_name": "Doe",
            "email": "john@example.com",
            "administration": 2,
            "role": 6
        }
        header = {
            'HTTP_AUTHORIZATION': f'Bearer {token}'
        }

        list_response = self.client.get("/api/v1/users?pending=true",
                                        follow=True,
                                        **header)
        users = list_response.json()
        fl = list(
            filter(lambda x: x['email'] == 'john@example.com', users['data']))

        add_response = self.client.put(
            "/api/v1/user/{0}".format(fl[0]['id']),
            edit_payload,
            content_type='application/json',
            **header)
        self.assertEqual(add_response.status_code, 400)
        edit_payload["role"] = 2
        add_response = self.client.put(
            "/api/v1/user/{0}".format(fl[0]['id']),
            edit_payload,
            content_type='application/json',
            **header)
        self.assertEqual(add_response.status_code, 200)
        self.assertEqual(add_response.json(),
                         {'message': 'User updated successfully'})
        get_response = self.client.get(
            "/api/v1/user/{0}".format(fl[0]['id']),
            content_type='application/json',
            **header)
        self.assertEqual(get_response.status_code, 200)
        self.assertEqual(
            ['first_name', 'last_name', 'email', 'administration', 'role',
             'phone_number', 'designation', 'forms', 'pending_approval',
             'data'], list(get_response.json()))

    def test_get_user_profile(self):
        call_command("administration_seeder", "--test")
        user_payload = {"email": "admin@rtmis.com", "password": "Test105*"}
        user_response = self.client.post('/api/v1/login',
                                         user_payload,
                                         content_type='application/json')
        user = user_response.json()
        token = user.get('token')
        header = {
            'HTTP_AUTHORIZATION': f'Bearer {token}'
        }
        response = self.client.get("/api/v1/profile",
                                   content_type='application/json',
                                   **header)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            ['email', 'name', 'administration', 'role', 'phone_number',
             'designation'], list(response.json().keys()))

    def test_get_user_roles(self):
        response = self.client.get("/api/v1/user/roles",
                                   content_type='application/json', )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(4, len(response.json()))
        self.assertEqual(['id', 'value'], list(response.json()[0].keys()))

    #
    def test_verify_invite(self):
        call_command("administration_seeder", "--test")
        user_payload = {"email": "admin@rtmis.com", "password": "Test105*"}
        self.client.post('/api/v1/login',
                         user_payload,
                         content_type='application/json')
        user = SystemUser.objects.first()
        invite_payload = 'dummy-token'
        invite_response = self.client.get(
            '/api/v1/invitation/{0}'.format(invite_payload),
            content_type='application/json')
        self.assertEqual(invite_response.status_code, 400)

        invite_payload = signing.dumps(user.pk)
        invite_response = self.client.get(
            '/api/v1/invitation/{0}'.format(invite_payload),
            content_type='application/json')
        self.assertEqual(invite_response.json(), {'name': "Admin RTMIS"})
        self.assertEqual(invite_response.status_code, 200)

    def test_set_user_password(self):
        call_command("administration_seeder", "--test")
        user_payload = {"email": "admin@rtmis.com", "password": "Test105*"}
        self.client.post('/api/v1/login',
                         user_payload,
                         content_type='application/json')
        user = SystemUser.objects.first()
        password_payload = {'invite': 'dummy-token', 'password': 'Test105*',
                            'confirm_password': 'Test105*'}
        invite_response = self.client.put('/api/v1/user/set-password',
                                          password_payload,
                                          content_type='application/json')
        self.assertEqual(invite_response.status_code, 400)
        password_payload = {'invite': signing.dumps(user.pk),
                            'password': 'Test105*',
                            'confirm_password': 'Test105*'}
        invite_response = self.client.put('/api/v1/user/set-password',
                                          password_payload,
                                          content_type='application/json')
        self.assertEqual(invite_response.status_code, 200)

    def test_list_administration(self):
        call_command("administration_seeder", "--test")
        administration = self.client.get('/api/v1/administration/1',
                                         content_type='application/json')
        self.assertEqual(administration.status_code, 200)

        response = self.client.get('/api/v1/levels',
                                   content_type='application/json')
        levels = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 4)
        self.assertEqual(list(levels[0]), ['id', 'name', 'level'])

    def test_config_js(self):
        response = self.client.get('/api/v1/config.js',
                                   content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_email_template(self):
        # test get user_register template
        response = self.client.get(
            '/api/v1/email_template?type=user_register',
            content_type='application/json')
        self.assertEqual(response.status_code, 200)
        # test get user_approval template
        response = self.client.get(
            '/api/v1/email_template?type=user_approval',
            content_type='application/json')
        self.assertEqual(response.status_code, 200)
        # test get data_approval template
        response = self.client.get(
            '/api/v1/email_template?type=data_approval',
            content_type='application/json')
        self.assertEqual(response.status_code, 200)
        # test get data_rejection template
        response = self.client.get(
            '/api/v1/email_template?type=data_rejection',
            content_type='application/json')
        self.assertEqual(response.status_code, 200)
        # test get batch_approval template
        response = self.client.get(
            '/api/v1/email_template?type=batch_approval',
            content_type='application/json')
        self.assertEqual(response.status_code, 200)
        # test get batch_rejection template
        response = self.client.get(
            '/api/v1/email_template?type=batch_rejection',
            content_type='application/json')
        self.assertEqual(response.status_code, 200)
        # test get pending_approval template
        response = self.client.get(
            '/api/v1/email_template?type=pending_approval',
            content_type='application/json')
        self.assertEqual(response.status_code, 200)
        # test get upload_error template
        response = self.client.get(
            '/api/v1/email_template?type=upload_error',
            content_type='application/json')
        self.assertEqual(response.status_code, 200)
        # test get new_request template
        response = self.client.get(
            '/api/v1/email_template?type=new_request',
            content_type='application/json')
        self.assertEqual(response.status_code, 200)
        # test get unchanged_data template
        response = self.client.get(
            '/api/v1/email_template?type=unchanged_data',
            content_type='application/json')
        self.assertEqual(response.status_code, 200)
        # not send type
        response = self.client.get('/api/v1/email_template',
                                   content_type='application/json')
        self.assertEqual(response.status_code, 400)
        # test invalid type
        response = self.client.get('/api/v1/email_template?type=registration',
                                   content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_delete_user(self):
        call_command("administration_seeder", "--test")
        user_payload = {"email": "admin@rtmis.com", "password": "Test105*"}
        user_response = self.client.post('/api/v1/login',
                                         user_payload,
                                         content_type='application/json')
        user = user_response.json()
        token = user.get('token')
        header = {
            'HTTP_AUTHORIZATION': f'Bearer {token}'
        }
        call_command("fake_user_seeder")
        call_command("fake_approver_seeder")
        u = SystemUser.objects.filter(
            user_access__role__in=[UserRoleTypes.approver,
                                   UserRoleTypes.user]).first()
        response = self.client.delete('/api/v1/user/{0}'.format(u.id),
                                      content_type='application/json',
                                      **header)
        self.assertEqual(response.status_code, 204)

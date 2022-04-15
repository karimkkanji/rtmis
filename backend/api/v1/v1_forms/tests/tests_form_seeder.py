from io import StringIO

from django.core.management import call_command
from api.v1.v1_profile.models import Administration, Levels
from django.test import TestCase

from api.v1.v1_forms.models import Forms


def seed_administration_test():
    level = Levels(name="country", level=1)
    level.save()
    administration = Administration(id=1,
                                    name="Indonesia",
                                    parent=None,
                                    level=level)
    administration.save()
    administration = Administration(id=2,
                                    name="Jakarta",
                                    parent=administration,
                                    level=level)
    administration.save()


class FormSeederTestCase(TestCase):
    def call_command(self, *args, **kwargs):
        out = StringIO()
        call_command(
            "form_seeder",
            *args,
            stdout=out,
            stderr=StringIO(),
            **kwargs,
        )
        return out.getvalue()

    def test_call_command(self):

        self.maxDiff = None
        seed_administration_test()
        output = self.call_command()
        json_forms = [
            "Health Facilities",
            "Household",
            "CLTS",
            "WASH in School",
            "Water System",
        ]
        output = list(filter(lambda x: len(x), output.split("\n")))
        forms = Forms.objects.all()
        form_names = [form.name for form in forms]
        form_ids = [form.id for form in forms]
        self.assertEqual(forms.count(), 5)
        for json_form in json_forms:
            self.assertIn(f"Form Created | {json_form}", output)
            self.assertIn(json_form, form_names)

        user = {"email": "admin@rtmis.com", "password": "Test105*"}
        user = self.client.post('/api/v1/login',
                                user,
                                content_type='application/json')
        user = user.json()
        token = user.get("token")
        self.assertTrue(token)
        for id in form_ids:
            response = self.client.get(
                f"/api/v1/form/web/{id}",
                follow=True,
                content_type='application/json',
                **{'HTTP_AUTHORIZATION': f'Bearer {token}'})
            self.assertEqual(200, response.status_code)
        response = self.client.get("/api/v1/form/web/952774024",
                                   follow=True,
                                   content_type='application/json',
                                   **{'HTTP_AUTHORIZATION': f'Bearer {token}'})
        self.assertEqual(200, response.status_code)
        response = response.json()
        self.assertEqual("Water Quality",
                         response["question_group"][0]["name"])
        self.assertEqual(968554020,
                         response["question_group"][0]["question"][0]['id'])
        self.assertEqual('Can we conduct a water quality test?',
                         response["question_group"][0]["question"][0]['name'])
        self.assertEqual(
            ['id', 'name'],
            list(response["question_group"][0]["question"][0]['option'][0]))
        self.assertEqual(False,
                         response["question_group"][0]["question"][0]['meta'])
        self.assertEqual(996974044,
                         response["question_group"][0]["question"][1]['id'])
        self.assertEqual('If yes, can we conduct a test on salinity (taste)?',
                         response["question_group"][0]["question"][1]['name'])
        self.assertEqual(
            ['id', 'name'],
            list(response["question_group"][0]["question"][1]['option'][0]))
        self.assertEqual(False,
                         response["question_group"][0]["question"][1]['meta'])

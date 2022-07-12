# Generated by Django 4.0.4 on 2022-07-11 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('v1_forms', '0014_materialized_viewjmpdata'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ViewJmpData',
        ),
        migrations.RunSQL(
            """
            DROP MATERIALIZED VIEW view_jmp_data;
            DROP MATERIALIZED VIEW view_jmp_criteria;
            CREATE MATERIALIZED VIEW view_jmp_criteria as
                SELECT row_number() OVER (PARTITION BY true::boolean) AS id,
                    qa.form_id,
                    split_part(qa.name, '|'::text, 1) AS name,
                    split_part(qa.name, '|'::text, 2) AS level,
                    split_part(qa.name, '|'::text, 3)::int AS score,
                    jsonb_agg(qa.option) AS criteria
                 FROM (
                     SELECT
                         q.name,
                         qs.form_id,
                         q.question_id,
                         concat(q.question_id, '||', lower(
                         jsonb_array_elements_text(q.options))) AS
                         option
                      FROM question_attribute q
                      LEFT JOIN question qs ON q.question_id = qs.id
                      WHERE q.attribute = 4) qa
                GROUP BY qa.form_id, qa.name, qa.question_id
                ORDER BY qa.name;
            CREATE MATERIALIZED VIEW view_jmp_data as
            SELECT row_number() OVER (PARTITION BY true::boolean) AS id,
                    d.data_id,
                    a.path,
                    d.form_id,
                    c.name,
                    c.level,
                    c.score::int,
                    COUNT(*) as matches
            FROM view_data_options D
            LEFT JOIN view_jmp_criteria C
                ON c.form_id = d.form_id
            LEFT join data dt
                ON dt.id = d.data_id
            LEFT JOIN administrator A
                ON dt.administration_id = a.id
            WHERE d.options ?|
                TRANSLATE(c.criteria::jsonb::text,'[]','{}')::text[]
            GROUP BY
                d.data_id, a.path, d.form_id,
                c.name, c.level, c.score
            ORDER BY d.data_id,
                d.form_id, c.name, c.level;
            """,
            """
            DROP MATERIALIZED VIEW view_jmp_data;
            DROP MATERIALIZED VIEW view_jmp_criteria;
            CREATE MATERIALIZED VIEW view_jmp_criteria as
                SELECT row_number() OVER (PARTITION BY true::boolean) AS id,
                    qa.form_id,
                    split_part(qa.name, '|'::text, 1) AS name,
                    split_part(qa.name, '|'::text, 2) AS level,
                    jsonb_agg(qa.option) AS criteria
                 FROM (
                     SELECT
                         q.name,
                         qs.form_id,
                         q.question_id,
                         concat(q.question_id, '||', lower(
                         jsonb_array_elements_text(q.options))) AS
                         option
                      FROM question_attribute q
                      LEFT JOIN question qs ON q.question_id = qs.id
                      WHERE q.attribute = 4) qa
                GROUP BY qa.form_id, qa.name, qa.question_id
                ORDER BY qa.name;
            CREATE MATERIALIZED VIEW view_jmp_data as
            SELECT row_number() OVER (PARTITION BY true::boolean) AS id,
                    d.data_id,
                    a.path,
                    d.form_id,
                    c.name,
                    c.level,
                    COUNT(*) as matches
            FROM view_data_options D
            LEFT JOIN view_jmp_criteria C
                ON c.form_id = d.form_id
            LEFT join data dt
                ON dt.id = d.data_id
            LEFT JOIN administrator A
                ON dt.administration_id = a.id
            WHERE d.options ?|
                TRANSLATE(c.criteria::jsonb::text,'[]','{}')::text[]
            GROUP BY
                d.data_id, a.path, d.form_id,
                c.name, c.level
            ORDER BY d.data_id,
                d.form_id, c.name, c.level;
            """
        )
    ]
# Generated by Django 4.2.16 on 2024-10-04 22:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0003_course_summary_es_course_summary_fr_course_title_es_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="code",
            field=models.CharField(default="testcode101", max_length=200, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="course",
            name="credit",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="course",
            name="is_elective",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="course",
            name="level",
            field=models.CharField(
                choices=[("Bachelor", "Bachelor Degree"), ("Master", "Master Degree")],
                default="Bachelor",
                max_length=25,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="course",
            name="summary",
            field=models.TextField(blank=True, default="Test summary", max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="course",
            name="title",
            field=models.CharField(default="Test title", max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="course",
            name="year",
            field=models.IntegerField(
                choices=[(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5"), (6, "6")],
                default=1,
            ),
        ),
        migrations.AlterField(
            model_name="program",
            name="summary",
            field=models.TextField(blank=True, default="Test summary"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="upload",
            name="updated_date",
            field=models.DateTimeField(
                auto_now=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="upload",
            name="upload_time",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="uploadvideo",
            name="summary",
            field=models.TextField(blank=True, default="test"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="uploadvideo",
            name="timestamp",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
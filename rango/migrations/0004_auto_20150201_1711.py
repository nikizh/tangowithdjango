# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models, migrations
import uuid

def uuid_slug(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Category = apps.get_model("rango", "Category")
    for category in Category.objects.all():
        category.slug = str(uuid.uuid4())
        category.save()


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0003_category_slug'),
    ]

    operations = [
        migrations.RunPython(uuid_slug),
    ]

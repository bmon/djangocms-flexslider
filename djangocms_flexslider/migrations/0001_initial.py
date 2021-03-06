# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-15 15:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import djangocms_text_ckeditor.fields
import filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0015_auto_20160421_0000'),
        ('filer', '0004_auto_20160328_1434'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('width', models.IntegerField(blank=True, help_text='in pixels', null=True, verbose_name='width')),
                ('height', models.IntegerField(blank=True, help_text='in pixels', null=True, verbose_name='height')),
                ('caption', djangocms_text_ckeditor.fields.HTMLField(blank=True, help_text='Optional caption that is displayed with the image', null=True, verbose_name='caption')),
                ('link_url', models.URLField(blank=True, help_text='If a url is specified, this slide will act as a hyperlink to that url.', max_length=500, null=True, verbose_name='link url')),
                ('image', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.CASCADE, to='filer.Image')),
                ('page_url', models.ForeignKey(blank=True, help_text='If a page is specified, this slide will act as a hyperlink to that page.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms.Page', verbose_name='page url')),
            ],
            options={
                'verbose_name': 'Slide',
                'verbose_name_plural': 'Slides',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('slider_id', models.CharField(default='slider', help_text='The ID attribute used in the HTML', max_length=100, verbose_name='slider ID')),
                ('slider_config', models.TextField(blank=True, help_text='The JSON object passed to Flexslider. For more info <a target="_blank" href="https://github.com/woothemes/FlexSlider/wiki/FlexSlider-Properties">click here</a>', null=True, verbose_name='slider config')),
                ('carousel', models.BooleanField(default=False, help_text='Add a thumbnail carousel to the slider', verbose_name='carousel')),
                ('carousel_id', models.CharField(default='carousel', help_text='The ID attribute used in the HTML', max_length=100, verbose_name='slider ID')),
                ('carousel_config', models.TextField(blank=True, help_text='The JSON object passed to Flexslider for the carousel. For more info <a target="_blank" href="https://github.com/woothemes/FlexSlider/wiki/FlexSlider-Properties">click here</a>', null=True, verbose_name='carousel config')),
            ],
            options={
                'verbose_name': 'Slider',
                'verbose_name_plural': 'Sliders',
            },
            bases=('cms.cmsplugin',),
        ),
    ]

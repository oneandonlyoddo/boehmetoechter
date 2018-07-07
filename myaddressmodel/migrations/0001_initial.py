# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Country'
        db.create_table(u'myaddressmodel_country', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'myaddressmodel', ['Country'])

        # Adding model 'Address'
        db.create_table(u'myaddressmodel_address', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('vorname', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('nachname', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('nr', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('stadt', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'myaddressmodel', ['Address'])


    def backwards(self, orm):
        # Deleting model 'Country'
        db.delete_table(u'myaddressmodel_country')

        # Deleting model 'Address'
        db.delete_table(u'myaddressmodel_address')


    models = {
        u'myaddressmodel.address': {
            'Meta': {'object_name': 'Address'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nachname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nr': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'stadt': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'vorname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'myaddressmodel.country': {
            'Meta': {'object_name': 'Country'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['myaddressmodel']
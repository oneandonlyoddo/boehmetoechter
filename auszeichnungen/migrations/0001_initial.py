# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Veranstalter'
        db.create_table(u'auszeichnungen_veranstalter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=2000)),
        ))
        db.send_create_signal(u'auszeichnungen', ['Veranstalter'])

        # Adding model 'Auszeichnung'
        db.create_table(u'auszeichnungen_auszeichnung', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('jahr', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('titel', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('veranstalter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auszeichnungen.Veranstalter'])),
        ))
        db.send_create_signal(u'auszeichnungen', ['Auszeichnung'])

        # Adding model 'AuszeichnungsPlugin'
        db.create_table(u'cmsplugin_auszeichnungsplugin', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('auszeichnung', self.gf('django.db.models.fields.related.ForeignKey')(related_name='plugins', to=orm['auszeichnungen.Auszeichnung'])),
        ))
        db.send_create_signal(u'auszeichnungen', ['AuszeichnungsPlugin'])


    def backwards(self, orm):
        # Deleting model 'Veranstalter'
        db.delete_table(u'auszeichnungen_veranstalter')

        # Deleting model 'Auszeichnung'
        db.delete_table(u'auszeichnungen_auszeichnung')

        # Deleting model 'AuszeichnungsPlugin'
        db.delete_table(u'cmsplugin_auszeichnungsplugin')


    models = {
        u'auszeichnungen.auszeichnung': {
            'Meta': {'object_name': 'Auszeichnung'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jahr': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'titel': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'veranstalter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auszeichnungen.Veranstalter']"})
        },
        u'auszeichnungen.auszeichnungsplugin': {
            'Meta': {'object_name': 'AuszeichnungsPlugin', 'db_table': "u'cmsplugin_auszeichnungsplugin'", '_ormbases': ['cms.CMSPlugin']},
            'auszeichnung': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'plugins'", 'to': u"orm['auszeichnungen.Auszeichnung']"}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'auszeichnungen.veranstalter': {
            'Meta': {'object_name': 'Veranstalter'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '2000'})
        },
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['auszeichnungen']
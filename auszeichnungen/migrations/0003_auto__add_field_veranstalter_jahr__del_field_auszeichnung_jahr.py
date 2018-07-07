# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Veranstalter.jahr'
        db.add_column(u'auszeichnungen_veranstalter', 'jahr',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=4),
                      keep_default=False)

        # Deleting field 'Auszeichnung.jahr'
        db.delete_column(u'auszeichnungen_auszeichnung', 'jahr')


    def backwards(self, orm):
        # Deleting field 'Veranstalter.jahr'
        db.delete_column(u'auszeichnungen_veranstalter', 'jahr')

        # Adding field 'Auszeichnung.jahr'
        db.add_column(u'auszeichnungen_auszeichnung', 'jahr',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=4),
                      keep_default=False)


    models = {
        u'auszeichnungen.auszeichnung': {
            'Meta': {'object_name': 'Auszeichnung'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            'jahr': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
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
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EventCategoryTranslation'
        db.create_table(u'simple_events_eventcategory_translation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['simple_events.EventCategory'])),
        ))
        db.send_create_signal(u'simple_events', ['EventCategoryTranslation'])

        # Adding unique constraint on 'EventCategoryTranslation', fields ['language_code', 'master']
        db.create_unique(u'simple_events_eventcategory_translation', ['language_code', 'master_id'])

        # Adding model 'EventCategory'
        db.create_table(u'simple_events_eventcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'simple_events', ['EventCategory'])

        # Adding M2M table for field sites on 'EventCategory'
        m2m_table_name = db.shorten_name(u'simple_events_eventcategory_sites')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('eventcategory', models.ForeignKey(orm[u'simple_events.eventcategory'], null=False)),
            ('site', models.ForeignKey(orm[u'sites.site'], null=False))
        ))
        db.create_unique(m2m_table_name, ['eventcategory_id', 'site_id'])

        # Adding model 'EventTranslation'
        db.create_table(u'simple_events_event_translation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('language_code', self.gf('django.db.models.fields.CharField')(max_length=15, db_index=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(related_name='translations', null=True, to=orm['simple_events.Event'])),
        ))
        db.send_create_signal(u'simple_events', ['EventTranslation'])

        # Adding unique constraint on 'EventTranslation', fields ['language_code', 'master']
        db.create_unique(u'simple_events_event_translation', ['language_code', 'master_id'])

        # Adding model 'Event'
        db.create_table(u'simple_events_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cms.Placeholder'], null=True, blank=True)),
            ('start', self.gf('django.db.models.fields.DateField')()),
            ('time', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('end', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'simple_events', ['Event'])

        # Adding M2M table for field categories on 'Event'
        m2m_table_name = db.shorten_name(u'simple_events_event_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm[u'simple_events.event'], null=False)),
            ('eventcategory', models.ForeignKey(orm[u'simple_events.eventcategory'], null=False))
        ))
        db.create_unique(m2m_table_name, ['event_id', 'eventcategory_id'])

        # Adding M2M table for field sites on 'Event'
        m2m_table_name = db.shorten_name(u'simple_events_event_sites')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm[u'simple_events.event'], null=False)),
            ('site', models.ForeignKey(orm[u'sites.site'], null=False))
        ))
        db.create_unique(m2m_table_name, ['event_id', 'site_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'EventTranslation', fields ['language_code', 'master']
        db.delete_unique(u'simple_events_event_translation', ['language_code', 'master_id'])

        # Removing unique constraint on 'EventCategoryTranslation', fields ['language_code', 'master']
        db.delete_unique(u'simple_events_eventcategory_translation', ['language_code', 'master_id'])

        # Deleting model 'EventCategoryTranslation'
        db.delete_table(u'simple_events_eventcategory_translation')

        # Deleting model 'EventCategory'
        db.delete_table(u'simple_events_eventcategory')

        # Removing M2M table for field sites on 'EventCategory'
        db.delete_table(db.shorten_name(u'simple_events_eventcategory_sites'))

        # Deleting model 'EventTranslation'
        db.delete_table(u'simple_events_event_translation')

        # Deleting model 'Event'
        db.delete_table(u'simple_events_event')

        # Removing M2M table for field categories on 'Event'
        db.delete_table(db.shorten_name(u'simple_events_event_categories'))

        # Removing M2M table for field sites on 'Event'
        db.delete_table(db.shorten_name(u'simple_events_event_sites'))


    models = {
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        u'simple_events.event': {
            'Meta': {'ordering': "('-start',)", 'object_name': 'Event'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['simple_events.EventCategory']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True', 'blank': 'True'}),
            'end': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'default': '[1]', 'to': u"orm['sites.Site']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'start': ('django.db.models.fields.DateField', [], {}),
            'time': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'simple_events.eventcategory': {
            'Meta': {'object_name': 'EventCategory'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['sites.Site']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'simple_events.eventcategorytranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'EventCategoryTranslation', 'db_table': "u'simple_events_eventcategory_translation'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['simple_events.EventCategory']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'simple_events.eventtranslation': {
            'Meta': {'unique_together': "[('language_code', 'master')]", 'object_name': 'EventTranslation', 'db_table': "u'simple_events_event_translation'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'translations'", 'null': 'True', 'to': u"orm['simple_events.Event']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['simple_events']
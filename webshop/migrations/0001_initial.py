# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Wein'
        db.create_table(u'webshop_wein', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('polymorphic_ctype', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'polymorphic_webshop.wein_set', null=True, to=orm['contenttypes.ContentType'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('unit_price', self.gf('django.db.models.fields.DecimalField')(default='0.0', max_digits=30, decimal_places=2)),
            ('main_category', self.gf('mptt.fields.TreeForeignKey')(to=orm['weinkategorien.Category'])),
            ('img', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('lage', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('jahrgang', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('sauere', self.gf('django.db.models.fields.FloatField')()),
            ('suesse', self.gf('django.db.models.fields.FloatField')()),
            ('alk', self.gf('django.db.models.fields.FloatField')()),
            ('vol', self.gf('django.db.models.fields.FloatField')()),
            ('bouquet', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('auszeichnung', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auszeichnungen.Auszeichnung'], null=True, on_delete=models.SET_NULL, blank=True)),
        ))
        db.send_create_signal(u'webshop', ['Wein'])

        # Adding M2M table for field additional_categories on 'Wein'
        m2m_table_name = db.shorten_name(u'webshop_wein_additional_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('wein', models.ForeignKey(orm[u'webshop.wein'], null=False)),
            ('category', models.ForeignKey(orm['weinkategorien.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['wein_id', 'category_id'])


    def backwards(self, orm):
        # Deleting model 'Wein'
        db.delete_table(u'webshop_wein')

        # Removing M2M table for field additional_categories on 'Wein'
        db.delete_table(db.shorten_name(u'webshop_wein_additional_categories'))


    models = {
        u'auszeichnungen.auszeichnung': {
            'Meta': {'object_name': 'Auszeichnung'},
            'beschreibung': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jahr': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'webshop.wein': {
            'Meta': {'object_name': 'Wein'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'additional_categories': ('mptt.fields.TreeManyToManyField', [], {'related_name': "'extra_product_categories'", 'symmetrical': 'False', 'to': "orm['weinkategorien.Category']"}),
            'alk': ('django.db.models.fields.FloatField', [], {}),
            'auszeichnung': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auszeichnungen.Auszeichnung']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'bouquet': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'jahrgang': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'lage': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'main_category': ('mptt.fields.TreeForeignKey', [], {'to': "orm['weinkategorien.Category']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'polymorphic_webshop.wein_set'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'sauere': ('django.db.models.fields.FloatField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'suesse': ('django.db.models.fields.FloatField', [], {}),
            'unit_price': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '30', 'decimal_places': '2'}),
            'vol': ('django.db.models.fields.FloatField', [], {})
        },
        'weinkategorien.category': {
            'Meta': {'object_name': 'Category'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'descr': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name_path': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['weinkategorien.Category']"}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        }
    }

    complete_apps = ['webshop']
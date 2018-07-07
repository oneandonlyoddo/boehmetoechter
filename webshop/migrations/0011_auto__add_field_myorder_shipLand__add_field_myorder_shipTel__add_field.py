# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'myOrder.shipLand'
        db.add_column(u'webshop_myorder', 'shipLand',
                      self.gf('django.db.models.fields.CharField')(default='Deutschland', max_length=255),
                      keep_default=False)

        # Adding field 'myOrder.shipTel'
        db.add_column(u'webshop_myorder', 'shipTel',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=255),
                      keep_default=False)

        # Adding field 'myOrder.shipFax'
        db.add_column(u'webshop_myorder', 'shipFax',
                      self.gf('django.db.models.fields.CharField')(default=0, max_length=255),
                      keep_default=False)

        # Adding field 'myOrder.billLand'
        db.add_column(u'webshop_myorder', 'billLand',
                      self.gf('django.db.models.fields.CharField')(default='Deutschland', max_length=255),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'myOrder.shipLand'
        db.delete_column(u'webshop_myorder', 'shipLand')

        # Deleting field 'myOrder.shipTel'
        db.delete_column(u'webshop_myorder', 'shipTel')

        # Deleting field 'myOrder.shipFax'
        db.delete_column(u'webshop_myorder', 'shipFax')

        # Deleting field 'myOrder.billLand'
        db.delete_column(u'webshop_myorder', 'billLand')


    models = {
        u'auszeichnungen.auszeichnung': {
            'Meta': {'object_name': 'Auszeichnung'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titel': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'veranstalter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auszeichnungen.Veranstalter']"})
        },
        u'auszeichnungen.veranstalter': {
            'Meta': {'object_name': 'Veranstalter'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jahr': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '2000'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'webshop.artkategorie': {
            'Meta': {'ordering': "['sortID']", 'object_name': 'ArtKategorie'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'sortID': ('django.db.models.fields.IntegerField', [], {'max_length': '1'})
        },
        u'webshop.lagekategorie': {
            'Meta': {'ordering': "['sortID']", 'object_name': 'LageKategorie'},
            'beschreibung': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255'}),
            'sortID': ('django.db.models.fields.IntegerField', [], {'max_length': '1'})
        },
        u'webshop.myorder': {
            'Meta': {'object_name': 'myOrder'},
            'billLand': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'billNr': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'billPrename': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'billStreet': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'billSurname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'billTown': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'billZipCode': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'billing_address_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'cart_pk': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'emailForConfirm': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'order_subtotal': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '30', 'decimal_places': '2'}),
            'order_total': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '30', 'decimal_places': '2'}),
            'shipFax': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'shipLand': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'shipNr': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'shipPrename': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'shipStreet': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'shipSurname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'shipTel': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'shipTown': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'shipZipCode': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'shipping_address_text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        u'webshop.wein': {
            'Meta': {'ordering': "['slug']", 'object_name': 'Wein'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'alk': ('django.db.models.fields.FloatField', [], {}),
            'art': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['webshop.ArtKategorie']", 'null': 'True', 'blank': 'True'}),
            'auszeichnung': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['auszeichnungen.Auszeichnung']", 'null': 'True', 'blank': 'True'}),
            'bouquet': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'jahrgang': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'kat': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['webshop.LageKategorie']", 'null': 'True', 'blank': 'True'}),
            'lage': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'listed': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'polymorphic_webshop.wein_set'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'sauere': ('django.db.models.fields.FloatField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'suesse': ('django.db.models.fields.FloatField', [], {}),
            'unit_price': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '30', 'decimal_places': '2'}),
            'vol': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['webshop']
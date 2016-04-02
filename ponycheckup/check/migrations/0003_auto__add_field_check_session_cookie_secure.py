# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Check.session_cookie_secure'
        db.add_column('check_check', 'session_cookie_secure',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Check.session_cookie_secure'
        db.delete_column('check_check', 'session_cookie_secure')


    models = {
        'check.check': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Check'},
            'admin_forces_https': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'admin_found': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allows_trace': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'csrf_cookie_found': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hsts_header_found': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'login_forces_https': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'login_found': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'session_cookie_found': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'session_cookie_httponly': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'session_cookie_secure': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'xframe_header_found': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['check']
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Page'
        db.create_table('content_page', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=500)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['users.User'], blank=True, null=True, related_name='+')),
        ))
        db.send_create_signal('content', ['Page'])

        # Adding model 'Article'
        db.create_table('content_article', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=500)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['users.User'], blank=True, null=True, related_name='+')),
        ))
        db.send_create_signal('content', ['Article'])

        # Adding model 'FaqEntry'
        db.create_table('content_faqentry', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now_add=True)),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now=True)),
            ('question', self.gf('django.db.models.fields.TextField')()),
            ('response', self.gf('django.db.models.fields.TextField')()),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['users.User'], blank=True, null=True, related_name='+')),
        ))
        db.send_create_signal('content', ['FaqEntry'])


    def backwards(self, orm):
        # Deleting model 'Page'
        db.delete_table('content_page')

        # Deleting model 'Article'
        db.delete_table('content_article')

        # Deleting model 'FaqEntry'
        db.delete_table('content_faqentry')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'content.article': {
            'Meta': {'object_name': 'Article'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['users.User']", 'blank': 'True', 'null': 'True', 'related_name': "'+'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '500'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'content.faqentry': {
            'Meta': {'object_name': 'FaqEntry'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['users.User']", 'blank': 'True', 'null': 'True', 'related_name': "'+'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'question': ('django.db.models.fields.TextField', [], {}),
            'response': ('django.db.models.fields.TextField', [], {})
        },
        'content.page': {
            'Meta': {'object_name': 'Page'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['users.User']", 'blank': 'True', 'null': 'True', 'related_name': "'+'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '500'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)", 'db_table': "'django_content_type'", 'object_name': 'ContentType'},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'users.user': {
            'Meta': {'ordering': "('first_name', 'last_name', 'email')", 'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 11, 28, 0, 0)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'unique': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True', 'null': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Group']", 'blank': 'True', 'related_name': "'user_set'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True', 'null': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True', 'related_name': "'user_set'"})
        }
    }

    complete_apps = ['content']
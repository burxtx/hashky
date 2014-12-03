# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BlogPost'
        db.create_table(u'blog_blogpost', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modify_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal(u'blog', ['BlogPost'])

        # Adding model 'Collection'
        db.create_table(u'blog_collection', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=150)),
            ('desc', self.gf('django.db.models.fields.TextField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'blog', ['Collection'])

        # Adding model 'Tag'
        db.create_table(u'blog_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64)),
        ))
        db.send_create_signal(u'blog', ['Tag'])

        # Adding M2M table for field blogposts on 'Tag'
        m2m_table_name = db.shorten_name(u'blog_tag_blogposts')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tag', models.ForeignKey(orm[u'blog.tag'], null=False)),
            ('blogpost', models.ForeignKey(orm[u'blog.blogpost'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tag_id', 'blogpost_id'])

        # Adding M2M table for field collections on 'Tag'
        m2m_table_name = db.shorten_name(u'blog_tag_collections')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tag', models.ForeignKey(orm[u'blog.tag'], null=False)),
            ('collection', models.ForeignKey(orm[u'blog.collection'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tag_id', 'collection_id'])

        # Adding model 'Followingship'
        db.create_table(u'blog_followingship', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('following', self.gf('django.db.models.fields.related.ForeignKey')(related_name='following_set', to=orm['auth.User'])),
            ('followers', self.gf('django.db.models.fields.related.ForeignKey')(related_name='followers_set', to=orm['auth.User'])),
        ))
        db.send_create_signal(u'blog', ['Followingship'])

        # Adding unique constraint on 'Followingship', fields ['followers', 'following']
        db.create_unique(u'blog_followingship', ['followers_id', 'following_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Followingship', fields ['followers', 'following']
        db.delete_unique(u'blog_followingship', ['followers_id', 'following_id'])

        # Deleting model 'BlogPost'
        db.delete_table(u'blog_blogpost')

        # Deleting model 'Collection'
        db.delete_table(u'blog_collection')

        # Deleting model 'Tag'
        db.delete_table(u'blog_tag')

        # Removing M2M table for field blogposts on 'Tag'
        db.delete_table(db.shorten_name(u'blog_tag_blogposts'))

        # Removing M2M table for field collections on 'Tag'
        db.delete_table(db.shorten_name(u'blog_tag_collections'))

        # Deleting model 'Followingship'
        db.delete_table(u'blog_followingship')


    models = {
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'blog.blogpost': {
            'Meta': {'object_name': 'BlogPost'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modify_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'blog.collection': {
            'Meta': {'object_name': 'Collection'},
            'desc': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'blog.followingship': {
            'Meta': {'unique_together': "(('followers', 'following'),)", 'object_name': 'Followingship'},
            'followers': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'followers_set'", 'to': u"orm['auth.User']"}),
            'following': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'following_set'", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'blog.tag': {
            'Meta': {'object_name': 'Tag'},
            'blogposts': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['blog.BlogPost']", 'symmetrical': 'False'}),
            'collections': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['blog.Collection']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['blog']
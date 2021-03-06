# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Pathway'
        db.create_table(u'pathways_pathway', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=256)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('private_owners', self.gf('django.db.models.fields.BooleanField')()),
            ('public_owners', self.gf('django.db.models.fields.BooleanField')()),
            (u'language', self.gf('django.db.models.fields.CharField')(default='en', max_length=10)),
            (u'translation_of', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'translations', null=True, to=orm['pathways.Pathway'])),
        ))
        db.send_create_signal(u'pathways', ['Pathway'])

        # Adding M2M table for field specific_private_owners on 'Pathway'
        m2m_table_name = db.shorten_name(u'pathways_pathway_specific_private_owners')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pathway', models.ForeignKey(orm[u'pathways.pathway'], null=False)),
            ('owner', models.ForeignKey(orm[u'owners.owner'], null=False))
        ))
        db.create_unique(m2m_table_name, ['pathway_id', 'owner_id'])

        # Adding M2M table for field specific_public_owners on 'Pathway'
        m2m_table_name = db.shorten_name(u'pathways_pathway_specific_public_owners')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pathway', models.ForeignKey(orm[u'pathways.pathway'], null=False)),
            ('owner', models.ForeignKey(orm[u'owners.owner'], null=False))
        ))
        db.create_unique(m2m_table_name, ['pathway_id', 'owner_id'])

        # Adding model 'RichTextContent'
        db.create_table(u'pathways_pathway_richtextcontent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('feincms.contrib.richtext.RichTextField')(blank=True)),
            (u'parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'richtextcontent_set', to=orm['pathways.Pathway'])),
            (u'region', self.gf('django.db.models.fields.CharField')(max_length=255)),
            (u'ordering', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'pathways', ['RichTextContent'])

        # Adding model 'MediaFileContent'
        db.create_table(u'pathways_pathway_mediafilecontent', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mediafile', self.gf('feincms.module.medialibrary.fields.MediaFileForeignKey')(related_name=u'+', to=orm['medialibrary.MediaFile'])),
            (u'parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'mediafilecontent_set', to=orm['pathways.Pathway'])),
            (u'region', self.gf('django.db.models.fields.CharField')(max_length=255)),
            (u'ordering', self.gf('django.db.models.fields.IntegerField')(default=0)),
            (u'type', self.gf('django.db.models.fields.CharField')(default='default', max_length=20)),
        ))
        db.send_create_signal(u'pathways', ['MediaFileContent'])


    def backwards(self, orm):
        # Deleting model 'Pathway'
        db.delete_table(u'pathways_pathway')

        # Removing M2M table for field specific_private_owners on 'Pathway'
        db.delete_table(db.shorten_name(u'pathways_pathway_specific_private_owners'))

        # Removing M2M table for field specific_public_owners on 'Pathway'
        db.delete_table(db.shorten_name(u'pathways_pathway_specific_public_owners'))

        # Deleting model 'RichTextContent'
        db.delete_table(u'pathways_pathway_richtextcontent')

        # Deleting model 'MediaFileContent'
        db.delete_table(u'pathways_pathway_mediafilecontent')


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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'livinglots_owners.alias': {
            'Meta': {'object_name': 'Alias'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '256'})
        },
        u'medialibrary.category': {
            'Meta': {'ordering': "[u'parent__title', u'title']", 'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'children'", 'null': 'True', 'to': u"orm['medialibrary.Category']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '150'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'medialibrary.mediafile': {
            'Meta': {'ordering': "[u'-created']", 'object_name': 'MediaFile'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['medialibrary.Category']", 'null': 'True', 'blank': 'True'}),
            'copyright': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '255'}),
            'file_size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        },
        u'owners.owner': {
            'Meta': {'object_name': 'Owner'},
            'aliases': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['livinglots_owners.Alias']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '256'}),
            'owner_type': ('django.db.models.fields.CharField', [], {'default': "'private'", 'max_length': '20'})
        },
        u'pathways.mediafilecontent': {
            'Meta': {'ordering': "[u'ordering']", 'object_name': 'MediaFileContent', 'db_table': "u'pathways_pathway_mediafilecontent'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mediafile': ('feincms.module.medialibrary.fields.MediaFileForeignKey', [], {'related_name': "u'+'", 'to': u"orm['medialibrary.MediaFile']"}),
            u'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'mediafilecontent_set'", 'to': u"orm['pathways.Pathway']"}),
            u'region': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'type': ('django.db.models.fields.CharField', [], {'default': "'default'", 'max_length': '20'})
        },
        u'pathways.pathway': {
            'Meta': {'object_name': 'Pathway'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            u'language': ('django.db.models.fields.CharField', [], {'default': "'en'", 'max_length': '10'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'private_owners': ('django.db.models.fields.BooleanField', [], {}),
            'public_owners': ('django.db.models.fields.BooleanField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '256'}),
            'specific_private_owners': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'private+'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['owners.Owner']"}),
            'specific_public_owners': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'public+'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['owners.Owner']"}),
            u'translation_of': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'translations'", 'null': 'True', 'to': u"orm['pathways.Pathway']"})
        },
        u'pathways.richtextcontent': {
            'Meta': {'ordering': "[u'ordering']", 'object_name': 'RichTextContent', 'db_table': "u'pathways_pathway_richtextcontent'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'richtextcontent_set'", 'to': u"orm['pathways.Pathway']"}),
            u'region': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'text': ('feincms.contrib.richtext.RichTextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['pathways']
# Generated by Django 2.1.1 on 2018-09-30 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='gendder',
            new_name='gender',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='station',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='最寄駅'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='status',
            field=models.CharField(choices=[('1', '稼働終了が確定しているので案件を積極的に探している'), ('2', '即日稼働可能なので緊急で案件を探している'), ('3', '現在稼働中だが希望条件にあう案件があれば検討したい')], default='female', max_length=30, verbose_name='現在の状況'),
        ),
    ]

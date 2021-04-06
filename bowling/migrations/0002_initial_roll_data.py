from django.db import migrations


def initial_roll_data(apps, schema_editor):
    roll = apps.get_model('bowling', 'Roll')
    roll_list = []
    for index in range(-1, 11):
        roll_list.append(
            roll(
                pins_hit=index
            )
        )
    roll.objects.bulk_create(roll_list)


class Migration(migrations.Migration):
    dependencies = [
        ('bowling', '0001_initial')
    ]
    operations = [
        migrations.RunPython(initial_roll_data)
    ]

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up

# * Rearrange models's order
# * Make sure each model has one filed with primary_key = True
# * Make sure each ForeignKey and OneToOneField has "on_delete" set to the desired behavior
# * Remove 'managed = False' lines if you wish to allow Django to create, modify, and delete the table

# Feel free to rename the models, but don't rename db_tables values or field names

from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.core.validators import MinValueValidator


class Affiliation(models.Model):
    """
    Table used to record organization, groups or other affiliation
    """

    affiliation_id = models.AutoField(primary_key=True)
    affiliation_name = models.CharField(max_length=50)
    foundation_year = models.PositiveIntegerField()
    is_active = models.BooleanField()
    dissolution_year = models.PositiveIntegerField(blank=True, null=True)
    base_of_operations = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'affiliations'


class Alias(models.Model):
    alias_id = models.AutoField(primary_key=True)
    alias = models.CharField(unique=True, max_length=50)

    class Meta:
        db_table = 'aliases'


class BloodStatus(models.Model):
    blood_status_id = models.AutoField(primary_key=True)
    blood_status = models.CharField(max_length=50)

    class Meta:
        db_table = 'blood_statuses'


class CharacterAffiliation(models.Model):
    id = models.AutoField(primary_key=True)
    character = models.OneToOneField('Character', models.CASCADE)
    affiliation = models.ForeignKey(Affiliation, models.CASCADE)
    year_joined = models.PositiveIntegerField()
    year_left = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'characters_affiliations'
        unique_together = (('character', 'affiliation'),)


class CharacterAlias(models.Model):
    id = models.AutoField(primary_key=True)
    alias = models.OneToOneField(Alias, models.DO_NOTHING)
    character = models.ForeignKey('Character', models.DO_NOTHING)

    class Meta:
        db_table = 'characters_aliases'
        unique_together = (('alias', 'character'),)


class CharacterMutation(models.Model):
    id = models.AutoField(primary_key=True)
    character = models.OneToOneField('Character', models.DO_NOTHING)
    mutation = models.ForeignKey('Mutation', models.DO_NOTHING)

    class Meta:
        db_table = 'characters_mutations'
        unique_together = (('character', 'mutation'),)


class CharacterType(models.Model):
    character_type_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=50)

    class Meta:
        db_table = 'character_types'


class Character(models.Model):
    character_id = models.AutoField(primary_key=True)
    character_type = models.ForeignKey(CharacterType, on_delete=models.DO_NOTHING)
    given_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    surname = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=8, blank=True, null=True)
    nickname = models.CharField(max_length=50, blank=True, null=True)
    birthdate = models.DateField()
    birthplace = models.CharField(max_length=50, blank=True, null=True)
    deathdate = models.DateField(blank=True, null=True)
    occupation = models.CharField(max_length=50, blank=True, null=True)
    picture_url = models.ImageField(upload_to="character_img/", blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()
    user = models.ForeignKey('User', models.CASCADE)
    marital_status = models.ForeignKey('MaritalStatus', models.DO_NOTHING, blank=True, null=True)
    species = models.ForeignKey('Species', models.DO_NOTHING, blank=True, null=True)
    gender_identity = models.ForeignKey('GenderIdentity', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'characters'


class Config(models.Model):
    config_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    description = models.TextField()
    value = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'configs'


class DivineGroup(models.Model):
    divine_group_id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    god = models.ForeignKey('God', models.SET_NULL, blank=True, null=True)
    foundation_year = models.PositiveSmallIntegerField(blank=True, null=True)
    dissolution_year = models.PositiveSmallIntegerField(blank=True, null=True)
    base_of_operation = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'divine_groups'


class GenderIdentity(models.Model):
    gender_identity_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=50)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'gender_identities'


class God(models.Model):
    god_id = models.AutoField(primary_key=True)
    pantheon = models.ForeignKey('Pantheon', models.DO_NOTHING)
    god_name = models.CharField(max_length=50)
    power_sphere = models.CharField(max_length=100, blank=True, null=True)
    animal_symbol = models.CharField(max_length=50, blank=True, null=True)
    other_symbol = models.CharField(max_length=50, blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'gods'


class House(models.Model):
    house_id = models.AutoField(primary_key=True)
    house_name = models.CharField(max_length=50)
    school_system = models.CharField(max_length=50)
    symbol = models.CharField(max_length=50, blank=True, null=True)
    founder_first_name = models.CharField(max_length=50, blank=True, null=True)
    founder_last_name = models.CharField(max_length=50, blank=True, null=True)
    primary_color = models.CharField(max_length=50, blank=True, null=True)
    secondary_color = models.CharField(max_length=50, blank=True, null=True)
    wizarding_school = models.ForeignKey('WizardingSchool', models.DO_NOTHING)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'houses'


class Leader(models.Model):
    """ Table used to record organization, groups or other affiliation """
    id = models.AutoField(primary_key=True)
    character = models.OneToOneField(Character, models.CASCADE)
    affiliation = models.ForeignKey(Affiliation, models.CASCADE)
    year_started = models.PositiveSmallIntegerField()
    year_ended = models.PositiveSmallIntegerField(blank=True, null=True)
    is_current_leader = models.BooleanField(blank=True)

    class Meta:
        db_table = 'affiliations_leadership'
        unique_together = (('character', 'affiliation', 'year_started'),)


class MaritalStatus(models.Model):
    marital_status_id = models.AutoField(primary_key=True)
    marital_status = models.CharField(unique=True, max_length=50)

    class Meta:
        db_table = 'marital_status'


class MutagenicLevel(models.Model):
    mutagenic_level_id = models.AutoField(primary_key=True)
    mutagenic_level_name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'mutagenic_level' 


class Mutation(models.Model):
    mutation_id = models.AutoField(primary_key=True)
    description = models.TextField()

    class Meta:
        db_table = 'mutations'


class Pantheon(models.Model):
    pantheon_id = models.AutoField(primary_key=True)
    pantheon_name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    leader = models.CharField(max_length=50, blank=True, null=True)
    overworld = models.CharField(max_length=50, blank=True, null=True)
    underworld = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    virtues = models.CharField(max_length=50, blank=True, null=True)
    hubris = models.CharField(max_length=50, blank=True, null=True)
    purview = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'pantheons'


class Platform(models.Model):
    platform_id = models.AutoField(primary_key=True)
    platform_name = models.CharField(unique=True, max_length=50)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'platforms'


class PlatformMutant(models.Model):
    id = models.AutoField(primary_key=True)
    character = models.OneToOneField(Character, on_delete=models.DO_NOTHING)
    mutation = models.ForeignKey(Mutation, on_delete=models.DO_NOTHING)
    mutagenic_level = models.ForeignKey(MutagenicLevel, on_delete=models.DO_NOTHING, blank=True, null=True)
    manifestation_date = models.DateField(blank=True, null=True)
    base_of_operation = models.CharField(max_length=50, blank=True, null=True)
    control_power = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0)])
    danger = models.IntegerField(blank=True, null=True)
    fbi_risk = models.IntegerField(blank=True, null=True)
    public_identity = models.IntegerField(blank=True, null=True)
    reality = models.CharField(max_length=45)

    class Meta:
        db_table = 'platform_mutante'
        unique_together = (('character', 'mutation'),)


class PlatformOlympian(models.Model):
    id = models.AutoField(primary_key=True)
    platform = models.OneToOneField(Platform, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.RESTRICT)
    god = models.ForeignKey(God, on_delete=models.SET_NULL, null=True)
    pantheon = models.ForeignKey(Pantheon, on_delete=models.RESTRICT)
    type = models.CharField(max_length=9, blank=True, null=True)
    year_claimed = models.PositiveSmallIntegerField()
    divine_group = models.ForeignKey(DivineGroup, on_delete=models.SET_NULL, blank=True, null=True)
    camp_assigned = models.CharField(max_length=50, blank=True, null=True)
    powers = models.TextField(blank=True, null=True)
    favored_weapon = models.CharField(max_length=50, blank=True, null=True)
    quest_count = models.PositiveIntegerField(blank=True, null=True)
    legacy_of = models.ForeignKey(God, on_delete=models.SET_NULL, related_name='platformolimpiano_legacy_of_god', blank=True, null=True)

    class Meta:
        db_table = 'platform_olimpiano'
        constraints = [
            models.UniqueConstraint(fields=['platform', 'character'], name='unique_platform_character')
        ]


class PlatformPotterian(models.Model):
    id = models.AutoField(primary_key=True)
    platform = models.OneToOneField(Platform, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    wizarding_school = models.ForeignKey('WizardingSchool', on_delete=models.SET_NULL, blank=True, null=True)
    house = models.ForeignKey(House, on_delete=models.SET_NULL, blank=True, null=True)
    wand = models.ForeignKey('Wand', on_delete=models.SET_NULL, blank=True, null=True)
    blood_status = models.ForeignKey(BloodStatus, on_delete=models.CASCADE, blank=True, null=True)
    year_enrolled = models.PositiveSmallIntegerField(blank=True, null=True)
    boggart = models.CharField(max_length=45, blank=True, null=True)
    patronus = models.CharField(max_length=45, blank=True, null=True)
    animagus = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'platform_potteriano'
        unique_together = (('platform', 'character'),)


class Professor(models.Model):
    professor_id = models.AutoField(primary_key=True)
    wizarding_school = models.ForeignKey('WizardingSchool', on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)

    class Meta:
        db_table = 'professors'


class Species(models.Model):
    species_id = models.AutoField(primary_key=True)
    species_name = models.CharField(unique=True, max_length=50)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'species'


class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=50)
    category = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'subjects'


class SubjectTaught(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.OneToOneField(Subject, on_delete=models.SET_NULL, null=True)
    professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True)
    wizarding_school = models.ForeignKey('WizardingSchool', on_delete=models.SET_NULL, null=True)
    year_taught = models.PositiveSmallIntegerField()

    class Meta:
        db_table = 'subjects_taught'
        unique_together = (('subject', 'professor', 'year_taught'),)


class UserType(models.Model):
    user_type_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=50)

    class Meta:
        db_table = 'user_types'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=50)
    email = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthdate = models.DateField(blank=True, null=True)
    picture_url = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    user_type = models.ForeignKey(UserType, on_delete=models.SET_DEFAULT, default=3)

    def __str__(self):
        return f"{self.username} ({self.email})"

    def save(self, *args, **kwargs):
        if not self.pk or not check_password(self.password, User.objects.get(pk=self.pk).password):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    @classmethod
    def create_user(cls, username, email, password):
        """
        Method for a profile create.
        
        """
        hashed_passowrd = make_password(password)
        user = cls(username=username, email=email, password=password)
        user.save()
        return user



    class Meta:
        db_table = 'users'


class WandCore(models.Model):
    core_id = models.AutoField(primary_key=True)
    substance = models.CharField(max_length=50)
    animal = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'wand_cores'


class WandWood(models.Model):
    wood_id = models.AutoField(primary_key=True)
    wood_name = models.CharField(unique=True, max_length=50)
    description = models.TextField(blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'wand_woods'


class Wandmaker(models.Model):
    wandmaker_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    shop_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'wandmakers'


class Wand(models.Model):
    wand_id = models.AutoField(primary_key=True)
    wood = models.ForeignKey(WandWood, on_delete=models.SET_NULL, null=True)
    wandmaker = models.ForeignKey(Wandmaker, on_delete=models.SET_NULL, null=True)
    core = models.ForeignKey(WandCore, on_delete=models.SET_NULL, null=True)
    size = models.FloatField(blank=True, null=True)
    flexibility = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    made_at = models.PositiveSmallIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'wands'


class WizardingSchool(models.Model):
    wizarding_school_id = models.AutoField(primary_key=True)
    wizarding_school_name = models.CharField(unique=True, max_length=50)
    full_name = models.CharField(unique=True, max_length=100, blank=True, null=True)
    location = models.CharField(max_length=50)
    foundation_year = models.PositiveSmallIntegerField(blank=True, null=True)
    headmaster = models.CharField(max_length=50, blank=True, null=True)
    deputy_head = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'wizarding_schools'
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AttributeDefinition(models.Model):
    attribute_definition_id = models.IntegerField()
    attribute_name = models.TextField()
    attribute_description = models.TextField(blank=True, null=True)
    attribute_type_concept_id = models.IntegerField()
    attribute_syntax = models.TextField(blank=True, null=True)

    objects = models.Manager()
    class Meta:
        managed = False
        db_table = 'attribute_definition'


class CareSite(models.Model):
    care_site_id = models.IntegerField()
    care_site_name = models.TextField(blank=True, null=True)
    place_of_service_concept_id = models.IntegerField(blank=True, null=True)
    location_id = models.IntegerField(blank=True, null=True)
    care_site_source_value = models.TextField(blank=True, null=True)
    place_of_service_source_value = models.TextField(blank=True, null=True)

    objects = models.Manager()
    class Meta:
        managed = False
        db_table = 'care_site'


class CdmSource(models.Model):
    cdm_source_name = models.TextField()
    cdm_source_abbreviation = models.TextField(blank=True, null=True)
    cdm_holder = models.TextField(blank=True, null=True)
    source_description = models.TextField(blank=True, null=True)
    source_documentation_reference = models.TextField(blank=True, null=True)
    cdm_etl_reference = models.TextField(blank=True, null=True)
    source_release_date = models.DateField(blank=True, null=True)
    cdm_release_date = models.DateField(blank=True, null=True)
    cdm_version = models.TextField(blank=True, null=True)
    vocabulary_version = models.TextField(blank=True, null=True)

    objects = models.Manager()
    class Meta:
        managed = False
        db_table = 'cdm_source'


class Cohort(models.Model):
    cohort_definition_id = models.IntegerField()
    subject_id = models.IntegerField()
    cohort_start_date = models.DateField()
    cohort_end_date = models.DateField()

    objects = models.Manager()
    class Meta:
        managed = False
        db_table = 'cohort'


class CohortAttribute(models.Model):
    cohort_definition_id = models.IntegerField()
    subject_id = models.IntegerField()
    cohort_start_date = models.DateField()
    cohort_end_date = models.DateField()
    attribute_definition_id = models.IntegerField()
    value_as_number = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    value_as_concept_id = models.IntegerField(blank=True, null=True)

    objects = models.Manager()
    class Meta:
        managed = False
        db_table = 'cohort_attribute'


class CohortDefinition(models.Model):
    cohort_definition_id = models.IntegerField()
    cohort_definition_name = models.TextField()
    cohort_definition_description = models.TextField(blank=True, null=True)
    definition_type_concept_id = models.IntegerField()
    cohort_definition_syntax = models.TextField(blank=True, null=True)
    subject_concept_id = models.IntegerField()
    cohort_initiation_date = models.DateField(blank=True, null=True)

    objects = models.Manager()
    class Meta:
        managed = False
        db_table = 'cohort_definition'


class Concept(models.Model):
    concept_id = models.IntegerField()
    concept_name = models.TextField()
    domain_id = models.TextField()
    vocabulary_id = models.TextField()
    concept_class_id = models.TextField()
    standard_concept = models.TextField(blank=True, null=True)
    concept_code = models.TextField()
    valid_start_date = models.DateField()
    valid_end_date = models.DateField()
    invalid_reason = models.TextField(blank=True, null=True)

    objects = models.Manager()
    class Meta:
        managed = False
        db_table = 'concept'


class ConceptAncestor(models.Model):
    ancestor_concept_id = models.IntegerField()
    descendant_concept_id = models.IntegerField()
    min_levels_of_separation = models.IntegerField()
    max_levels_of_separation = models.IntegerField()

    objects = models.Manager()
    class Meta:
        managed = False
        db_table = 'concept_ancestor'


class ConceptClass(models.Model):
    concept_class_id = models.TextField()
    concept_class_name = models.TextField()
    concept_class_concept_id = models.IntegerField()

    objects = models.Manager()
    class Meta:
        managed = False
        db_table = 'concept_class'


class ConceptRelationship(models.Model):
    concept_id_1 = models.IntegerField()
    concept_id_2 = models.IntegerField()
    relationship_id = models.TextField()
    valid_start_date = models.DateField()
    valid_end_date = models.DateField()
    invalid_reason = models.TextField(blank=True, null=True)

    objects = models.Manager()
    class Meta:
        managed = False
        db_table = 'concept_relationship'


class ConceptSynonym(models.Model):
    concept_id = models.IntegerField()
    concept_synonym_name = models.TextField()
    language_concept_id = models.IntegerField()

    objects = models.Manager()
    class Meta:
        managed = False
        db_table = 'concept_synonym'


class ConditionEra(models.Model):
    condition_era_id = models.IntegerField()
    person_id = models.IntegerField()
    condition_concept_id = models.IntegerField()
    condition_era_start_date = models.DateField()
    condition_era_end_date = models.DateField()
    condition_occurrence_count = models.IntegerField(blank=True, null=True)

    objects = models.Manager()
    class Meta:
        managed = False
        db_table = 'condition_era'


class ConditionOccurrence(models.Model):
    condition_occurrence_id = models.IntegerField(primary_key=True)
    person_id = models.IntegerField()
    condition_concept_id = models.IntegerField()
    condition_start_date = models.DateField()
    condition_start_datetime = models.DateTimeField(blank=True, null=True)
    condition_end_date = models.DateField(blank=True, null=True)
    condition_end_datetime = models.DateTimeField(blank=True, null=True)
    condition_type_concept_id = models.IntegerField()
    stop_reason = models.TextField(blank=True, null=True)
    provider_id = models.IntegerField(blank=True, null=True)
    visit_occurrence_id = models.IntegerField(blank=True, null=True)
    visit_detail_id = models.IntegerField(blank=True, null=True)
    condition_source_value = models.TextField(blank=True, null=True)
    condition_source_concept_id = models.IntegerField(blank=True, null=True)
    condition_status_source_value = models.TextField(blank=True, null=True)
    condition_status_concept_id = models.IntegerField(blank=True, null=True)

    objects = models.Manager()

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in ConditionOccurrence._meta.fields]
    class Meta:
        managed = False
        db_table = 'condition_occurrence'


class Cost(models.Model):
    cost_id = models.IntegerField()
    cost_event_id = models.IntegerField()
    cost_domain_id = models.TextField()
    cost_type_concept_id = models.IntegerField()
    currency_concept_id = models.IntegerField(blank=True, null=True)
    total_charge = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    total_cost = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    total_paid = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    paid_by_payer = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    paid_by_patient = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    paid_patient_copay = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    paid_patient_coinsurance = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    paid_patient_deductible = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    paid_by_primary = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    paid_ingredient_cost = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    paid_dispensing_fee = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    payer_plan_period_id = models.IntegerField(blank=True, null=True)
    amount_allowed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    revenue_code_concept_id = models.IntegerField(blank=True, null=True)
    revenue_code_source_value = models.TextField(blank=True, null=True)
    drg_concept_id = models.IntegerField(blank=True, null=True)
    drg_source_value = models.TextField(blank=True, null=True)

    objects = models.Manager()
    class Meta:
        managed = False
        db_table = 'cost'


class Death(models.Model):
    person_id = models.IntegerField()
    death_date = models.DateField()
    death_datetime = models.DateTimeField(blank=True, null=True)
    death_type_concept_id = models.IntegerField()
    cause_concept_id = models.IntegerField(blank=True, null=True)
    cause_source_value = models.TextField(blank=True, null=True)
    cause_source_concept_id = models.IntegerField(blank=True, null=True)

    objects = models.Manager()
    class Meta:
        managed = False
        db_table = 'death'


class DeviceExposure(models.Model):
    device_exposure_id = models.IntegerField()
    person_id = models.IntegerField()
    device_concept_id = models.IntegerField()
    device_exposure_start_date = models.DateField()
    device_exposure_start_datetime = models.DateTimeField(blank=True, null=True)
    device_exposure_end_date = models.DateField(blank=True, null=True)
    device_exposure_end_datetime = models.DateTimeField(blank=True, null=True)
    device_type_concept_id = models.IntegerField()
    unique_device_id = models.TextField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    provider_id = models.IntegerField(blank=True, null=True)
    visit_occurrence_id = models.IntegerField(blank=True, null=True)
    visit_detail_id = models.IntegerField(blank=True, null=True)
    device_source_value = models.TextField(blank=True, null=True)
    device_source_concept_id = models.IntegerField(blank=True, null=True)

    objects = models.Manager()
    class Meta:
        managed = False
        db_table = 'device_exposure'


class Domain(models.Model):
    domain_id = models.TextField()
    domain_name = models.TextField()
    domain_concept_id = models.IntegerField()

    objects = models.Manager()
    class Meta:
        managed = False
        db_table = 'domain'


class DoseEra(models.Model):
    dose_era_id = models.IntegerField()
    person_id = models.IntegerField()
    drug_concept_id = models.IntegerField()
    unit_concept_id = models.IntegerField()
    dose_value = models.DecimalField(max_digits=65535, decimal_places=65535)
    dose_era_start_date = models.DateField(blank=True, null=True)
    dose_era_end_date = models.DateField(blank=True, null=True)
    temporal_unit_concept_id = models.IntegerField(blank=True, null=True)
    temporal_value = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    objects = models.Manager()
    class Meta:
        managed = False
        db_table = 'dose_era'


class DrugEra(models.Model):
    drug_era_id = models.IntegerField()
    person_id = models.IntegerField()
    drug_concept_id = models.IntegerField()
    drug_era_start_date = models.DateField()
    drug_era_end_date = models.DateField()
    drug_exposure_count = models.IntegerField(blank=True, null=True)
    gap_days = models.IntegerField(blank=True, null=True)

    objects = models.Manager()
    class Meta:
        managed = False
        db_table = 'drug_era'


class DrugExposure(models.Model):
    drug_exposure_id = models.IntegerField()
    person_id = models.IntegerField()
    drug_concept_id = models.IntegerField()
    drug_exposure_start_date = models.DateField(blank=True, null=True)
    drug_exposure_start_datetime = models.DateTimeField(blank=True, null=True)
    drug_exposure_end_date = models.DateField(blank=True, null=True)
    drug_exposure_end_datetime = models.DateTimeField(blank=True, null=True)
    verbatim_end_date = models.DateField(blank=True, null=True)
    drug_type_concept_id = models.IntegerField()
    stop_reason = models.TextField(blank=True, null=True)
    refills = models.IntegerField(blank=True, null=True)
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    days_supply = models.IntegerField(blank=True, null=True)
    sig = models.TextField(blank=True, null=True)
    route_concept_id = models.IntegerField(blank=True, null=True)
    lot_number = models.TextField(blank=True, null=True)
    provider_id = models.IntegerField(blank=True, null=True)
    visit_occurrence_id = models.IntegerField(blank=True, null=True)
    visit_detail_id = models.IntegerField(blank=True, null=True)
    drug_source_value = models.TextField(blank=True, null=True)
    drug_source_concept_id = models.IntegerField(blank=True, null=True)
    route_source_value = models.TextField(blank=True, null=True)
    dose_unit_source_value = models.TextField(blank=True, null=True)
    quantity_source_value = models.TextField(blank=True, null=True)

    objects = models.Manager()
    class Meta:
        managed = False
        db_table = 'drug_exposure'


class DrugStrength(models.Model):
    drug_concept_id = models.IntegerField()
    ingredient_concept_id = models.IntegerField()
    amount_value = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_unit_concept_id = models.IntegerField(blank=True, null=True)
    numerator_value = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    numerator_unit_concept_id = models.IntegerField(blank=True, null=True)
    denominator_value = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    denominator_unit_concept_id = models.IntegerField(blank=True, null=True)
    box_size = models.IntegerField(blank=True, null=True)
    valid_start_date = models.DateField()
    valid_end_date = models.DateField()
    invalid_reason = models.TextField(blank=True, null=True)

    objects = models.Manager()
    class Meta:
        managed = False
        db_table = 'drug_strength'


class FactRelationship(models.Model):
    domain_concept_id_1 = models.IntegerField()
    fact_id_1 = models.IntegerField()
    domain_concept_id_2 = models.IntegerField()
    fact_id_2 = models.IntegerField()
    relationship_concept_id = models.IntegerField()

    objects = models.Manager()
    class Meta:
        managed = False
        db_table = 'fact_relationship'


class Location(models.Model):
    location_id = models.IntegerField()
    address_1 = models.TextField(blank=True, null=True)
    address_2 = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    zip = models.TextField(blank=True, null=True)
    county = models.TextField(blank=True, null=True)
    location_source_value = models.TextField(blank=True, null=True)

    objects = models.Manager()
    class Meta:
        managed = False
        db_table = 'location'


class Measurement(models.Model):
    measurement_id = models.IntegerField(primary_key=True)
    person_id = models.IntegerField()
    measurement_concept_id = models.IntegerField()
    measurement_date = models.DateField()
    measurement_datetime = models.DateTimeField(blank=True, null=True)
    measurement_time = models.CharField(max_length=10, blank=True, null=True)
    measurement_type_concept_id = models.IntegerField()
    operator_concept_id = models.IntegerField(blank=True, null=True)
    value_as_number = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    value_as_concept_id = models.IntegerField(blank=True, null=True)
    unit_concept_id = models.IntegerField(blank=True, null=True)
    range_low = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    range_high = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    provider_id = models.IntegerField(blank=True, null=True)
    visit_occurrence_id = models.IntegerField(blank=True, null=True)
    visit_detail_id = models.IntegerField(blank=True, null=True)
    measurement_source_value = models.TextField(blank=True, null=True)
    measurement_source_concept_id = models.IntegerField(blank=True, null=True)
    unit_source_value = models.TextField(blank=True, null=True)
    value_source_value = models.TextField(blank=True, null=True)

    objects = models.Manager()

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Measurement._meta.fields]

    class Meta:
        managed = False
        db_table = 'measurement'


class Metadata(models.Model):
    metadata_concept_id = models.IntegerField()
    metadata_type_concept_id = models.IntegerField()
    name = models.CharField(max_length=250)
    value_as_string = models.TextField(blank=True, null=True)
    value_as_concept_id = models.IntegerField(blank=True, null=True)
    metadata_date = models.DateField(blank=True, null=True)
    metadata_datetime = models.DateTimeField(blank=True, null=True)

    objects = models.Manager()
    class Meta:
        managed = False
        db_table = 'metadata'


class Note(models.Model):
    note_id = models.IntegerField(primary_key=True)
    person_id = models.IntegerField()
    note_date = models.DateField()
    note_datetime = models.DateTimeField(blank=True, null=True)
    note_type_concept_id = models.IntegerField()
    note_class_concept_id = models.IntegerField()
    note_title = models.TextField(blank=True, null=True)
    note_text = models.TextField(blank=True, null=True)
    encoding_concept_id = models.IntegerField()
    language_concept_id = models.IntegerField()
    provider_id = models.IntegerField(blank=True, null=True)
    visit_occurrence_id = models.IntegerField(blank=True, null=True)
    visit_detail_id = models.IntegerField(blank=True, null=True)
    note_source_value = models.TextField(blank=True, null=True)

    objects = models.Manager()

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Note._meta.fields]

    class Meta:
        managed = False
        db_table = 'note'


class NoteNlp(models.Model):
    note_nlp_id = models.IntegerField()
    note_id = models.IntegerField()
    section_concept_id = models.IntegerField(blank=True, null=True)
    snippet = models.TextField(blank=True, null=True)
    lexical_variant = models.TextField()
    note_nlp_concept_id = models.IntegerField(blank=True, null=True)
    note_nlp_source_concept_id = models.IntegerField(blank=True, null=True)
    nlp_system = models.TextField(blank=True, null=True)
    nlp_date = models.DateField()
    nlp_datetime = models.DateTimeField(blank=True, null=True)
    term_exists = models.TextField(blank=True, null=True)
    term_temporal = models.TextField(blank=True, null=True)
    term_modifiers = models.TextField(blank=True, null=True)
    offset_begin = models.IntegerField(blank=True, null=True)
    offset_end = models.IntegerField(blank=True, null=True)
    section_source_value = models.TextField(blank=True, null=True)
    section_source_concept_id = models.IntegerField(blank=True, null=True)

    objects = models.Manager()
    class Meta:
        managed = False
        db_table = 'note_nlp'


class Observation(models.Model):
    observation_id = models.IntegerField(primary_key=True)
    person_id = models.IntegerField()
    observation_concept_id = models.IntegerField()
    observation_date = models.DateField()
    observation_datetime = models.DateTimeField(blank=True, null=True)
    observation_type_concept_id = models.IntegerField()
    value_as_number = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    value_as_string = models.TextField(blank=True, null=True)
    value_as_concept_id = models.IntegerField(blank=True, null=True)
    qualifier_concept_id = models.IntegerField(blank=True, null=True)
    unit_concept_id = models.IntegerField(blank=True, null=True)
    provider_id = models.IntegerField(blank=True, null=True)
    visit_occurrence_id = models.IntegerField(blank=True, null=True)
    visit_detail_id = models.IntegerField(blank=True, null=True)
    observation_source_value = models.TextField(blank=True, null=True)
    observation_source_concept_id = models.IntegerField(blank=True, null=True)
    unit_source_value = models.TextField(blank=True, null=True)
    qualifier_source_value = models.TextField(blank=True, null=True)

    objects = models.Manager()

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Observation._meta.fields]

    class Meta:
        managed = False
        db_table = 'observation'


class ObservationPeriod(models.Model):
    observation_period_id = models.IntegerField()
    person_id = models.IntegerField()
    observation_period_start_date = models.DateField()
    observation_period_end_date = models.DateField()
    period_type_concept_id = models.IntegerField()
    observation_period_start_datetime = models.DateTimeField()
    observation_period_end_datetime = models.DateTimeField()

    objects = models.Manager()
    class Meta:
        managed = False
        db_table = 'observation_period'


class PayerPlanPeriod(models.Model):
    payer_plan_period_id = models.IntegerField()
    person_id = models.IntegerField()
    payer_plan_period_start_date = models.DateField()
    payer_plan_period_end_date = models.DateField()
    payer_concept_id = models.IntegerField(blank=True, null=True)
    payer_source_value = models.TextField(blank=True, null=True)
    payer_source_concept_id = models.IntegerField(blank=True, null=True)
    plan_concept_id = models.IntegerField(blank=True, null=True)
    plan_source_value = models.TextField(blank=True, null=True)
    plan_source_concept_id = models.IntegerField(blank=True, null=True)
    sponsor_concept_id = models.IntegerField(blank=True, null=True)
    sponsor_source_value = models.CharField(max_length=50, blank=True, null=True)
    sponsor_source_concept_id = models.IntegerField(blank=True, null=True)
    family_source_value = models.TextField(blank=True, null=True)
    stop_reason_concept_id = models.IntegerField(blank=True, null=True)
    stop_reason_source_value = models.CharField(max_length=50, blank=True, null=True)
    stop_reason_source_concept_id = models.IntegerField(blank=True, null=True)

    objects = models.Manager()
    class Meta:
        managed = False
        db_table = 'payer_plan_period'


class Person(models.Model):
    person_id = models.IntegerField(primary_key=True)
    gender_concept_id = models.IntegerField()
    year_of_birth = models.IntegerField()
    month_of_birth = models.IntegerField(blank=True, null=True)
    day_of_birth = models.IntegerField(blank=True, null=True)
    birth_datetime = models.DateTimeField(blank=True, null=True)
    race_concept_id = models.IntegerField()
    ethnicity_concept_id = models.IntegerField()
    location_id = models.IntegerField(blank=True, null=True)
    provider_id = models.IntegerField(blank=True, null=True)
    care_site_id = models.IntegerField(blank=True, null=True)
    person_source_value = models.TextField(blank=True, null=True)
    gender_source_value = models.TextField(blank=True, null=True)
    gender_source_concept_id = models.IntegerField(blank=True, null=True)
    race_source_value = models.TextField(blank=True, null=True)
    race_source_concept_id = models.IntegerField(blank=True, null=True)
    ethnicity_source_value = models.TextField(blank=True, null=True)
    ethnicity_source_concept_id = models.IntegerField(blank=True, null=True)

    objects = models.Manager()

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Person._meta.fields]

    class Meta:
        managed = False
        db_table = 'person'


class ProcedureOccurrence(models.Model):
    procedure_occurrence_id = models.IntegerField()
    person_id = models.IntegerField()
    procedure_concept_id = models.IntegerField()
    procedure_date = models.DateField()
    procedure_datetime = models.DateTimeField(blank=True, null=True)
    procedure_type_concept_id = models.IntegerField()
    modifier_concept_id = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    provider_id = models.IntegerField(blank=True, null=True)
    visit_occurrence_id = models.IntegerField(blank=True, null=True)
    visit_detail_id = models.IntegerField(blank=True, null=True)
    procedure_source_value = models.TextField(blank=True, null=True)
    procedure_source_concept_id = models.IntegerField(blank=True, null=True)
    modifier_source_value = models.TextField(blank=True, null=True)

    objects = models.Manager()
    class Meta:
        managed = False
        db_table = 'procedure_occurrence'


class Provider(models.Model):
    provider_id = models.IntegerField()
    provider_name = models.TextField(blank=True, null=True)
    npi = models.TextField(blank=True, null=True)
    dea = models.TextField(blank=True, null=True)
    specialty_concept_id = models.IntegerField(blank=True, null=True)
    care_site_id = models.IntegerField(blank=True, null=True)
    year_of_birth = models.IntegerField(blank=True, null=True)
    gender_concept_id = models.IntegerField(blank=True, null=True)
    provider_source_value = models.TextField(blank=True, null=True)
    specialty_source_value = models.TextField(blank=True, null=True)
    specialty_source_concept_id = models.IntegerField(blank=True, null=True)
    gender_source_value = models.TextField(blank=True, null=True)
    gender_source_concept_id = models.IntegerField(blank=True, null=True)

    objects = models.Manager()
    class Meta:
        managed = False
        db_table = 'provider'


class Relationship(models.Model):
    relationship_id = models.TextField()
    relationship_name = models.TextField()
    is_hierarchical = models.TextField()
    defines_ancestry = models.TextField()
    reverse_relationship_id = models.TextField()
    relationship_concept_id = models.IntegerField()

    objects = models.Manager()
    class Meta:
        managed = False
        db_table = 'relationship'


class SourceToConceptMap(models.Model):
    source_code = models.TextField()
    source_concept_id = models.IntegerField()
    source_vocabulary_id = models.TextField()
    source_code_description = models.TextField(blank=True, null=True)
    target_concept_id = models.IntegerField()
    target_vocabulary_id = models.TextField()
    valid_start_date = models.DateField()
    valid_end_date = models.DateField()
    invalid_reason = models.TextField(blank=True, null=True)

    objects = models.Manager()
    class Meta:
        managed = False
        db_table = 'source_to_concept_map'


class Specimen(models.Model):
    specimen_id = models.IntegerField()
    person_id = models.IntegerField()
    specimen_concept_id = models.IntegerField()
    specimen_type_concept_id = models.IntegerField()
    specimen_date = models.DateField()
    specimen_datetime = models.DateTimeField(blank=True, null=True)
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    unit_concept_id = models.IntegerField(blank=True, null=True)
    anatomic_site_concept_id = models.IntegerField(blank=True, null=True)
    disease_status_concept_id = models.IntegerField(blank=True, null=True)
    specimen_source_id = models.TextField(blank=True, null=True)
    specimen_source_value = models.TextField(blank=True, null=True)
    unit_source_value = models.TextField(blank=True, null=True)
    anatomic_site_source_value = models.TextField(blank=True, null=True)
    disease_status_source_value = models.TextField(blank=True, null=True)

    objects = models.Manager()
    class Meta:
        managed = False
        db_table = 'specimen'


class VisitDetail(models.Model):
    visit_detail_id = models.IntegerField()
    person_id = models.IntegerField()
    visit_detail_concept_id = models.IntegerField()
    visit_start_date = models.DateField()
    visit_start_datetime = models.DateTimeField(blank=True, null=True)
    visit_end_date = models.DateField()
    visit_end_datetime = models.DateTimeField(blank=True, null=True)
    visit_type_concept_id = models.IntegerField()
    provider_id = models.IntegerField(blank=True, null=True)
    care_site_id = models.IntegerField(blank=True, null=True)
    admitting_source_concept_id = models.IntegerField(blank=True, null=True)
    discharge_to_concept_id = models.IntegerField(blank=True, null=True)
    preceding_visit_detail_id = models.IntegerField(blank=True, null=True)
    visit_source_value = models.TextField(blank=True, null=True)
    visit_source_concept_id = models.IntegerField(blank=True, null=True)
    admitting_source_value = models.TextField(blank=True, null=True)
    discharge_to_source_value = models.TextField(blank=True, null=True)
    visit_detail_parent_id = models.IntegerField(blank=True, null=True)
    visit_occurrence_id = models.IntegerField()
    visit_detail_source_value = models.CharField(max_length=50, blank=True, null=True)
    visit_detail_source_concept_id = models.IntegerField(blank=True, null=True)
    admitting_concept_id = models.IntegerField(blank=True, null=True)
    discharge_to_source_concept_id = models.IntegerField(blank=True, null=True)

    objects = models.Manager()
    class Meta:
        managed = False
        db_table = 'visit_detail'


class VisitDetailAssign(models.Model):
    visit_detail_id = models.IntegerField(blank=True, null=True)
    visit_occurrence_id = models.IntegerField(blank=True, null=True)
    visit_start_datetime = models.DateTimeField(blank=True, null=True)
    visit_end_datetime = models.DateTimeField(blank=True, null=True)
    is_first = models.BooleanField(blank=True, null=True)
    is_last = models.BooleanField(blank=True, null=True)
    is_icu = models.BooleanField(blank=True, null=True)
    is_emergency = models.BooleanField(blank=True, null=True)

    objects = models.Manager()
    class Meta:
        managed = False
        db_table = 'visit_detail_assign'


class VisitOccurrence(models.Model):
    visit_occurrence_id = models.IntegerField(primary_key=True)
    person_id = models.IntegerField()
    visit_concept_id = models.IntegerField()
    visit_start_date = models.DateField()
    visit_start_datetime = models.DateTimeField(blank=True, null=True)
    visit_end_date = models.DateField()
    visit_end_datetime = models.DateTimeField(blank=True, null=True)
    visit_type_concept_id = models.IntegerField()
    provider_id = models.IntegerField(blank=True, null=True)
    care_site_id = models.IntegerField(blank=True, null=True)
    visit_source_value = models.TextField(blank=True, null=True)
    visit_source_concept_id = models.IntegerField(blank=True, null=True)
    #admitting_source_concept_id = models.IntegerField(blank=True, null=True)
    #admitting_source_value = models.TextField(blank=True, null=True)
    #discharge_to_concept_id = models.IntegerField(blank=True, null=True)
    #discharge_to_source_value = models.TextField(blank=True, null=True)
    preceding_visit_occurrence_id = models.IntegerField(blank=True, null=True)
    #admitting_concept_id = models.IntegerField(blank=True, null=True)
    #discharge_to_source_concept_id = models.IntegerField(blank=True, null=True)

    objects = models.Manager()

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in VisitOccurrence._meta.fields]

    class Meta:
        managed = False
        db_table = 'visit_occurrence'


class Vocabulary(models.Model):
    vocabulary_id = models.TextField()
    vocabulary_name = models.TextField()
    vocabulary_reference = models.TextField()
    vocabulary_version = models.TextField(blank=True, null=True)
    vocabulary_concept_id = models.IntegerField()

    objects = models.Manager()
    class Meta:
        managed = False
        db_table = 'vocabulary'

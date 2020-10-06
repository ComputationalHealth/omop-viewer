from django.shortcuts import render
from django.http import HttpResponse
from .models import Person as PersonModel
from .models import VisitOccurrence as VisitOccurrenceModel
from .models import Observation as ObservationModel
from .models import ConditionOccurrence as ConditionOccurrenceModel
from .models import Note as NoteModel
from .models import Measurement as MeasurementModel


# Create your views here.
def patViewer(request):
    return render(request, 'index.html')


def search(request):
    person_id = request.POST.get('person_id')
    patient = PersonModel.objects.get(person_id=person_id)
    
    measurements = {}
    measurements = MeasurementModel.objects.filter(person_id=person_id)[:20]
    meas = MeasurementModel.objects.first()
    measurment_fields = {}
    if meas is not None:
        measurement_fields = MeasurementModel.get_fields(meas)

    all_encs = VisitOccurrenceModel.objects.filter(person_id=person_id)

    return render(request, 'index.html', {'patient': patient, 'all_encs': all_encs,
                                        'measurements': measurements, 'measurement_fields': measurment_fields
    })


def patient(request, person_id):
    patient = None
    return render(request, 'index.html')


def encounter(request, visit_occurrence_id):
    enc_id = visit_occurrence_id
    encounter = VisitOccurrenceModel.objects.get(visit_occurrence_id=enc_id)

    # Observations
    observations = {}
    observations = ObservationModel.objects.filter(visit_occurrence_id=enc_id)
    obj = ObservationModel.objects.first()
    objservation_fidlds = {}
    if obj is not None:
        observation_fields = ObservationModel.get_fields(obj)


    # Conditions
    conditions = {}
    conditions = ConditionOccurrenceModel.objects.filter(visit_occurrence_id=enc_id)
    cond = ConditionOccurrenceModel.objects.first()
    condition_fields = {}
    if cond is not None:
        condition_fields = ConditionOccurrenceModel.get_fields(cond)

    # Notes
    notes = {}
    notes = NoteModel.objects.filter(visit_occurrence_id=enc_id)
    note = NoteModel.objects.first()
    note_fields = {}
    if note is not None:
        note_fields = NoteModel.get_fields(note)
    
    return render(request, 'encounter.html', {'encounter': encounter, 
                            'observations': observations, "observation_fields": observation_fields,
                            'conditions': conditions, "condition_fields": condition_fields,
                            'notes': notes, "note_fields": note_fields
                     })

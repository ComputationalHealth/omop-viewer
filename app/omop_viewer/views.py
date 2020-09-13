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


def searchMRN(request):
    mrn_num = request.POST.get('mrn_num')
    patient = PersonModel.objects.get(person_id=mrn_num)
    
    measurements = {}
    measurements = MeasurementModel.objects.filter(person_id=mrn_num)[:20]
    meas = MeasurementModel.objects.first()
    measurment_fields = {}
    if meas is not None:
        measurement_fields = MeasurementModel.get_fields(meas)

    all_encs = VisitOccurrenceModel.objects.filter(person_id=mrn_num)

    return render(request, 'index.html', {'patient': patient, 'all_encs': all_encs,
                                        'measurements': measurements, 'measurement_fields': measurment_fields
    })

def pat_detail(request, mrn):

    pat = None
    return render(request, 'index.html')
    
def enc_detail(request, person_id, visit_occurrence_id ):
    mrn_num = person_id
    enc_id = visit_occurrence_id
    enc_details = VisitOccurrenceModel.objects.get(visit_occurrence_id=enc_id)

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
    
    return render(request, 'encounter.html', {'enc_detail': enc_details, 
                            'observations': observations, "observation_fields": observation_fields,
                            'conditions': conditions, "condition_fields": condition_fields,
                            'notes': notes, "note_fields": note_fields
                     })


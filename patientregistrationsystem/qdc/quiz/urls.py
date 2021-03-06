from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^$', 'quiz.views.contact', name='contact'),
    url(r'^busca/$', 'quiz.views.search_patient', name='search_patient'),
    url(r'^contato/$', 'quiz.views.contact', name='contato'),
    url(r'^busca_avancada/$', 'quiz.views.advanced_search', name='advanced_search'),

    url(r'^patient/new/$', 'quiz.views.patient_create', name='patient_new'),
    url(r'^patient/edit/(?P<patient_id>\d+)/$', 'quiz.views.patient_update', name='patient_edit'),
    url(r'^patient/search/$', 'quiz.views.search_patients_ajax', name='patient_search'),
    url(r'^patient/verify_homonym/$', 'quiz.views.patients_verify_homonym', name='patients_verify_homonym'),
    url(r'^patient/(?P<patient_id>\d+)/$', 'quiz.views.patient', name='patient_view'),
    url(r'^restore/patient/(?P<patient_id>\d+)/$', 'quiz.views.restore_patient', name='patient_restore'),

    # medical_record (create, read, update)
    url(r'^patient/(?P<patient_id>\d+)/medical_record/new/$',
        'quiz.views.medical_record_create', name='medical_record_new'),
    url(r'^patient/(?P<patient_id>\d+)/medical_record/(?P<record_id>\d+)/$',
        'quiz.views.medical_record_view', name='medical_record_view'),
    url(r'^patient/(?P<patient_id>\d+)/medical_record/edit/(?P<record_id>\d+)/$',
        'quiz.views.medical_record_update', name='medical_record_edit'),

    # cid
    url(r'^patient/medical_record/cid-10/$', 'quiz.views.search_cid10_ajax', name='cid10_search'),

    # diagnosis (create, delete, update)
    url(r'^patient/(?P<patient_id>\d+)/medical_record/(?P<medical_record_id>\d+)/diagnosis/(?P<cid10_id>\d+)/$',
        'quiz.views.diagnosis_create', name='diagnosis_create'),
    url(r'^patient/(?P<patient_id>\d+)/medical_record/new/diagnosis/(?P<cid10_id>\d+)/$',
        'quiz.views.medical_record_create_diagnosis_create', name='medical_record_diagnosis_create'),
    url(r'^diagnosis/delete/(?P<patient_id>\d+)/(?P<diagnosis_id>\d+)/$',
        'quiz.views.diagnosis_delete', name='diagnosis_delete'),

    # exam (create, read, update, delete)
    url(r'^patient/(?P<patient_id>\d+)/medical_record/edit/(?P<record_id>\d+)/diagnosis/(?P<diagnosis_id>\d+)/exam/new/$',
        'quiz.views.exam_create', name='exam_create'),
    url(r'^patient/(?P<patient_id>\d+)/medical_record/(?P<record_id>\d+)/exam/(?P<exam_id>\d+)/$',
        'quiz.views.exam_view', name='exam_view'),
    url(r'^patient/(?P<patient_id>\d+)/medical_record/edit/(?P<record_id>\d+)/exam/edit/(?P<exam_id>\d+)/$',
        'quiz.views.exam_edit', name='exam_edit'),
    url(r'^patient/(?P<patient_id>\d+)/medical_record/edit/(?P<record_id>\d+)/exam/remove/(?P<exam_id>\d+)/$',
        'quiz.views.exam_delete', name='exam_delete'),

    # exam file (delete)
    url(r'^exam_file/delete/(?P<exam_file_id>\d+)/$',
        'quiz.views.exam_file_delete', name='exam_file_delete'),
)

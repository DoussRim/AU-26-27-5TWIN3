from django.contrib import admin,messages
from Event.models import Event
from datetime import datetime
# Register your models here.
class FilterEvent(admin.SimpleListFilter):
    title="Event Date"
    parameter_name="evt_date"
    def lookups(self, request, model_admin):
        return (
            ('PE',('Past Events')),
            ('UE',('Upcoming Events')),
            ('TE',('Today Events')),
        )
    def queryset(self, request, queryset):
        if self.value()=='PE':
            return queryset.filter(evt_date__lt=datetime.now())
        if self.value()=='uE':
            return queryset.filter(evt_date__gt=datetime.now())
        if self.value()=='TE':
                    return queryset.filter(evt_date__exact=datetime.now())
        
class EventAdmin(admin.ModelAdmin):
    list_display=('title','description','category','evt_date','creation_date','update_date','organizer','state')
    def accept_state(self,request,queryset):
        req=queryset.update(state=True)
        if req==1:
            msg="1 event was "
        else:
            msg=f' {req} events were'
        messages.success(request, f'{msg} successfully updated')
    accept_state.short_description="state True"
    def refuse_state(self,request,queryset):
            req=queryset.update(state=False)
            if req==1:
                msg="1 event was "
            else:
                msg=f' {req} events were'
            messages.success(request, f'{msg} successfully updated')
    actions=[accept_state,refuse_state]
    search_fields=['title','category']
    list_per_page=2
    ordering=['evt_date']
    list_filter=['title','organizer',FilterEvent]
    readonly_fields=['creation_date','update_date']
    fieldsets=(
        ('A propos',{
            'fields':('title','description','category','image','nbe_participant')
        }),
        ('Event Dates',{
                    'fields':('evt_date','creation_date','update_date')
                }),
        ('State of The Event',{
                            'fields':('state',)
                        }),
        (None,{
                            'fields':('organizer',)
                        }),
    )
    autocomplete_fields=['organizer']
admin.site.register(Event,EventAdmin)
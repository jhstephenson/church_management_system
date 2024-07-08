from django.contrib import admin
from .models import Unit, Organization, Position, Leadership, Calling

admin.site.register(Unit)
admin.site.register(Organization)
admin.site.register(Position)
admin.site.register(Leadership)

@admin.register(Calling)
class CallingAdmin(admin.ModelAdmin):
    list_display = ('person_being_called', 'unit', 'organization', 'position', 'date_called', 'leader_and_clerk_resources_updated')
    list_filter = ('unit', 'organization', 'leader_and_clerk_resources_updated')
    search_fields = ('person_being_called', 'person_being_released')
    date_hierarchy = 'date_called'